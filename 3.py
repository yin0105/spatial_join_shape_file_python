import csv
with open('HBMatrix.csv', 'r') as in_file:
    with open('HBmatrixTotal.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["tijd", "H", "B", "aantalpa", "aantalov", "aantalfts", "total"])

        csv_file = csv.DictReader(in_file)
        for row in csv_file:
            sum = float(row['aantalpa']) + float(row['aantalov']) + float(row['aantalfts'])
            writer.writerow([row['tijd'], row['H'], row['B'], row['aantalpa'], row['aantalov'], row['aantalov'], sum])