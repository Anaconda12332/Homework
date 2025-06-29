import pytest


@pytest.fixture(scope="session")
def default_messages():
    print("[setup] default_messages")
    return [
        "Hello there!",
        "This is urgent!",
        "   ",
        "Another one.",
        ""
    ]


@pytest.fixture(scope="function")
def clean_messages(default_messages):
    print("[setup] clean_messages")
    return default_messages  #[msg for msg in default_messages if msg.strip()]
