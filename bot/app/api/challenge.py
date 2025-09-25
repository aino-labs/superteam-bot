from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Challenge(BaseModel):
    id: int
    title: str
    prize: str
    deadline: datetime
