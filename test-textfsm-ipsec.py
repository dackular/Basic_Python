import textfsm
# Load the input file to a variable
input_file_ipsec = open("ipsec-log.log", encoding='utf-8')
raw_text_data_ipsec = input_file_ipsec.read()
input_file_ipsec.close()
print(input_file_ipsec)


# Run the text through the FSM. 
# The argument 'template_ipsec' is a file handle and 'raw_text_data_ipsec' is a 
# string with the content from the show_inventory.txt file
template_ipsec = open("ipsec-textfsm.textfsm")
re_table_ipsec = textfsm.TextFSM(template_ipsec)
fsm_results_ipsec = re_table_ipsec.ParseText(raw_text_data_ipsec)

# the results are written to a CSV file
outfile_name = open("outfile-ipsec-csv.csv", "w+")
outfile = outfile_name

# Display result as CSV and write it to the output file
# First the column headers...
print(re_table_ipsec.header)
for s in re_table_ipsec.header:
    outfile.write("%s;" % s)
outfile.write("\n")

# ...now all row's which were parsed by TextFSM
counter = 0
for row in fsm_results_ipsec:
    print(row)
    for s in row:
        outfile.write("%s;" % s)
    outfile.write("\n")
    counter += 1
print("Write %d records" % counter)


