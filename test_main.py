from main import greet, farewell, greet_all

def test_greet():
    assert greet("Anna") == "Hello, Anna!"

def test_farewell():
    assert farewell("Anna") == "Goodbye, Anna!"

def test_greet_all():
    assert greet_all(["A", "B"]) == ["Hello, A!", "Hello, B!"]
