# COAD
## Computer Organization and Design
Just a place to post the code I wrote for this class. Stage 3 of the design was finished, which had us implement stage 2 into actual working code. In the given timeframe, we managed to get it to execute single instructions correctly, but ran into trouble getting the program counter to work, along with a jump instruction. Stage 2 of design was the implimentation of the data path. Phase 1 consisted of coming up with the assembly language and a few other details, like the name of the microprocessor design. The name is BISC, or Basic Instruction Set Computer. The assemby code goes by the same name.

### What you can find in this repository:
- C code to x86 Assembly (to help learn MIPS Assembly)
- ~VHDL for the microprocessor~ Not included due to the fact that future students could use it.
- Memory Loader (for group project)
- Final Design Description

### Writing C code and seeing how it looks in x86 Assembly
- swap.c & swap.S - A simple swap function  
Viewing what happens when GCC turns C into x86 Assembly, and commenting on what it does.
Mostly to help learn MIPS Assembly. It's similar enough and allows me to compare C code to Assembly.

### Memory Loader
- loader.py  
loader.py is a simple script used to automate the process of recieving a binary file and loading it into BISC's memory. This task is done by modifying the actual VHDL file that contains the memory unit.

### Small Description of the Final Design
The microprocessor had 8 16-bit registers, with the 0th register being a constant 0 value.
It was capable of executing 13 instrucions (with varying degrees of accuracy due to the control unit implementation). There was one 16-bit Arithmatic Logic Unit (ALU), one Control Unit (which also consisted of many smaller parts), one register file, one main memory, and a few multiplexors to hold everything together. It was a large project to undertake, and my peers and I learned a lot from it. If I had to do it again, I would make sure to have the control signals working correctly, as that lead to a large number of complications in implementing the microprocessor in phase 3.
