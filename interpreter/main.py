class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def interpret(self):
        self.eval(self.ast)

    def eval(self, node):
        if node.node_type == "VariableDeclaration":
            self.eval_variable_declaration(node)

    def eval_variable_declaration(self, node):
        name = node.value["name"]
        value = node.value["value"]
        self.symbol_table[name] = value
        print(f"Variable {name} has been assigned the value {value}")