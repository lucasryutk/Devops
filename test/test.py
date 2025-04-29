from src.main import *
from unittest.mock import patch


def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()
        yield result
    assert result == {"teste": True, "num_aleatorio": 13245}

def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Lucas", curso="ADS", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result

def test_update_estudante_negativo(id_estudante: int):
    result = update_estudante(-5)
    yield result
    assert not result

def test_update_estudante_positivo(id_estudante: int):
    result = update_estudante(1)
    yield update_estudante(1)
    assert not result

def test_delete_estudante_negativo(id_estudante: int):
    result = delete_estudante(-1)
    yield result
    assert not result

def test_delete_estudante_positivo(id_estudante: int):
    result = delete_estudante(-1)
    yield result
    assert not result
