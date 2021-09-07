from pydantic import BaseModel, Field
from typing import Optional
import datetime


class Profile(BaseModel):
    user_id: Optional[int]
    name: Optional[str]
    screen_name: str
    location: Optional[str]
    description: Optional[str]
    followers_count: Optional[int]
    friends_count: Optional[int]
    created_at: Optional[int]
    verified: Optional[bool]
    profile_image_url: Optional[str]
    profile_banner_url: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_id": "2893511188",
                "name": "Ryan Reynolds",
                "screen_name": "VancityReynolds",
                "location": "\ud83c\udde8\ud83c\udde6 & \ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc77\udb40\udc6c\udb40\udc73\udb40\udc7f",
                "description": "owner: @aviationgin - @MintMobile - @maximumeffort - @Wrexham_AFC",
                "followers_count": "17751144",
                "friends_count": "999",
                "created_at": "Wed Nov 26 16:12:27 +0000 2014",
                "verified": True,
                "profile_image_url": "http://pbs.twimg.com/profile_images/1299844050208555008/7wMQaJRA",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/2893511188/1620251003"
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
