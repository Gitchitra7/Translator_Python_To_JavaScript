## Python to JavaScript Translator with GUI
A lightweight, modular compiler that translates a subset of Python code into clean, readable JavaScript.
Built from scratch in Python, featuring lexical analysis, parsing, AST construction, and code generation — all wrapped in a user-friendly Tkinter GUI.

## Features
1.Complete pipeline: Tokenizes Python source, parses it into an Abstract Syntax Tree (AST), and generates equivalent JavaScript code.
2.Supported syntax: Functions, variables, expressions, control flow (if, else, while), print statements, and basic operators.
3.Robust error handling: Meaningful syntax error messages during parsing to help diagnose issues.
4.Interactive GUI: Intuitive Tkinter interface to write Python code, compile instantly, view JavaScript output, and save results.
5.Extensible architecture: Clean separation between lexer, parser, AST nodes, and code generator for easy future expansion.

## Why This Project?
This project is a practical demonstration of:
1.Compiler design fundamentals — lexical analysis, parsing, AST generation, and code emission.
2.Bridging programming languages — translating Python semantics to JavaScript syntax.
3.GUI integration — combining system-level language processing with a graphical frontend.
4.Learning through building — ideal for students and enthusiasts diving into language tooling and transpilers.

## Project Structure
/lexer.py         # Tokenizer that breaks Python code into tokens
/parser.py        # Parser that builds the AST from tokens
/ast_nodes.py     # Classes defining nodes in the AST
/codegen_js.py    # Generates JavaScript code from the AST
/gui.py           # Tkinter-based GUI for code input and output
/README.md        # This documentation file

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests to improve the lexer, parser, code generator, or GUI.

## Contact
Chitra Pandey
B.Tech Computer Science — 4th Year
Email: chitrapandey688@gmail.com
GitHub: Gitchitra7
