from fastapi import APIRouter

from app.utils.all_comb import gen_all_combinations
from app.utils.pairwise_gen import pairwise_gen
from app.models.cond import Conditions


router = APIRouter(tags=["combinations"])


@router.post('/api/combinations/pair')
async def pairwise(parameters: dict[str, list[str]], conditions: Conditions):
    can_conditions = conditions.can
    cannot_conditions = conditions.cannot
    
    response = pairwise_gen(parameters, can_conditions, cannot_conditions)
    return response


@router.post('/api/combinations/all')
async def all_combinations(parameters: dict[str, list[str]], conditions: Conditions):
    can_conditions = conditions.can
    cannot_conditions = conditions.cannot
    
    response = gen_all_combinations(parameters, can_conditions, cannot_conditions)
    return response
    