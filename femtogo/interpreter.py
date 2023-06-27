class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def visit_Program(self, node):
        return self.visit(node.statements)

    def visit_StatementList(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_AssignmentStatement(self, node):
        self.variables[node.identifier.name] = self.visit(node.expression)

    def visit_DeclarationStatement(self, node):
        self.variables[node.identifier.name] = None

    def visit_PrintStatement(self, node):
        print(self.visit(node.expression))

    def visit_BinaryExpression(self, node):
        if node.operator.op == '+':
            return self.visit(node.left_expression) + self.visit(node.right_expression)
        elif node.operator.op == '-':
            return self.visit(node.left_expression) - self.visit(node.right_expression)
        elif node.operator.op == '*':
            return self.visit(node.left_expression) * self.visit(node.right_expression)
        elif node.operator.op == '/':
            return self.visit(node.left_expression) / self.visit(node.right_expression)

    def visit_Identifier(self, node):
        return self.variables[node.name]

    def visit_Literal(self, node):
        return node.value

if __name__ == '__main__':
    from lexer import Lexer, Token
    from parser import Parser
    lexer = Lexer('''
    var x
    x = 42

    x = x + 2

    Println(x)
    ''')
    parser = Parser(lexer.tokenize())
    interpreter = Interpreter()
    interpreter.visit(parser.program())
