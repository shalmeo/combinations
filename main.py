import logging

from fastapi import FastAPI

from app import handlers
from app.core.providers import all_gen_provider, pairwise_gen_provider
from app.utils.all_comb import gen_all_combinations
from app.utils.pairwise_gen import pairwise_gen


logger = logging.getLogger(__name__)


def app():
    application = FastAPI()

    application.dependency_overrides = {
        pairwise_gen_provider: lambda: pairwise_gen,
        all_gen_provider: lambda: gen_all_combinations
    }

    handlers.setup(application)

    return application
