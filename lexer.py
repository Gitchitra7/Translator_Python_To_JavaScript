import re
from tokens import TokenType

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        token_specification = [
            (TokenType.DEF, r'\bdef\b'),
            (TokenType.RETURN, r'\breturn\b'),
            (TokenType.IF, r'\bif\b'),
            (TokenType.ELSE, r'\belse\b'),
            (TokenType.WHILE, r'\bwhile\b'),
            (TokenType.PRINT, r'\bprint\b'),

            (TokenType.EQEQ, r'=='),
            (TokenType.NOTEQ, r'!='),
            (TokenType.LTE, r'<='),
            (TokenType.GTE, r'>='),

            (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
            (TokenType.NUMBER, r'\d+'),
            (TokenType.STRING, r'\".*?\"|\'.*?\''),

            (TokenType.EQUALS, r'='),
            (TokenType.PLUS, r'\+'),
            (TokenType.MINUS, r'-'),
            (TokenType.MULTIPLY, r'\*'),
            (TokenType.DIVIDE, r'/'),
            (TokenType.GREATER, r'>'),
            (TokenType.LESS, r'<'),

            (TokenType.LPAREN, r'\('),
            (TokenType.RPAREN, r'\)'),
            (TokenType.COLON, r':'),
            (TokenType.NEWLINE, r'\n'),
        ]

        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

        for match in re.finditer(token_regex, self.source_code):
            kind = match.lastgroup
            value = match.group()
            if kind == TokenType.NUMBER:
                value = int(value)
            self.tokens.append(Token(kind, value))

        self.tokens.append(Token(TokenType.EOF, None))
        return self.tokens