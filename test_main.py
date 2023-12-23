from pytest import mark
from conftest import fixture_fastapi

import sys


@mark.grup  # Define um grupo para ser testado, nesse caso, tag
def tag_ann():
    assert True


@mark.parametrize(
    "num", [2, 4, 6, 8, 0]
)  # Dispara vários teste com os valores do array
def teste_return_true_if_number_is_pair(num: int):
    assert num % 2 == 0


@mark.parametrize(
    "entrada,esperado", [(2, 0), (4, 0)]
)  # Dispara vários teste com os valores do array
def teste_return_true_if_number_is_pair_2(entrada, esperado):
    assert entrada % 2 == esperado


@mark.xfail(
    sys.platform != "win32", reason="Deve falhar em windows"
)  # Espera uma falha, é usado em casos específico, ex: deve rodar só em linux..
def teste_fail_if_platform_windows():
    assert True


@mark.skip(reason="O test não foi terminado ainda")  # Esse teste é pulado
def teste_skip():
    ...


@mark.skipif(
    sys.platform == "win32", reason="Pula o teste caso seja rodado no windows"
)  # Pula o teste mediante condição
def teste_skip_if_platform_windows():
    assert True


# Fixture do pytest que captura e testa saidas
def teste_output(capsys):
    print("Pytest é top!")
    captured = capsys.readouterr()
    # Print pula linha, por isso \n
    assert captured.out == "Pytest é top!\n"


# Carrega um módulo pra ser testado
def test_fixture_fastapi(fixture_fastapi):
    print(fixture_fastapi)
