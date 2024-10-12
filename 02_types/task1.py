def output_info(months, n):
    if n < 1 or n > 12:
            print("ошибка")
            return

    idx = n - 1
    print(months[idx])

    if idx in [0, 1, 11]:
        print("зима")

    elif 2 <= idx <= 4:
        print("весна")

    elif 5 <= idx <= 7:
        print("лето")

    elif 8 <= idx <= 10:
        print("осень")


months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
n = int(input())
output_info(months, n)

