from src.calculadora import soma, subtrai, multiplica, divide, eh_par
import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(10, 5) == 5

def test_multiplica():
    assert multiplica(3, 4) == 12

def test_divide():
    assert divide(8, 2) == 4

def test_divide_por_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_eh_par():
    assert eh_par(4)
    assert not eh_par(5)
