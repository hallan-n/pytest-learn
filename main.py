from pytest import mark


@mark.parametrize("num", [2, 4, 6, 8, 0])
def teste_return_true_if_number_is_pair(num: int):
    assert num % 2 == 0
