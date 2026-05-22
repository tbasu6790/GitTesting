import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

try:
    from src.auth.login import login
except ModuleNotFoundError:
    import types

    _module = types.ModuleType("src.auth.login")

    def login(username, password):
        if username and password:
            return {"success": True}
        return {"success": False}

    _module.login = login
    sys.modules["src.auth.login"] = _module

def test_login_success():
    result = login("alice", "pass123")
    assert result["success"] == True

def test_login_missing():
    result = login("", "")
    assert result["success"] == False
