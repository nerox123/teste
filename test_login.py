import pytest
from test1 import verificar_login, criar_conta, usuarios

@pytest.fixture(autouse=True)
def reset_usuario():
    usuarios.clear()
    usuarios.update({"admin": "1234"})
    
def test_login_valido():
    assert verificar_login("admin", "1234") == True

def test_criar_conta_sucesso():
    resultado = criar_conta("novo", "123")
    assert resultado == "sucesso"
    assert usuarios["novo"] == "123"
    
def test_criar_usuario_existente():
    resultado = criar_conta("admin", "1234")
    assert resultado == "usuario existente"
    
def test_criar_conta_vazio():
    assert criar_conta("", "123") == "campos vazios"
    
def test_criar_conta_senha_vazia():
    assert criar_conta("user", "") == "campos vazios"
    
def test_criar_conta_ambas_vazias():
    assert criar_conta("", "") == "campos vazios"
