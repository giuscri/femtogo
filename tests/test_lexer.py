from femtogo.lexer import Lexer, Token

def collect_tokens(lexer):
    tokens = []
    while (token := lexer.next_token()).type != 'EOF':
        tokens.append(token)
    return tokens

def test_single_assignment():
    lexer = Lexer('a = 5')
    tokens = collect_tokens(lexer)
    assert tokens == [
        Token('IDENTIFIER', 'a'),
        Token('ASSIGN', '='),
        Token('NUMBER', 5),
    ]

def test_multiple_assignment():
    lexer = Lexer('a = 5 b := 3')
    tokens = collect_tokens(lexer)
    assert tokens == [
        Token('IDENTIFIER', 'a'),
        Token('ASSIGN', '='),
        Token('NUMBER', 5),
        Token('IDENTIFIER', 'b'),
        Token('ASSIGN', ':='),
        Token('NUMBER', 3),
    ]

def test_declaration():
    lexer = Lexer('var a')
    tokens = collect_tokens(lexer)
    assert tokens == [
        Token('VAR', 'var'),
        Token('IDENTIFIER', 'a'),
    ]

def test_print_statement():
    lexer = Lexer('Println(a)')
    tokens = collect_tokens(lexer)
    assert tokens == [
        Token('PRINTLN', 'Println'),
        Token('LPAREN', '('),
        Token('IDENTIFIER', 'a'),
        Token('RPAREN', ')'),
    ]

def test_expression():
    lexer = Lexer('a = b + 3')
    tokens = collect_tokens(lexer)
    assert tokens == [
        Token('IDENTIFIER', 'a'),
        Token('ASSIGN', '='),
        Token('IDENTIFIER', 'b'),
        Token('PLUS', '+'),
        Token('NUMBER', 3),
    ]
