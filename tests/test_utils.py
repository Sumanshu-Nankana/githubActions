from src import utils
import pytest

@pytest.mark.parametrize('x, y, result', 
                            [
                                (10, 10, 20), 
                                ('Hello', 'World', 'HelloWorld'), 
                                (10.5, 0.5, 11)
                        ])
def test_add(x, y, result):
    assert utils.add(x, y) == result


@pytest.mark.parametrize('data, result',
[('Sumanshu Nankana', 'SumanshuNankana'), 
('Sumanshu      Nankana', 'SumanshuNankana')])
def test_remove_spaces(data, result):
    assert utils.remove_spaces(data) == result