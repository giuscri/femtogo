from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str

class Lexer:
    def __init__(self, text):
        self.text = text
        self.current_char = text[0]
        self.pos = 0

    def error(self):
        raise Exception('Invalid character')

    def tokenize(self):
        tokens = []
        while (tok := self.next_token()) != Token('EOF', None):
            tokens.append(tok)
        return tokens

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def word(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return result

    def next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isalpha():
                word = self.word()
                if word in ['var', 'Println']:
                    return Token(word.upper(), word)
                return Token('IDENTIFIER', word)
            elif self.current_char.isdigit():
                return Token('NUMBER', self.integer())
            elif self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')
            elif self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')
            elif self.current_char == '*':
                self.advance()
                return Token('MUL', '*')
            elif self.current_char == '/':
                self.advance()
                return Token('DIV', '/')
            elif self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')
            elif self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')
            elif self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('EQUAL', '==')
                return Token('ASSIGN', '=')
            elif self.current_char == ':':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('ASSIGN', ':=')
                # return Token('COLON', ':')

            self.error()

        return Token('EOF', None)

if __name__ == '__main__':
    # Use this space for quick testing lexer outputs.

    lexer = Lexer('a := 42')
