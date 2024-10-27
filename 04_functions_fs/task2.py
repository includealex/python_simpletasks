def last_discharge(a):
    if a.isdigit():
        return int(a) - 1

    return float(a) - 10 ** (-len(a.split('.')[1]))

