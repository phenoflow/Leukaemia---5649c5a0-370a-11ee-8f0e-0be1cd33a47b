# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"B640000","system":"readv2"},{"code":"B654.00","system":"readv2"},{"code":"B65y100","system":"readv2"},{"code":"B660.00","system":"readv2"},{"code":"B662.00","system":"readv2"},{"code":"B663.00","system":"readv2"},{"code":"B670.00","system":"readv2"},{"code":"B674.00","system":"readv2"},{"code":"B675.00","system":"readv2"},{"code":"B680.00","system":"readv2"},{"code":"B682.00","system":"readv2"},{"code":"B690.00","system":"readv2"},{"code":"B692.00","system":"readv2"},{"code":"BBr0200","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leukaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["leukaemia-msubacute---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["leukaemia-msubacute---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["leukaemia-msubacute---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
