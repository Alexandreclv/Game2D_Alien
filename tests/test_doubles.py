from tests.doubles import StubSemDesconto
from src.desconto import Pedido


def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto()) # Usa o stub que retorna 0.0 para o desconto
    assert pedido.total(100) == 100.0 # Verifica se o total é igual ao valor original, já que o desconto é 0.0  

def test_pedido_com_mock_desconto(mocker):
    
    mock_desconto = mocker.Mock()
    mock_desconto.calcular.return_value = 10.0 # Configura o mock para retornar um desconto de 20.0

    pedido = Pedido(mock_desconto) # Usa o mock para o desconto
    resultado = pedido.total(100) # Calcula o total com o mock

    assert resultado == 90.0 # Verifica se o total é 90.0, já que o desconto é 10.0

    mock_desconto.calcular.assert_called() # Verifica se o método calcular foi chamado corretamente com o valor 100
    mock_desconto.calcular.assert_called_with(100) # Verifica se o método calcular foi chamado com o valor 100
    assert mock_desconto.calcular.call_count == 1 # Verifica se o método calcular foi chamado exatamente uma vez