def double_print(string: str):
    if len(string) == 0:
        raise ValueError('empty string is not allowed')

    print(string)
    print(string)