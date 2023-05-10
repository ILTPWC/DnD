class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children if children else []

    def __str__(self):
        return f"{self.node_type}({self.value})"

    def __repr__(self):
        return self.__str__()

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        return self.parse_declaration()

    def parse_declaration(self):
        realm = self.expect("REALM")
        hero = self.expect("HERO")
        hero_name = self.expect("HERO_NAME")
        integer_sword = self.expect("INTEGER_SWORD")
        power = self.expect("POWER")
        number = self.expect("NUMBER")

        variable_name = hero_name.value.split()[-1]
        variable_value = int(number.value)

        return ASTNode("VariableDeclaration",
            value={"name": variable_name, "value": variable_value})

    def expect(self, token_type):
        if self.index >= len(self.tokens):
            raise ValueError("Unexpected end of input")

        token = self.tokens[self.index]
        if token.token_type != token_type:
            raise ValueError(f"Unexpected token: {token}, expected {token_type}")

        self.index += 1
        return token