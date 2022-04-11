from fastapi import APIRouter, Depends

from app.core.providers import all_gen_provider, pairwise_gen_provider
from app.models.parameters import Parameters
from app.models.cond import Conditions


router = APIRouter(tags=["combinations"])


@router.post('/combinations/pair')
async def pairwise(
    parameters: Parameters,
    conditions: Conditions,
    pairwise_gen = Depends(pairwise_gen_provider)
):
    can_conditions = conditions.can
    cannot_conditions = conditions.cannot
    
    response = pairwise_gen(parameters.dict(), can_conditions, cannot_conditions)
    return response


@router.post('/combinations/all')
async def all_combinations(
    parameters: Parameters,
    conditions: Conditions,
    all_gen = Depends(all_gen_provider)
):
    can_conditions = conditions.can
    cannot_conditions = conditions.cannot
    
    response = all_gen(parameters.dict(), can_conditions, cannot_conditions)
    return response
    