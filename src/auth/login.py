def login(username, password):
    if not username or not password:
        return {"success": False, "error": "Missing credentials"}
    return {"success": True, "token": "abc123"}
