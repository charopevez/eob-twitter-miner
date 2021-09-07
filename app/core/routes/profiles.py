from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from core.services import miner
from core.db.storage import *
from core.models.profile import *
import time

router = APIRouter()


@router.get("/{id}", response_description="Get twitter user profile")
async def get_profile(id:str):
    json_responce=miner.get_profile_data(username=id)
    new_profile={"screen_name":id}
    new_profile["location"]=json_responce["location"]
    new_profile["user_id"]=json_responce["id"]
    new_profile["name"]=json_responce["name"]
    new_profile["description"]=json_responce["description"]
    new_profile["followers_count"]=json_responce["followers_count"]
    new_profile["friends_count"]=json_responce["friends_count"]
    new_profile["created_at"]=time.mktime(time.strptime(json_responce["created_at"],"%a %b %d %H:%M:%S +0000 %Y"))
    new_profile["verified"]=json_responce["verified"]
    new_profile["profile_image_url"]=json_responce["profile_image_url"].replace("_normal","")
    new_profile["profile_banner_url"]=json_responce["profile_banner_url"]
    added_profile = await add_profile(new_profile)
    return ResponseModel(added_profile, "Profile mined successfully.")
