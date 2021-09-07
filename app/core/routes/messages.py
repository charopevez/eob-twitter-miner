from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import time
from core.db.storage import *
from core.models.message import *
from core.services.miner import *

router = APIRouter()


@router.get("/{id}", response_description="Get twitter user messages")
async def get_messages(id):
    json_responce=miner.get_profile_data(username=id)
    message = await add_message(id)
    return ResponseModel(message, "Student data retrieved successfully") 

@router.get("/profile/{id}/{n}", response_description="Get twitter user messages")
async def get_profile_messages(id,n):
    json_responce=get_profile_tweets(username=id, n=n)
    existing_id = await get_messages_id(id)
    new_messages=[]
    for data in json_responce:
        message={"profile":id}
        message["msg_id"] = data._json["id"]
        if message["msg_id"] not in existing_id:
            message["full_text"] = data._json["full_text"]
            message["created_at"] = time.mktime(time.strptime(data._json["created_at"],"%a %b %d %H:%M:%S +0000 %Y"))
            message["retweet_count"] = data._json["retweet_count"]
            message["favorite_count"] = data._json["favorite_count"]    
            message["retweeted"] = data._json["retweeted"]
            message["lang"] = data._json["lang"]
            new_messages.append(message)
    
    all_messages = await add_profile_messages(new_messages)
    return ResponseModel(all_messages, "Student data retrieved successfully") \

