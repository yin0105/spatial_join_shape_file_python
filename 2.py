import csv
with open('shape_files/HBMatrix2019.csv', 'r') as in_file:
    with open('HBMatrix.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["tijd", "H", "B", "aantalpa", "aantalov", "aantalfts"])

        csv_file = csv.DictReader(in_file)
        min_tijd = 10
        pre_h = -1
        pre_b = -1
        aantalpa_sum = aantalov_sum = aantalfts_sum = 0
        for row in csv_file:
            if row['H'] != pre_h or row['B'] != pre_b:
                if pre_h != -1:
                    writer.writerow([min_tijd, pre_h, pre_b, aantalpa_sum, aantalov_sum, aantalfts_sum])
                    aantalpa_sum = aantalov_sum = aantalfts_sum = 0
                    min_tijd = 10
                aantalpa_sum += float(row['aantalpa'])
                aantalov_sum += float(row['aantalov'])
                aantalfts_sum += float(row['aantalfts'])
                if int(row['tijd']) < min_tijd : min_tijd = int(row['tijd'])
                pre_h = row['H']
                pre_b = row['B']
            # print(dict(row))