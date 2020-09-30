import csv
with open('areanr_PC4.csv', 'r') as in_file_1:
    areanr_dict = {}
    tmp_dict = {}
    csv_file = csv.DictReader(in_file_1)
    for row in csv_file:
        areanr_dict[row['Areanr']] = row['PC4']
    # print(dict(areanr_dict))
    with open('HBmatrixTotal.csv', 'r') as in_file_2:
        with open('HBmatrixTotalPC4.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(["tijd", "H", "B", "aantalpa", "aantalov", "aantalfts", "total"])

            csv_file = csv.DictReader(in_file_2)
            for row in csv_file:
                if row['H'] in areanr_dict and row['B'] in areanr_dict:
                    writer.writerow([row['tijd'], areanr_dict[row['H']], areanr_dict[row['B']], row['aantalpa'], row['aantalov'], row['aantalfts'], row['total']])
                else:
                    if not row['H'] in areanr_dict: tmp_dict[row['H']] = ""
                    if not row['B'] in areanr_dict: tmp_dict[row['B']] = ""

            print(dict(tmp_dict))
            
            for kk in tmp_dict.keys():
                print(kk + " ")