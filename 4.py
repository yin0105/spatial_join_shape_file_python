import csv
with open('areanr_PC4.csv', 'r') as in_file_1:
    areanr_dict = {}
    tmp_dict = {}
    csv_file = csv.DictReader(in_file_1)
    for row in csv_file:
        areanr_dict[row['Areanr']] = row['PC4']
    # print(dict(areanr_dict))
    result_dict = {}
    with open('HBmatrixTotal.csv', 'r') as in_file_2:
        with open('HBmatrixTotalPC4.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(["tijd", "H", "B", "aantalpa", "aantalov", "aantalfts", "total"])

            csv_file = csv.DictReader(in_file_2)
            for row in csv_file:
                if row['H'] in areanr_dict or row['B'] in areanr_dict:
                    ok = False
                    if areanr_dict[row['H']] in result_dict:
                        if areanr_dict[row['B']] in result_dict[areanr_dict[row['H']]]:
                            result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalpa'] = str(float(result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalpa']) + float(row['aantalpa']))
                            result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalov'] = str(float(result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalov']) + float(row['aantalov']))
                            result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalfts'] = str(float(result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalfts']) + float(row['aantalfts']))
                            result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['total'] = str(float(result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['total']) + float(row['total']))
                            if row['tijd'] < result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['tijd']: result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['tijd'] = row['tijd']
                            ok = True
                    
                    if not ok:
                        if not areanr_dict[row['H']] in result_dict:
                            result_dict[areanr_dict[row['H']]] = {}
                        if not areanr_dict[row['B']] in result_dict[areanr_dict[row['H']]]:
                            result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]] = {}
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['tijd'] = row['tijd']
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['H'] = areanr_dict[row['H']]
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['B'] = areanr_dict[row['B']]
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalpa'] = row['aantalpa']
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalov'] = row['aantalov']
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['aantalfts'] = row['aantalfts']
                        result_dict[areanr_dict[row['H']]][areanr_dict[row['B']]]['total'] = row['total']


                    # writer.writerow([row['tijd'], areanr_dict[row['H']], areanr_dict[row['B']], row['aantalpa'], row['aantalov'], row['aantalfts'], row['total']])
                else:
                    if not row['H'] in areanr_dict: tmp_dict[row['H']] = ""
                    if not row['B'] in areanr_dict: tmp_dict[row['B']] = ""

            for aa in result_dict:
                for bb in result_dict[aa]:
                    writer.writerow([result_dict[aa][bb]['tijd'], aa, bb, result_dict[aa][bb]['aantalpa'], result_dict[aa][bb]['aantalov'], result_dict[aa][bb]['aantalfts'], result_dict[aa][bb]['total']])
            
            in_file_1.close()
            in_file_2.close()
            out_file.close()
            print(dict(tmp_dict))
            
            for kk in tmp_dict.keys():
                print(kk + " ")