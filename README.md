# DnD++ - Dungeon and Dragons inspired Programming Language

Welcome to my first experiment building my own programming language which is showcased on my YouTube Channel ILTPWC.

DnD++ is a Dungeons & Dragons-inspired programming language designed for those who want to bring some excitement and creativity to their coding adventures. 
This project provides a lexer, parser, interpreter, and compiler for the DnD++ programming language, as well as example code to demonstrate its syntax and usage.

And please don't take it to serious!


## Language Overview

The DnD++ programming language uses a syntax inspired by Dungeons & Dragons adventures, with a focus on storytelling and imaginative descriptions. Variable declarations, for example, are written as follows:

`In the realm of Variables, a legendary hero was born called christian. The hero wields a mighty Sword, forged with the power of 10`

This declaration is equivalent to the following code in C++:

`int christian = 10;`

## Getting Started

To start using the DnD++ programming language, clone this repository and install the required dependencies:

`git clone https://github.com/your-username/dndpp.git`

Once you have the repository cloned, follow the instructions in the subsequent sections to tokenize, parse, interpret, and compile DnD++ code.

This project includes a lexer, parser, interpreter, and compiler for the DnD++ programming language. You can find their implementations in their subfolders lexer, parser, compiler, interpreter, respectively.

To tokenize, parse, interpret, or compile DnD++ code, follow these steps:

1. Write your DnD++ code in a text file, e.g., example.dndpp.
2. Use the main.py example.dndpp to generate a .asm file
3. Assembe the .asm file with NASM and link the object file with GCC after that generate the executable

`nasm -f elf64 example.asm -o example.o`
`gcc example.o -o example`
`./example`


And the most important think have fun! and try to play the adventure with your DnD Party.


### Lexer

ToDo: Add Content


### Parser

ToDo: Add Content


### Interpreter

ToDo: Add Content


### Compiler

ToDo: Add Content


## Examples

The following example demonstrates how to declare and initialize a variable in the DnD++ programming language:

`In the realm of Variables, a legendary hero was born called healthPoints. The hero wields a mighty Sword, forged with the power of 100`


## Contributing

We welcome contributions from the community! If you have any ideas, suggestions, or improvements for the DnD++ programming language, please feel free to submit an issue or pull request.

## Support

If you want to support me please consider to like the YouTube Video about the DnD++ Language and subscribe to my Channel ILTPWC(http://www.youtube.com/@ILTPWC)

