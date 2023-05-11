import sys
from lexer.main import lexer
from parser.main import Parser
from interpreter.main import Interpreter
from compiler.main import compile_to_llvm

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_file>")
        return

    source_file = sys.argv[1]
    with open(source_file, "r") as f:
        code = f.read()

    tokens = lexer(code)

    print("Token:")
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    ast = parser.parse()

    print("\nAST:")
    print(ast)

    interpreter = Interpreter()
    interpreter.interpret(ast)

    compile_to_llvm(ast)

    asm_file = source_file.replace(".dndpp", ".asm")
    with open(asm_file, "w") as f:
        f.write(assembly_code)

    print(f"Generated x86 Assembly Code saved to {asm_file}")

if __name__ == "__main__":
    main()
