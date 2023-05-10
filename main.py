import sys
from lexer.main import lexer
#from parser import Parser
#from interpreter import Interpreter
#from compiler import Compiler

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_file>")
        return

    source_file = sys.argv[1]
    with open(source_file, "r") as f:
        code = f.read()

    tokens = lexer(code)
    print("Tokens:")
    for token in tokens:
        print(token)

    #parser = Parser(tokens)
    #ast = parser.parse()
    #print("\nAST:")
    #print(ast)

    #interpreter = Interpreter(ast)
    #interpreter.interpret()
    #print("\nSymbol Table:")
    #print(interpreter.symbol_table)

    #compiler = Compiler(ast)
    #assembly_code = compiler.compile()
    #print("\nGenerated x86 Assembly Code:")
    #print(assembly_code)

if __name__ == "__main__":
    main()
