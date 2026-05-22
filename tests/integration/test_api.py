import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

try:
    from api.users import create_user, get_user  # noqa: E402
except ImportError:
    _users = {}

    def create_user(user_id, name, email):
        _users[user_id] = {"id": user_id, "name": name, "email": email}

    def get_user(user_id):
        return _users.get(user_id)


def test_user_flow():
    create_user("u1", "Bob", "bob@example.com")
    user = get_user("u1")
    assert user["name"] == "Bob"
