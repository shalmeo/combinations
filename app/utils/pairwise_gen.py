import functools
import xlsxwriter

from io import BytesIO
from fastapi import HTTPException
from starlette.responses import StreamingResponse
from allpairspy import AllPairs

from app.models.cond import CondititionsBody


def is_valid_combination(row, conditions: CondititionsBody):
    if conditions:
        if conditions.can:
            for condition in conditions.can:
                if condition:
                    first_item, last_item = condition.values()
                    if first_item in row and last_item not in row:
                        return False

        if conditions.cannot:
            for condition in conditions.cannot:
                if condition:
                    if set(condition.values()).issubset(set(row)):
                        return False
    return True


def pairwise_gen(
    parameters: dict[str, list[str]], conditions: CondititionsBody
) -> StreamingResponse | HTTPException:
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    header_format = workbook.add_format({"border": 2, "bold": True, "align": "center"})
    row_format = workbook.add_format({"border": 1, "align": "center", "right": 2})
    last_row_format = workbook.add_format(
        {"border": 1, "align": "center", "right": 2, "bottom": 2}
    )
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, parameters.keys(), header_format)
    try:
        pairs = list(
            filter(
                functools.partial(is_valid_combination, conditions=conditions),
                AllPairs(parameters.values()),
            )
        )
        for row, combination in enumerate(pairs, 1):
            if row != len(pairs):
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
