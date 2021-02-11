# tokens (to keep track of what the computer reads)
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}: {self.value}" if self.value else f"{self.type}"


# a list of pinite tokens
PT_INT = "INT"
PT_FLOAT = "FLOAT"
PT_STRING = "STR"
PT_PLUS = "PLUS"
PT_MINUS = "MINUS"
PT_MUL = "MUL"
PT_DIV = "DIV"


# a class that reads our programming language
class Pinite:
    def __init__(self, line):
        self.line = line
        self.pos = -1
        self.current_char = None

    # a method to go to the next position
    def move(self):
        self.pos += 1
        self.current_char = self.line[self.pos] if self.pos < len(self.line) else None

    # get all the tokens
    def get_tokens(self):
        tokens = []
        self.move()

        while self.current_char:
            # ignore empty spaces
            if self.current_char in " \t":
                self.move()

            # check for integers and floats
            elif self.current_char.isnumeric():
                tokens.append(self.build_number())

            # check for strings
            elif self.current_char == "\"":
                self.move()
                tokens.append(self.build_string())

            # check for operations
            elif self.current_char == "+":
                tokens.append(Token(PT_PLUS))
                self.move()
            elif self.current_char == "-":
                tokens.append(Token(PT_MINUS))
                self.move()
            elif self.current_char == "*":
                tokens.append(Token(PT_MUL))
                self.move()
            elif self.current_char == "/":
                tokens.append(Token(PT_DIV))
                self.move()

            # if the symbol is not recognized
            else:
                return "Invalid line!"

        return tokens

    # a function to build a number if one is inputed
    def build_number(self):
        # keep count of the dots to know if it's a float or integer
        dot_count = 0
        number = ""
        # read the number
        while self.current_char and self.current_char.isnumeric() or self.current_char == '.':
            number += self.current_char
            if self.current_char == '.':
                if dot_count == 0:
                    dot_count = 1
                else:
                    return "Invalid line!"
            self.move()
        # return the number
        return Token(PT_INT, int(number)) if dot_count == 0 else Token(PT_FLOAT, float(number))

    # a function to build a string after quotation
    def build_string(self):
        string = ""
        while self.current_char and self.current_char != "\"":
            string += self.current_char
            self.move()
        print(string)
        # if the string is not closed
        if not self.current_char:
            return "Invalid line!"
        else:
            self.move()
            return Token(PT_STRING, string)
