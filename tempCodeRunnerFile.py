import tkinter as tk
from tkinter import filedialog, messagebox
import os
from lexer import Lexer
from parser import Parser
from codegen_js import JSCodeGenerator

class CompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python to JavaScript Compiler")
        tk.Label(root, text="Enter Python Code:").pack()
        self.input_text = tk.Text(root, height=15, width=80)
        self.input_text.pack()
        tk.Button(root, text="Compile to JavaScript", command=self.compile_code).pack(pady=10)

        tk.Label(root, text="Generated JavaScript Code:").pack()
        self.output_text = tk.Text(root, height=15, width=80)
        self.output_text.pack()
        tk.Button(root, text="Save JS Output", command=self.save_output).pack(pady=10)

    def compile_code(self):
        try:
            source_code = self.input_text.get("1.0", tk.END).strip()
            if not source_code:
                messagebox.showwarning("Input Missing", "Please enter Python code to compile.")
                return

            lexer = Lexer(source_code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            codegen = JSCodeGenerator()
            if isinstance(ast, list):
                for node in ast:
                    codegen.generate(node)
            else:
                codegen.generate(ast)
            js_code = "\n".join(codegen.code)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, js_code)
        except Exception as e:
            messagebox.showerror("Compilation Error", str(e))

    def save_output(self):
        js_code = self.output_text.get("1.0", tk.END).strip()
        if not js_code:
            messagebox.showwarning("No Output", "Nothing to save. Compile first.")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".js", filetypes=[("JavaScript Files", "*.js")])
        if filepath:
            with open(filepath, "w") as f:
                f.write(js_code)
            messagebox.showinfo("Saved", f"JavaScript code saved to {filepath}")

if __name__ == '__main__':
    root = tk.Tk()
    app = CompilerGUI(root)
    root.mainloop()