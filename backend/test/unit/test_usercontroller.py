import pytest
import unittest.mock as mock
from src.controllers.usercontroller import UserController


@pytest.fixture
def mocked_dao():
    return mock.MagicMock()


@pytest.fixture
def controller(mocked_dao):
    return UserController(dao=mocked_dao)


@pytest.mark.unit
def test_get_user_by_email_returns_user_when_one_match(controller, mocked_dao):
    user = {'email': 'jane@doe.com', 'name': 'Jane'}
    mocked_dao.find.return_value = [user]

    result = controller.get_user_by_email('jane@doe.com')

    assert result == user


@pytest.mark.unit
def test_get_user_by_email_returns_first_user_when_multiple_matches(controller, mocked_dao, capsys):
    users = [
        {'email': 'jane@doe.com', 'name': 'Jane1'},
        {'email': 'jane@doe.com', 'name': 'Jane2'}
    ]
    mocked_dao.find.return_value = users

    result = controller.get_user_by_email('jane@doe.com')
    captured = capsys.readouterr()

    assert result == users[0]
    assert 'more than one user found' in captured.out


@pytest.mark.unit
def test_get_user_by_email_returns_none_when_no_match(controller, mocked_dao):
    mocked_dao.find.return_value = []

    result = controller.get_user_by_email('jane@doe.com')

    assert result is None


@pytest.mark.unit
def test_get_user_by_email_raises_value_error_for_email_without_at(controller, mocked_dao):
    with pytest.raises(ValueError):
        controller.get_user_by_email('invalid-email')

    mocked_dao.find.assert_not_called()


@pytest.mark.unit
def test_get_user_by_email_raises_value_error_for_email_without_domain_host(controller, mocked_dao):
    with pytest.raises(ValueError):
        controller.get_user_by_email('jane@doe')

    mocked_dao.find.assert_not_called()


@pytest.mark.unit
def test_get_user_by_email_reraises_exception_when_dao_fails(controller, mocked_dao):
    mocked_dao.find.side_effect = Exception('database failure')

    with pytest.raises(Exception):
        controller.get_user_by_email('jane@doe.com')
