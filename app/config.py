from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class LLMOptions(BaseModel):
    api_key: str
    base_url: str


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='_', env_nested_max_split=1)

    bot_token: str
    llm: LLMOptions

    logging_path: str = 'logs'
    log_level: str = 'INFO'


config = Config(_env_file='.env')

__all__ = ["config", "LLMOptions"]
