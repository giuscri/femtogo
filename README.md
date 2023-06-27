# femtogo

A toy project of an interpreter for a crazy small (_femto_) subset of the Go language.

## Usage

```
$ pip3 install -e .
$ echo '''
a := 42
Println(a)
''' > /tmp/test.fgo
$ femtogo -f /tmp/test.fgo
```

## Most complex program

```go
a := 42

var b
b = a + 2

Println(b)
```

## Grammar

```
<program> ::= <statement_list>

<statement_list> ::= <statement> <statement_list> | <statement>

<statement> ::= <assignment_statement> | <declaration_statement> | <print_statement>

<assignment_statement> ::= <identifier> := <expression> | <identifier> = <expression>

<declaration_statement> ::= "var" <identifier>

<print_statement> ::= "Println" "(" <expression> ")"

<expression> ::= <identifier> | <literal> | <binary_expression>

<binary_expression> ::= <expression> <operator> <expression>

<operator> ::= "+" | "-" | "*" | "/"

<identifier> ::= <letter> <identifier_tail>

<identifier_tail> ::= <letter> | <digit> | "_"

<literal> ::= <number>

<number> ::= <digit> <number_tail>

<number_tail> ::= <digit> <number_tail> | <epsilon>

<letter> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

<epsilon> ::= ""
```
