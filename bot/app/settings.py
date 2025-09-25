from pydantic import BaseModel


class DataSource(BaseModel):
    url: str
    update_interval: int


class LLMSettings(BaseModel):
    language: str
    max_answer_length: int
    use_emoji: bool


class Messages(BaseModel):
    start: str
    privacy: str
    event_description: str
    challenge_description: str


class Settings(BaseModel):
    faq: list[str]
    messages: Messages
    sources: dict[str, DataSource]
    llm: LLMSettings



with open("settings.json", "r", encoding="utf-8") as f:
    settings = Settings.model_validate_json(f.read())

with open('knowledgebase.md', 'r') as f:
    kb = f.read()


__all__ = ["settings", 'kb']
