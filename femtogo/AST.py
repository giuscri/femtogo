from dataclasses import dataclass
from typing import List, Union

@dataclass
class Program:
    statements: 'StatementList'

@dataclass
class StatementList:
    statements: List[Union['AssignmentStatement', 'DeclarationStatement', 'PrintStatement']]

    def __getitem__(self, i):
        return self.statements[i]

@dataclass
class AssignmentStatement:
    identifier: 'Identifier'
    expression: Union['Identifier', 'Literal', 'BinaryExpression']

@dataclass
class DeclarationStatement:
    identifier: 'Identifier'

@dataclass
class PrintStatement:
    expression: Union['Identifier', 'Literal', 'BinaryExpression']

@dataclass
class BinaryExpression:
    left_expression: Union['Identifier', 'Literal']
    operator: 'Operator'
    right_expression: Union['Identifier', 'Literal']

@dataclass
class Identifier:
    name: str

@dataclass
class Literal:
    value: int  # or float if you have floating point numbers

@dataclass
class Operator:
    op: str
