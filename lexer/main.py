import re

TOKEN_COMMAND_KEYWORDS = [
    (r"hero|mage|knight|rogue|druid|oracle|bard|shaman|monk", "VARIABLE"),
    (r"gained a bonus of|increased their strength by", "ADD_VALUE"),
    (r"united with|combined their might with", "ADD_VARIABLE"),
    (r"An enchantment of|A potion of strength", "ADD_NUMBERS"),
]

TOKEN_VARIABLES = [
    (r"called\s+([_a-zA-Z][_a-zA-Z0-9]*)", "VARIABLE_NAME"),
    (r"sword|axe|club|dagger|mace", "INTEGER"),
    (r"bow|sling|dart|crossbow", "FLOAT"),
    (r"sang|composed|whispered|inscribed|penned", "STRING"),
    (r"forged|carved|mixed|brewed|crafted", "ASSIGN"),
    (r"swore|named|invoked|followed", "BOOL_ASSIGN"),
    (r"truth|falsehood", "BOOL_VALUE"),
    (r"[-+]?[0-9]*\.[0-9]+", "FLOAT_NUMBER"),
    (r"[-+]?[0-9]+", "INTEGER_NUMBER"),
    (r".*", "COMMENT"),
]

TOKENS_STAGE2 = [
    (r"gained a bonus of", "ADD"),
    (r"increased their strength by", "ADD"),
    (r"united with", "ADD"),
    (r"combined their might with", "ADD"),
    (r"An enchantment of", "ADD"),
    (r"A potion of strength", "ADD"),
]

def identify_command(line):
    command_tokens = []

    match = None
    for token_regex, token_type in TOKEN_COMMAND_KEYWORDS:
        regex = re.compile(token_regex)
        match = regex.search(line)
        if match:
            value = match.group(0)
            new_token = (value, token_type)
            command_tokens.append(new_token)
            if token_type == "VARIABLE":
                command_tokens.append(lex_variable(line, command_tokens))

    return command_tokens

def lex_variable(line, tokens):
    regex = re.compile(TOKEN_VARIABLES[0][0])
    match = regex.search(line)
    if match:
        var_name = match.group(0).replace("called ", "")
        tokens.append((var_name, 'VARIABLE_NAME'))
    else:
        raise SyntaxError(("Missing called keyword after starting a variable definition with a hero"))
    
    token_regex, token_type = TOKEN_VARIABLES[1]
    regex = re.compile(token_regex)
    match = regex.search(line)
    if match:
        value = match.group(0)
        token = (value, token_type)
        tokens.append(token)

    token_regex, token_type = TOKEN_VARIABLES[4]
    regex = re.compile(token_regex)
    match = regex.search(line)
    if match:
        value = match.group(0)
        token = (value, token_type)
        tokens.append(token)

    token_regex, token_type = TOKEN_VARIABLES[8]
    regex = re.compile(token_regex)
    match = regex.search(line)
    if match:
        value = match.group(0)
        token = (value, token_type)
        tokens.append(token)

    return tokens

def lexer(code):
    lines = [line for line in code.split('\n') if line.strip() != '']
    all_tokens = []
    for line in lines:
        command = identify_command(line.strip())
        all_tokens.append(command)
    all_tokens = [token for token in all_tokens if token]
    return all_tokens