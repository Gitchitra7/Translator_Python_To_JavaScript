class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

class BinaryOp(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Assignment(ASTNode):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

class Print(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class Function(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class Return(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class String(ASTNode):
    def __init__(self, value):
        self.value = value

class Module(ASTNode):
    def __init__(self, body):
        self.body = body

class If(ASTNode):
    def __init__(self, condition, body, orelse):
        self.condition = condition
        self.body = body
        self.orelse = orelse

class While(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body