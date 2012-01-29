import os, sys, csv


def write_lists_csv(block_list,file_name, headers):
    """
    Takes a list or list of lists, a files location//name, and a list of headers
    Writes the itemsof the lists as rows in a CSV file.  Each item of the list is a comma-separated value.
    Returns the location of the CSV file.
    """
    fileWriter = csv.writer(open(file_name, 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow(headers)
    for each in block_list:
        fileWriter.writerow(each)