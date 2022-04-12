import logging

from fastapi import FastAPI

from app import handlers
from app.core.providers import all_gen_provider, pairwise_gen_provider, session_provider
from app.core.settings import load_config
from app.database.utils import get_connection_string, session_getter
from app.utils.all_comb import gen_all_combinations
from app.utils.pairwise_gen import pairwise_gen


logger = logging.getLogger(__name__)


def app():
    application = FastAPI()
    config = load_config()

    application.dependency_overrides = {
        session_provider: session_getter(get_connection_string(config.db)),
        pairwise_gen_provider: lambda: pairwise_gen,
        all_gen_provider: lambda: gen_all_combinations
    }

    handlers.setup(application)

    return application
