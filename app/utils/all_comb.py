import xlsxwriter
import io
import itertools

from fastapi import HTTPException
from starlette.responses import StreamingResponse

from app.models.cond import CondititionsBody


def gen_all_combinations(
    parameters: dict[str, list[str]], conditions: CondititionsBody
) -> StreamingResponse | HTTPException:
    combinations = list(itertools.product(*parameters.values()))
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    header_format = workbook.add_format({"border": 2, "bold": True, "align": "center"})
    row_format = workbook.add_format({"border": 1, "align": "center", "right": 2})
    last_row_format = workbook.add_format(
        {"border": 1, "align": "center", "right": 2, "bottom": 2}
    )
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, parameters.keys(), header_format)
    invalid_combinations = []
    try:
        for combination in combinations:
            if conditions:
                if conditions.can:
                    for condition in conditions.can:
                        if condition:
                            first_item, last_item = condition.values()
                            if (
                                first_item in combination
                                and last_item not in combination
                            ):
                                invalid_combinations.append(combination)

                if conditions.cannot:
                    for condition in conditions.cannot:
                        if condition:
                            first_item, last_item = condition.values()
                            if first_item in combination and last_item in combination:
                                invalid_combinations.append(combination)

        all_combinations = list(set(combinations) - set(invalid_combinations))
        for row, combination in enumerate(all_combinations, 1):
            if row != len(all_combinations):
                worksheet.write_row(row, 0, combination, row_format)
            else:
                worksheet.write_row(row, 0, combination, last_row_format)

    except ValueError:
        return HTTPException(400, "Each parameter arrays must have at least one item")
    finally:
        workbook.close()
        output.seek(0)

    headers = {"Content-Disposition": 'attachment; filename="combinations.xlsx"'}
    return StreamingResponse(output, headers=headers)
