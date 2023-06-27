import io
import sys
import contextlib
from tinygo.lexer import Lexer
from tinygo.parser import Parser
from tinygo.interpreter import Interpreter

def interpret(program: str) -> str:
    lexer = Lexer(program)
    parser = Parser(lexer.tokenize())
    ast = parser.program()
    interpreter = Interpreter()
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    with contextlib.redirect_stdout(new_stdout):
        interpreter.visit(ast)
    sys.stdout = old_stdout
    return new_stdout.getvalue().strip()  # get stdout content, remove trailing newline

def test_declaration_assignment_and_print():
    program = """
    var a
    a = 5
    Println(a)
    """
    assert interpret(program) == "5"

def test_arithmetic_expression():
    program = """
    var a
    a = 5 + 3
    Println(a)
    """
    assert interpret(program) == "8"

def test_arithmetic_expression_with_parentheses():
    program = """
    var a
    a = (5 + 3) * 2
    Println(a)
    """
    assert interpret(program) == "16"

def test_expression_with_multiple_variables():
    program = """
    var a
    var b
    a = 5
    b = 3
    Println(a + b)
    """
    assert interpret(program) == "8"

def test_expression_with_uninitialized_variable():
    program = """
    var a
    Println(a)
    """
    assert interpret(program) == "None"
