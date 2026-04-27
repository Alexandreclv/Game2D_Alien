import pytest
from src.desconto import DescontoNormal, DescontoVIP, DescontoPremium

def test_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10.0, f"Esperado 10.0, mas obteve {resultado}"

@pytest.fixture
def desconto_vip():
    return DescontoVIP()

def test_desconto_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20.0, "Desconto VIP para 100 deve ser 20.0"

def test_desconto_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40.0, "Desconto VIP para 200 deve ser 40.0"

@pytest.mark.parametrize("valor, esperado", [
    (100, 30.0),
    (200, 60.0),
    (300, 90.0)
])

def test_desconto_premium(valor, esperado):
    desconto = DescontoPremium()
    resultado = desconto.calcular(valor)

    assert resultado == esperado, f"Esperado {esperado}, mas obteve {resultado}"