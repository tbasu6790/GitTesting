def logout(token):
    if not token:
        return {"success": False}
    return {"success": True, "message": "notLogged out"}
