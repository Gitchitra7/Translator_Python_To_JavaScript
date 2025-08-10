from lexer import TokenType
from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current = self.tokens[self.pos]

    def eat(self, token_type):
        if self.current.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current = self.tokens[self.pos]
        else:
            raise SyntaxError(f"Expected {token_type}, got {self.current.type}")

    def parse(self):
        statements = []
        while self.current.type != TokenType.EOF:
            while self.current.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            if self.current.type != TokenType.EOF:
                statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        while self.current.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)

        if self.current.type == TokenType.DEF:
            return self.parse_function()
        elif self.current.type == TokenType.RETURN:
            return self.parse_return()
        elif self.current.type == TokenType.IF:
            return self.parse_if()
        elif self.current.type == TokenType.WHILE:
            return self.parse_while()
        elif self.current.type == TokenType.PRINT:
            self.eat(TokenType.PRINT)
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return Print(expr)
        elif self.current.type == TokenType.IDENTIFIER:
            name = self.current.value
            self.eat(TokenType.IDENTIFIER)
            if self.current.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current.type != TokenType.RPAREN:
                    args.append(self.parse_expression())
                self.eat(TokenType.RPAREN)
                return FunctionCall(name, args)
            else:
                self.eat(TokenType.EQUALS)
                expr = self.parse_expression()
                return Assignment(Variable(name), expr)
        else:
            raise SyntaxError(f"Invalid statement: {self.current.type}")

    def parse_if(self):
        self.eat(TokenType.IF)
        condition = self.parse_expression()
        self.eat(TokenType.COLON)
        body = self.parse_block()
        orelse = []
        if self.current.type == TokenType.ELSE:
            self.eat(TokenType.ELSE)
            self.eat(TokenType.COLON)
            orelse = self.parse_block()
        return If(condition, body, orelse)

    def parse_while(self):
        self.eat(TokenType.WHILE)
        condition = self.parse_expression()
        self.eat(TokenType.COLON)
        body = self.parse_block()
        return While(condition, body)

    def parse_function(self):
        self.eat(TokenType.DEF)
        name = self.current.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.LPAREN)
        params = []
        if self.current.type == TokenType.IDENTIFIER:
            params.append(self.current.value)
            self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.COLON)
        body = self.parse_block()
        return Function(name, params, body)

    def parse_return(self):
        self.eat(TokenType.RETURN)
        expr = self.parse_expression()
        return Return(expr)

    def parse_block(self):
        statements = []
        while self.current.type not in (TokenType.EOF, TokenType.DEF, TokenType.ELSE):
            while self.current.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            if self.current.type in (TokenType.EOF, TokenType.DEF, TokenType.ELSE):
                break
            statements.append(self.parse_statement())
        return statements

    def parse_expression(self):
        left = self.parse_factor()
        while self.current.type in (
            TokenType.PLUS, TokenType.MINUS,
            TokenType.MULTIPLY, TokenType.DIVIDE,
            TokenType.EQEQ, TokenType.NOTEQ,
            TokenType.LTE, TokenType.GTE,
            TokenType.GREATER, TokenType.LESS
        ):
            op = self.current.value
            self.eat(self.current.type)
            right = self.parse_factor()
            left = BinaryOp(left, op, right)
        return left

    def parse_factor(self):
        if self.current.type == TokenType.NUMBER:
            val = self.current.value
            self.eat(TokenType.NUMBER)
            return Number(val)
        elif self.current.type == TokenType.STRING:
            val = self.current.value
            self.eat(TokenType.STRING)
            return String(val)
        elif self.current.type == TokenType.IDENTIFIER:
            name = self.current.value
            self.eat(TokenType.IDENTIFIER)
            if self.current.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current.type != TokenType.RPAREN:
                    args.append(self.parse_expression())
                self.eat(TokenType.RPAREN)
                return FunctionCall(name, args)
            return Variable(name)
        else:
            raise SyntaxError("Invalid factor")
