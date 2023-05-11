import llvmlite.ir as ir
import llvmlite.binding as llvm

class Codegen:
    def __init__(self):
        self.module = ir.Module()
        self.builder = ir.IRBuilder()
        self.variables = {}

    def generate_code(self, commands):
        for command in commands:
            if command['type'] == 'declaration':
                self.handle_declaration(command)
            elif command['type'] == 'assignment':
                self.handle_assignment(command)

    def handle_declaration(self, command):
        var_type = ir.IntType(32) if command['value_type'] == 'INTEGER' else ir.FloatType()
        self.variables[command['name']] = self.builder.alloca(var_type, name=command['name'])

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
            self.builder.store(value, self.variables[command['name']])

def compile_to_llvm(commands):
    codegen = Codegen()
    codegen.generate_code(commands)
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly(str(codegen.module))
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine
