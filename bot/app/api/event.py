from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    id: int
    title: str
    event_date: datetime
    location: str
    # rsvp_link: str
    source_url: str

