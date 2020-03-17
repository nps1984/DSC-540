from itertools import zip_longest


# Create function
def return_line_dict(header, line):
    # So we ensure our line has the same number of fields as our header,
    # we use zip_longest
    zipped_line = zip_longest(header, line, fillvalue=None)
    line_dict = {kv[0]: kv[1] for kv in zipped_line}
    return line_dict


# Open file
with open("sales_record.csv", 'r') as fd:
    # Read first line and save it
    first_line = fd.readline()

    # Remove newline, and split on comma, saving to a header list
    header = first_line.replace("\n", "").split(",")

    # Loop through rest of file
    for i, line in enumerate(fd):
        # Remove newlines and split on comma
        line = line.replace("\n", "").split(",")

        # pass header and current line to function
        d = return_line_dict(header, line)

        # print the sales, break after the 10th record
        print(f'{i+1}: {d}')
