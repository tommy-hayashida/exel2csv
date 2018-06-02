#! python3

import openpyxl
import csv
import sys

def main():
    rfile = sys.stdin # ファイル名入力
    wb = openpyxl.load_workbook(rfile) # ファイルを開く
    sheetList = wb.get_sheet_names()
    sheet = sheetList[0]
    
    wfile = 'shotaikyaku.csv'
    with open(wfile, 'w', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for cols in sheet.rows:
                writer.writerow([str(col.value or '') for col in cols])

if __name__ == '__main__':
    main()
