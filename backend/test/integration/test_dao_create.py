import pytest
import pymongo

from src.util.dao import DAO
from src.util.validators import getValidator, validators

TEST_COLLECTION = "user_test"
TEST_MONGO_URL = "mongodb://localhost:27017"


@pytest.fixture
def dao(monkeypatch):
    monkeypatch.setenv("MONGO_URL", TEST_MONGO_URL)
    validators[TEST_COLLECTION] = getValidator("user")

    client = pymongo.MongoClient(TEST_MONGO_URL, serverSelectionTimeoutMS=2000)
    client.admin.command("ping")
    database = client.edutask

    if TEST_COLLECTION in database.list_collection_names():
        database.drop_collection(TEST_COLLECTION)

    sut = DAO(collection_name=TEST_COLLECTION)

    yield sut

    database.drop_collection(TEST_COLLECTION)
    validators.pop(TEST_COLLECTION, None)
    client.close()


@pytest.mark.integration
def test_create_user_succeeds_with_valid_data(dao):
    user_data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@example.com",
    }

    result = dao.create(user_data)

    assert result["firstName"] == user_data["firstName"]
    assert result["lastName"] == user_data["lastName"]
    assert result["email"] == user_data["email"]
    assert "_id" in result


@pytest.mark.integration
def test_create_user_fails_when_required_field_missing(dao):
    user_data = {
        "firstName": "Jane",
        "lastName": "Doe",
    }

    with pytest.raises(pymongo.errors.WriteError):
        dao.create(user_data)


@pytest.mark.integration
def test_create_user_fails_when_field_is_wrong_type(dao):
    user_data = {
        "firstName": 123,
        "lastName": "Doe",
        "email": "jane.doe@example.com",
    }

    with pytest.raises(pymongo.errors.WriteError):
        dao.create(user_data)


@pytest.mark.integration
def test_create_user_fails_for_duplicated_email(dao):
    first_user = {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@example.com",
    }
    second_user = {
        "firstName": "Janet",
        "lastName": "Doe",
        "email": "jane.doe@example.com",
    }

    dao.create(first_user)

    with pytest.raises(pymongo.errors.WriteError):
        dao.create(second_user)
