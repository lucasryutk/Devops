from src.main import *
from unittest.mock import patch
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()

    assert result == {"message": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Lucas", curso="ADS", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(1)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-1)
    yield result
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(-1)
    assert result
