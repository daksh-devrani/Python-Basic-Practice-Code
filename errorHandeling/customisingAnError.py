class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__(f'Invalid value for n, WRONG_VALUE. {wrong_value} must be greater than 0.')


def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


count_from_zero_to_n(-10)
