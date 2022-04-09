import logging

from fastapi import FastAPI

from app import handlers


logger = logging.getLogger(__name__)


def app():
    application = FastAPI()

    handlers.setup(application)

    return application
