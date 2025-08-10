from lexer import Lexer
from parser import Parser
from codegen_js import generate_code
from ast_nodes import Module

with open("test1.py", "r") as f:
    source = f.read()

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
ast = parser.parse()
tree = Module(ast)

js_code = generate_code(tree)

with open("result.js", "w") as f:
    f.write(js_code)

print(" JavaScript code successfully generated in output/result.js")
