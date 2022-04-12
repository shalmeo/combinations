from dataclasses import dataclass

from environs import Env


@dataclass
class Database:
    login: str
    password: str
    host: str
    port: int
    name: str


@dataclass
class Config:
    db: Database


def load_config(path: str = '.env'):
    env = Env()
    env.read_env(path)

    return Config(
        db=Database(
            login=env.str('DB_LOGIN'),
            password=env.str('DB_PASS'),
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            name=env.str('DB_NAME'),
        )
    )