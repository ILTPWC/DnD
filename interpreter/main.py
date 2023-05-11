class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, commands):
        for command in commands:
            if command['type'] == 'declaration':
                self.handle_declaration(command)
            elif command['type'] == 'assignment':
                self.handle_assignment(command)
            else:
                raise SyntaxError("Unknown command type: " + command['type'])

    def handle_declaration(self, command):
        if command['value_type'] == 'INTEGER':
            self.variables[command['name']] = 0
        elif command['value_type'] == 'FLOAT':
            self.variables[command['name']] = 0.0
        elif command['value_type'] == 'STRING':
            self.variables[command['name']] = ""
        elif command['value_type'] == 'BOOL_VALUE':
            self.variables[command['name']] = False
        else:
            raise SyntaxError("Unknown variable type: " + command['value_type'])

    def handle_assignment(self, command):
        if command['name'] not in self.variables:
            raise SyntaxError("Undefined variable: " + command['name'])
        else:
            value = command['value']
            if isinstance(value, dict) and value['type'] == 'variable':
                if value['name'] not in self.variables:
                    raise SyntaxError("Undefined variable: " + value['name'])
                else:
                    value = self.variables[value['name']]
            self.variables[command['name']] += value

def interpret(commands):
    interpreter = Interpreter()
    interpreter.interpret(commands)
    return interpreter.variables
