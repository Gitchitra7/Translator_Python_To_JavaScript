from ast_nodes import *

class JSCodeGenerator:
    def __init__(self):
        self.code = []
        self.indent_level = 0
        self.declared_vars = set()
    def indent(self):
        return "    " * self.indent_level 
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        codegen = JSCodeGenerator()
        js_code = codegen.generate(ast)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, js_code)
    def emit(self, line):
        self.code.append(self.indent() + line)
    def generate(self, node):
        method_name = f'gen_{type(node).__name__}'
        method = getattr(self, method_name, self.generic_gen)
        return method(node)
    def generic_gen(self, node):
        raise Exception(f"No generate method for {type(node).__name__}")
    def gen_Module(self, node):
        for stmt in node.body:
            self.generate(stmt)
        return "\n".join(self.code)
    def gen_Function(self, node):
        args = ", ".join(node.params)
        self.emit(f"function {node.name}({args}) {{")
        self.indent_level += 1
        old_code = self.code
        self.code = []
        for stmt in node.body:
            self.generate(stmt)
        func_body = self.code
        self.code = old_code
        for line in func_body:
            self.emit(line)
        self.indent_level -= 1
        self.emit("}")
    def gen_Return(self, node):
        value = self.generate(node.expression)
        self.emit(f"return {value};")
    def gen_FunctionCall(self, node):
        args = ", ".join(self.generate(arg) for arg in node.args)
        return f"{node.name}({args})"
    def gen_String(self, node):
        return repr(node.value)
    def gen_Assignment(self, node):
        target = self.generate(node.variable)
        value = self.generate(node.expression)
        if target not in self.declared_vars:
            self.emit(f"let {target} = {value};")
            self.declared_vars.add(target)
        else:
            self.emit(f"{target} = {value};")
    def gen_Variable(self, node):
        return node.name
    def gen_BinaryOp(self, node):
        left = self.generate(node.left)
        right = self.generate(node.right)
        return f"{left} {node.operator} {right}"
    def gen_Number(self, node):
        return str(node.value)
    def gen_Print(self, node):
        value = self.generate(node.expression)
        self.emit(f"console.log({value});")
    def gen_If(self, node):
        test = self.generate(node.condition)
        self.emit(f"if ({test}) {{")
        self.indent_level += 1
        for stmt in node.body:
            self.generate(stmt)
        self.indent_level -= 1
        self.emit("}")
        if node.orelse:
            self.emit("else {")
            self.indent_level += 1
            for stmt in node.orelse:
                self.generate(stmt)
            self.indent_level -= 1
            self.emit("}")
    def gen_While(self, node):
        test = self.generate(node.condition)
        self.emit(f"while ({test}) {{")
        self.indent_level += 1
        for stmt in node.body:
            self.generate(stmt)
        self.indent_level -= 1
        self.emit("}")
def generate_code(ast_root):
    generator = JSCodeGenerator()
    return generator.generate(ast_root)
