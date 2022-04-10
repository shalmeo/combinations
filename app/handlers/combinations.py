from fastapi import APIRouter, Body, Form
from app.models.parameters import Parameters

from app.utils.all_comb import gen_all_combinations
from app.utils.pairwise_gen import pairwise_gen
from app.models.cond import Conditions


router = APIRouter(tags=["combinations"])


@router.post('/combinations/pair')
async def pairwise(parameters: Parameters, conditions: Conditions):
    can_conditions = conditions.can
    cannot_conditions = conditions.cannot
    
    
    
    response = pairwise_gen(parameters.dict(), can_conditions, cannot_conditions)
    return response


@router.post('/combinations/all')
async def all_combinations(parameters: Parameters, conditions: Conditions):
    can_conditions = conditions.can
    cannot_conditions = conditions.cannot
    
    response = gen_all_combinations(parameters.dict(), can_conditions, cannot_conditions)
    return response
    