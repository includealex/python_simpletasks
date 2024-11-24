from datetime import date

def days_lived(year: int, month: int, day: int):
    date_input = date(year=year, month=month, day=day)
    current_date = date.today()

    delta = current_date - date_input

    res = delta.days
    return res

