import sys, argparse                    # Handle Command Line Arguments
import csv                              # Manipulate .csv files
from pybtex.database import parse_file  # Parses BibTeX files


# Input validation
if len(sys.argv) != 3:
    print('\n**** ERROR: Missing command line argument. Please see correct usage. ****\n')
    print('\n**** Usage Instructions: $ python myBibTexParser.py -infile=<name of your .bib file> -outfile=<name of your .csv file>\n')
    raise ValueError('Missing Command Line Arguement(s)')

# Initialize Command Line Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('-inFile', required=True)
parser.add_argument('-outFile', required=True)
args = parser.parse_args()

# Create/Open output csv file using UTF-32 (in order to encode all languages)
output = open(args.outFile, 'w', encoding='UTF-32')

# Create writer to write to csv file
writer = csv.writer(output)

# Create header row
header = ['id', 'title', 'subject_lang', 'year']
writer.writerow(header)

# Open BibTeX file using UTF-8
with open(args.inFile, 'r', encoding='UTF-8') as bibtex_file:
    print('**** Initialized File Parsing. May take up to 2 minutes... ****')

    # Parse file using pybtex module
    bib_database = parse_file(bibtex_file)
    print('**** File Parsed ****')

    # Parse Data for each entry
    for id in bib_database.entries:

        # Mark as a null value if field is not found.
        nullValue = 'Null'

        try: 
            title = bib_database.entries[id].fields['title']
        except: 
            title = nullValue
        
        try:
            lgcode = bib_database.entries[id].fields['lgcode']
        except: 
            lgcode = nullValue
            
        try: 
            year = bib_database.entries[id].fields['year']
        except: 
            year = nullValue
            

        # Write row to csv file
        row = [id, title, lgcode, year]
        writer.writerow(row)
    
    print('**** CSV File Successfully Created! ****')

# Close output file
output.close()
