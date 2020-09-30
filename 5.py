import csv
with open('shape_files/Centroids_PC4.csv', 'r') as in_file_1:
    pc4_dict = {}
    tmp_dict = {}
    csv_file = csv.DictReader(in_file_1)
    for row in csv_file:
        pc4_dict[row['PC4']] = {"x":row['X'], "y":row['Y']}
    # print(dict(pc4_dict))
    with open('HBmatrixTotalPC4.csv', 'r') as in_file_2:
        with open('HBmatrixTotalPC4Centroids.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(["tijd", "H", "H_X_coordinate", "H_Y_coordinate", "B", "B_X_coordinate", "B_Y_coordinate", "aantalpa", "aantalov", "aantalfts", "total"])

            csv_file = csv.DictReader(in_file_2)
            for row in csv_file:
                if row['H'] in pc4_dict and row['B'] in pc4_dict:
                    writer.writerow([row['tijd'], row['H'], pc4_dict[row['H']]['x'], pc4_dict[row['H']]['y'], row['B'], pc4_dict[row['B']]['x'], pc4_dict[row['B']]['y'], row['aantalpa'], row['aantalov'], row['aantalfts'], row['total']])
                else:
                    if not row['H'] in pc4_dict: tmp_dict[row['H']] = ""
                    if not row['B'] in pc4_dict: tmp_dict[row['B']] = ""

            print(dict(tmp_dict))
            
            for kk in tmp_dict.keys():
                print(kk + " ")