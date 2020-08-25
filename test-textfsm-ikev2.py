import textfsm
# Load the input file to a variable
input_file_ikev2 = open("ikev2-test.log", encoding='utf-8')
raw_text_data_ikev2 = input_file_ikev2.read()
input_file_ikev2.close()
print(input_file_ikev2)


# Run the text through the FSM. 
# The argument 'template_ikev2' is a file handle and 'raw_text_data_ikev2' is a 
# string with the content from the show_inventory.txt file
template_ikev2 = open("ikev2-textfsm.textfsm")
re_table_ikev2 = textfsm.TextFSM(template_ikev2)
fsm_results_ikev2 = re_table_ikev2.ParseText(raw_text_data_ikev2)

# the results are written to a CSV file
outfile_name = open("outfile-ikev2-csv.csv", "w+")
outfile = outfile_name

# Display result as CSV and write it to the output file
# First the column headers...
print(re_table_ikev2.header)
for s in re_table_ikev2.header:
    outfile.write("%s;" % s)
outfile.write("\n")

# ...now all row's which were parsed by TextFSM
counter = 0
for row in fsm_results_ikev2:
    print(row)
    for s in row:
        outfile.write("%s;" % s)
    outfile.write("\n")
    counter += 1
print("Write %d records" % counter)


