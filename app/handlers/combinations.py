import random
import string

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.providers import all_gen_provider, pairwise_gen_provider, session_provider
from app.database.models import Combination
from app.models.parameters import Parameters
from app.models.cond import Conditions


router = APIRouter(tags=["combinations"])


@router.get('/combinations/{hash_id}')
async def get_combination(hash_id: str, session: AsyncSession = Depends(session_provider)):
    combination: Combination = await session.get(Combination, hash_id)
    
    if not combination:
        raise HTTPException(status_code=404, detail='Combination not found')
    
    return {'status': 'OK', 'combination': combination.data}


@router.post('/combinations')
async def create_combination(data: dict, session: AsyncSession = Depends(session_provider)):
    letters = string.ascii_letters + string.digits
    combinations: Combination = (await session.scalars(select(Combination))).all()
    
    while True:
        hash_id = ''.join(random.choice(letters) for _ in range(6))
        hash_exists = list(filter(lambda c: c.hash == hash_id, combinations))
        if not hash_exists:
            await session.merge(Combination(hash=hash_id, data=data))
            break
    
    await session.commit()
    return {'status': 'OK', 'hash': hash_id}
        
    


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
    