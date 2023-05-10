class Compiler:
    def __init__(self, ast):
        self.ast = ast
        self.assembly_code = []

    def compile(self):
        self.emit("; Generated x86 assembly code")
        self.emit("section .data")
        self.emit("section .text")
        self.emit("global _start")
        self.emit("_start:")
        self.emit("    ; Write variable declarations")
        self.compile_node(self.ast)
        self.emit("    ; Exit system call")
        self.emit("    mov eax, 1")
        self.emit("    xor ebx, ebx")
        self.emit("    int 0x80")
        return "\n".join(self.assembly_code)

    def compile_node(self, node):
        if node.node_type == "VariableDeclaration":
            self.compile_variable_declaration(node)

    def compile_variable_declaration(self, node):
        name = node.value["name"]
        value = node.value["value"]
        self.emit(f"    ; Declare variable {name} with value {value}")
        self.emit(f"    mov dword [{name}], {value}")

    def emit(self, code):
        self.assembly_code.append(code)
