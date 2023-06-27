from .AST import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def eat(self, type):
        if self.pos < len(self.tokens) and self.tokens[self.pos].type == type:
            self.pos += 1
            return True
        return False

    def program(self):
        return Program(self.statement_list())

    def statement_list(self):
        statements = [self.statement()]
        while self.pos < len(self.tokens):
            statements.append(self.statement())
        return StatementList(statements)

    def statement(self):
        if self.eat('VAR'):
            return self.declaration_statement()
        elif self.tokens[self.pos].type == 'IDENTIFIER':
            return self.assignment_statement()
        elif self.eat('PRINTLN'):
            return self.print_statement()
        else:
            raise Exception('Unexpected token: ' + self.tokens[self.pos].value)

    def assignment_statement(self):
        id = self.tokens[self.pos].value
        self.eat('IDENTIFIER')
        self.eat('ASSIGN')
        expr = self.expression()
        return AssignmentStatement(Identifier(id), expr)

    def declaration_statement(self):
        id = self.tokens[self.pos].value
        self.eat('IDENTIFIER')
        return DeclarationStatement(Identifier(id))

    def print_statement(self):
        self.eat('LPAREN')
        expr = self.expression()
        self.eat('RPAREN')
        return PrintStatement(expr)

    def expression(self):
        node = self.term()
        while self.eat('PLUS') or self.eat('MINUS'):
            op = Operator(self.tokens[self.pos - 1].value)
            node = BinaryExpression(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.eat('MUL') or self.eat('DIV'):
            op = Operator(self.tokens[self.pos - 1].value)
            node = BinaryExpression(node, op, self.factor())
        return node

    def factor(self):
        if self.eat('NUMBER'):
            return Literal(self.tokens[self.pos - 1].value)
        elif self.eat('IDENTIFIER'):
            return Identifier(self.tokens[self.pos - 1].value)
        elif self.eat('LPAREN'):
            node = self.expression()
            self.eat('RPAREN')
            return node
        else:
            raise Exception('Unexpected token: ' + self.tokens[self.pos].value)

if __name__ == '__main__':
    from lexer import Lexer, Token
    lexer = Lexer('x := 42')
    tokens = []
    while (tok := lexer.next_token()) != Token('EOF', None):
        tokens.append(tok)
    parser = Parser(tokens)
