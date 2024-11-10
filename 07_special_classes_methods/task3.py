class Number:
    value: int = None
    _operation: str = None

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return str(self.value)

    @property
    def plus(self):
        self._operation = "plus"
        return self

    @property
    def minus(self):
        self._operation = "minus"
        return self

    @property
    def times(self):
        self._operation = "times"
        return self

    def __getattr__(self, name: str):
        if name in globals() and isinstance(globals()[name], Number):
            other = globals()[name]
            if self._operation == "plus":
                return Number(self.value + other.value)
            elif self._operation == "minus":
                return Number(self.value - other.value)
            elif self._operation == "times":
                return Number(self.value * other.value)
        raise AttributeError(f"'Number' object has no attribute '{name}'")


names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
values = range(10)

for name, value in zip(names, values):
    globals()[name] = Number(value)

