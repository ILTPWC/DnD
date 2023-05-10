import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f"{self.token_type}({self.value})"

    def __repr__(self):
        return self.__str__()

REALM = "REALM"
HERO = "HERO"
HERO_NAME = "HERO_NAME"
INTEGER_SWORD = "INTEGER_SWORD"
POWER = "POWER"
NUMBER = "NUMBER"
COMMENT = "COMMENT"

token_patterns = [
    (r"In the realm of\s+[_a-zA-Z][_a-zA-Z0-9]*\s*,", REALM),
    (r"a\s+[_a-zA-Z][_a-zA-Z0-9]*\s+hero", HERO),
    (r"was born called\s+[_a-zA-Z][_a-zA-Z0-9]*\s*[.]?", HERO_NAME),
    (r"The hero wields a mighty Sword\s*[,:]?", INTEGER_SWORD),
    (r"forged with the power of\s+", POWER),
    (r"[-+]?[0-9]+", NUMBER),
    (r".*?(?=\n|$)", COMMENT), 
]

def lexer(code):
    tokens = []

    while code:
        code = code.lstrip()
        matched = False
        for pattern, token_type in token_patterns:
            match = re.match(pattern, code)
            if match:
                matched = True
                token_value = match.group(0)
                if token_type != COMMENT:
                    tokens.append(Token(token_type, token_value))
                code = code[len(token_value):]
                break

        if not matched:
            raise ValueError(f"Unexpected character: {code[0]}")

    return tokens