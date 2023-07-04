from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'BlogPost'
    app_desc: Optional[str]
    database_url: str = 'sqlite+aiosqlite:///./blogpost.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
