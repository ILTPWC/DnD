class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        commands = []
        while self.pos < len(self.tokens):
            command = self.parse_command()
            commands.append(command)
            self.pos += 1
        return commands

    def parse_command(self):
        if self.pos >= len(self.tokens):
            return None 

        command = {}
        token_type = (self.tokens[self.pos][0])[1]

        if token_type == "VARIABLE":
            command["type"] = "declaration"
            command["value_type"] = (self.tokens[0][2])[1]
            command["name"] = (self.tokens[0][1])[0]
            command["value"] = (self.tokens[0][4])[0]
        elif token_type in ["ADD_VALUE", "ADD_VARIABLE", "ADD_NUMBERS"]:
            command["type"] = "assignment"
            command["name"] = self.parse_variable_name()
            command["value"] = self.parse_value()
        else:
            self.pos += 1
        return command

    def parse_variable_name(self):
        if self.tokens[self.pos][1] != "VARIABLE_NAME":
            raise SyntaxError("Expected a variable name")
        return self.tokens[self.pos][0]

    def parse_value(self):
        token_type = self.tokens[self.pos][1]
        if token_type in ["INTEGER_NUMBER", "FLOAT_NUMBER", "STRING", "BOOL_VALUE"]:
            return self.tokens[self.pos][0]
        elif token_type == "VARIABLE_NAME":
            return {"type": "variable", "name": self.tokens[self.pos][0]}
        else:
            raise SyntaxError("Expected a value")

def parse(tokens):
    parser = Parser(tokens)
    return parser.parse()
