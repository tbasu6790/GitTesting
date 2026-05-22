def test_user_flow():
    from src.api.users import create_user, get_user
    create_user("u1", "Bob", "bob@example.com")
    user = get_user("u1")
    assert user["name"] == "Bob"
