import csv
import jsonlines
import json
import pandas as pd
from tabulate import tabulate

def get_data_from_excel():
    xls = pd.read_excel('WEO_Data.xls')
    data = xls.to_dict(orient='records')
    return data

def write_json_lines(data):
    with open('G7Economics.JSONL', 'wb') as f:
        writer = jsonlines.Writer(f)
        for line in data:
            line = {"text": line}
            writer.write(line)

def main():
    raw_data = get_data_from_excel()
    # print(data)
    dataToJSONL = []
    for line in raw_data:
        line = str(line).strip("{}").replace("'", "")
        dataToJSONL.append(line)
    write_json_lines(dataToJSONL)
    print("jsonL written..")

if __name__ == "__main__":
    main() 