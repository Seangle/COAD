#define the memory size
MEMORY_WORD_SIZE = 16
#file containing binary for BISC
BINARY_FILE = "output.txt"
#VHDL file containing the memory
MEMORY_FILE = "memory.vhd"
#starts replacing anything after this string
BEGIN_REPLACE = "--MEMORY_LOADER_START"
#stops replacing once this string is found
END_REPLACE = "--MEMORY_LOADER_END"

#read the file containing the binary output
text_file = open(BINARY_FILE)
lines = text_file.readlines()
text_file.close()

#line counter
line_number = 1
#begin replace line counter
br_line_number = 0
#end replace line counter
er_line_number = 0

#create a resulting list
parsed_lines = list()

#parse the BINARY_FILE
for x in lines:
	x = "".join(x.split())
	#check each line.
	if len(x) != MEMORY_WORD_SIZE:
		#incorrect amount of bits
		print ("ERROR: line", "{:03d}".format(line_number) , "does not contain 16 bits and will not fit in the memory register.")
	else:
		#line passed parser
		print("Line","{:03d}".format(line_number), ":", x, " passed all parsing checks.")
		#prep line for file
		x = "\"" + x + "\",\n"
		parsed_lines.append(x)
	#increment the line counter
	line_number = line_number + 1
print()

#might have to change the name to the final name when the time comes
vhdl_file = open(MEMORY_FILE)
edit_vhdl = vhdl_file.readlines()
vhdl_file.close()

#reset line counter
line_number = 1

#find lines to replace
print("Finding starting and ending points")
for x in edit_vhdl:
	if BEGIN_REPLACE in x:
		print("Found start at line", "{:03d}".format(line_number),"(keyword:", x[:-1], ")")
		br_line_number= line_number -1
	if END_REPLACE in x:
		print("Found  end  at line", "{:03d}".format(line_number), "(keyword:", x[:-1], ")")
		er_line_number = line_number -1
	line_number = line_number + 1
print()

#replace lines
if er_line_number < br_line_number or er_line_number == br_line_number:
	print("ERROR: start and end replace points are in the wrong order, or on the same line.")
else:
	print("Replacing the contents between the start and end points")
	#replace the contents between the lines
	del edit_vhdl[br_line_number+1: er_line_number]
	edit_vhdl[br_line_number+1:br_line_number+1] = parsed_lines
	#overwrite file
	vhdl_file = open(MEMORY_FILE, 'w')
	vhdl_file.writelines(edit_vhdl)
	vhdl_file.close()
	#replaced successfully
	print(MEMORY_FILE, "successfully updated")
