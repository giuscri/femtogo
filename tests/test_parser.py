from tinygo.AST import *
from tinygo.parser import Parser
from tinygo.lexer import Lexer

def ast_to_string(node):
    if isinstance(node, Program):
        return f"Program({', '.join(ast_to_string(stmt) for stmt in node.statements)})"
    elif isinstance(node, DeclarationStatement):
        return f"Declaration({node.identifier.name})"
    elif isinstance(node, AssignmentStatement):
        return f"Assignment({node.identifier.name}, {ast_to_string(node.expression)})"
    elif isinstance(node, PrintStatement):
        return f"Print({ast_to_string(node.expression)})"
    elif isinstance(node, BinaryExpression):
        return f"BinExpr({ast_to_string(node.left_expression)}, {node.operator.op}, {ast_to_string(node.right_expression)})"
    elif isinstance(node, Identifier):
        return f"Id({node.name})"
    elif isinstance(node, Literal):
        return f"Literal({node.value})"
    else:
        raise ValueError(f"Unexpected type {type(node)}")

def parse(text):
    lexer = Lexer(text)
    parser = Parser(lexer.tokenize())
    tree = parser.program()
    return ast_to_string(tree)

def test_declaration_statement():
    assert parse("var a") == "Program(Declaration(a))"

def test_assignment_statement():
    assert parse("a := 5") == "Program(Assignment(a, Literal(5)))"

def test_print_statement():
    assert parse("Println(a)") == "Program(Print(Id(a)))"

def test_binary_expression():
    assert parse("a := 5 + 3") == "Program(Assignment(a, BinExpr(Literal(5), +, Literal(3))))"

def test_expression_in_parentheses():
    assert parse("a := (5 + 3) * 2") == "Program(Assignment(a, BinExpr(BinExpr(Literal(5), +, Literal(3)), *, Literal(2))))"
