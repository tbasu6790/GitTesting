from src.auth.login import login

def test_login_success():
    result = login("alice", "pass123")
    assert result["success"] == True

def test_login_missing():
    result = login("", "")
    assert result["success"] == False
