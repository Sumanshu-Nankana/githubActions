from src import validate
import pytest

@pytest.mark.parametrize('email, result',
[('sumanshunankana@gmail.com', True), 
('Sumanshu      Nankana', False)])
def test_validate_email(email, result):
    assert validate.validate_email(email) == result