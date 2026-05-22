users_db = {}

def get_user(user_id):
    return users_db.get(user_id, None)

def create_user(user_id, name, email):
    users_db[user_id] = {"name": name, "email": email}
    return {"created": True, "id": user_id}
