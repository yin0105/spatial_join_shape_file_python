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
        result_dict = {}
        for row in csv_file:
            # if row['H'] == '1' and row['B'] == '14': print("ok")
            ok = False
            if row['H'] in result_dict:
                if row['B'] in result_dict[row['H']]:
                    result_dict[row['H']][row['B']]['aantalpa'] = str(float(result_dict[row['H']][row['B']]['aantalpa']) + float(row['aantalpa']))
                    result_dict[row['H']][row['B']]['aantalov'] = str(float(result_dict[row['H']][row['B']]['aantalov']) + float(row['aantalov']))
                    result_dict[row['H']][row['B']]['aantalfts'] = str(float(result_dict[row['H']][row['B']]['aantalfts']) + float(row['aantalfts']))
                    if row['tijd'] < result_dict[row['H']][row['B']]['tijd']: result_dict[row['H']][row['B']]['tijd'] = row['tijd']
                    ok = True
            
            if not ok:
                if not row['H'] in result_dict:
                    result_dict[row['H']] = {}
                if not row['B'] in result_dict[row['H']]:
                    result_dict[row['H']][row['B']] = {}
                result_dict[row['H']][row['B']]['tijd'] = row['tijd']
                result_dict[row['H']][row['B']]['H'] = row['H']
                result_dict[row['H']][row['B']]['B'] = row['B']
                result_dict[row['H']][row['B']]['aantalpa'] = row['aantalpa']
                result_dict[row['H']][row['B']]['aantalov'] = row['aantalov']
                result_dict[row['H']][row['B']]['aantalfts'] = row['aantalfts']
            
        for aa in result_dict:
            for bb in result_dict[aa]:
                writer.writerow([result_dict[aa][bb]['tijd'], aa, bb, result_dict[aa][bb]['aantalpa'], result_dict[aa][bb]['aantalov'], result_dict[aa][bb]['aantalfts']])
        
        in_file.close()
        out_file.close()