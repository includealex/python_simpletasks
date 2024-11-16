class ParseError(Exception):
    """ Error while parsing file """

    line_no:int = None
    text:str = None

    def __init__(self, *args, line_no:int=None, text:str=None):
        super().__init__(*args)

        if line_no is not None:
            self.line_no = line_no
        if text is not None:
            self.text = text
    
    def __str__(self):
        if self.line_no is not None and self.text is not None:
            return f"cannot parse text on line {self.line_no}: '{self.text}'"
        if self.line_no is not None:
            return f"cannot parse text on line {self.line_no}"
        if self.text is not None:
            return f"cannot parse text: '{self.text}'"

        return super().__str__()

