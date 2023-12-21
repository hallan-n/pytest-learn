from pytest import mark
import sys


@mark.tag  # Define um grupo para ser testado, nesse caso, tag
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
