from pymongo import MongoClient
from core.config.config import Config
from constants import CONFIG_FILE_PATH
from core.models.message import Message
from core.models.profile import Profile
import motor.motor_asyncio
from .helper import profileEntity, messageEntity

# ToDo create config from file
config = Config(yaml_file=CONFIG_FILE_PATH)
engine = "mongodb"
user = "eobuser"
password = "eobuserpass"
auth_db = "eob_system"
host = "eobdb-service"
port = "10010"
uri = "mongodb://%s:%s@%s:%s/%s" % (
    user, password, host, port, auth_db)
db = motor.motor_asyncio.AsyncIOMotorClient(uri) 
storage = db.eob_system
profiles = storage.get_collection("twitter_id")  # ?profiles collection
messages = storage.get_collection("twitter_msg")  # ?message collection



async def add_profile(profile_data: dict)->dict:
    """Add twitter profile to db"""
    #check if profile exists
    profile = await profiles.find_one({"screen_name": profile_data["screen_name"]})
    if profile is not None:
        return profileEntity(profile)
    new_profile = await profiles.insert_one(profile_data)
    added_record = await profiles.find_one({"_id": new_profile.inserted_id})
    return profileEntity(added_record) 

# ToDo
def update_profile(profileEntity: dict):
    """Update twitter profile to db"""

    profiles.insert_one(p)


async def get_messages_id(profile:str)->[str]:
    existing_ids=[]
    async for message in messages.find({"profile":profile}):
        existing_ids.append(message["msg_id"])
    return existing_ids


async def add_profile_messages(messages_data: [dict])->dict:
    """Add twitter msgs from user to db"""
    if len(messages_data)>0:
        message_list=[]
        profile=messages_data[0]["profile"]
        await messages.insert_many(messages_data)
        async for message in messages.find({"profile":profile}):
            message_list.append(messageEntity(message))
        return message_list
    else:
        return "No new messages"


async def add_message(messageEntity: dict)->dict:
    """Add twitter msg to db"""
    message = await messages.insert_one(messageEntity)
    added_record = await messages.find_one({"_id": message.inserted_id})
    return messageEntity(added_record) 