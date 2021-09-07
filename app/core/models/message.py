from pydantic import BaseModel, Field
from typing import Optional, List
from .profile import Profile
import datetime


class Message(BaseModel):
    msg_id: int = Field(...)
    profile: str = Field(...)
    full_text: str = Field(...)
    created_at: int = Field(...)
    retweet_count: int = Field(...)
    favorite_count: int = Field(...)
    retweeted: bool = Field(...)
    lang: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "msg_id":"1415800210685677569",
                "profile": "VancityReynolds",
                "full_text":"Oh, you can see where I hide my phone",
                "created_at": "Thu Jul 15 22:27:29 +0000 2021",
                "favorite_count": 12810,
                "retweet_count": 160,
                "hashtags": [],
                "mentions": ["RealHughJackman",],
                "urls": [],
                "media": [],
                "retweeted": False,
                "lang": "en"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
