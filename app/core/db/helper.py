def profileEntity(profile) -> dict:
    return {
        "eob_id": str(profile["_id"]),
        "user_id": profile["user_id"],
        "name": profile["name"],
        "screen_name": profile["screen_name"],
        "location": profile["location"],
        "description": profile["description"],
        "followers_count": profile["followers_count"],
        "friends_count": profile["friends_count"],
        "created_at": profile["created_at"],
        "verified": profile["verified"],
        "profile_image_url": profile["profile_image_url"],
        "profile_banner_url": profile["profile_banner_url"]
    }

def messageEntity(msg) -> dict:
    return {
        "id": str(msg['_id']),
        "msg_id": msg["msg_id"],
        "full_text":msg["full_text"],
        "created_at":msg["created_at"],
        "retweet_count":msg["retweet_count"],
        "favorite_count":msg["favorite_count"],
        "retweeted": msg["retweeted"],
        "lang": msg["lang"]
    }