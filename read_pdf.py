import tabula
from os import path, remove
import re


def extract_info(tiliote):
    tapahtumat_list = list()
    nested_list = list()
    if path.exists("sptili.csv") == False:
        tabula.convert_into("stili.pdf", "sptili.csv", output_format="csv", pages='all')

    
    with open("sptili.csv", "r") as f:
        read_file = f.read()
        
        tapahtumat_object = re.compile(r'\d*,(\d{4})(.*),,\d+,,"(\d*\.?\d*\.?\d{1,3},\d{2}[+-])"')#read only line with amount
        matches = tapahtumat_object.finditer(read_file)
        for match in matches:
            print("function", match)
            # tapahtumat_list.append(match)
            for group_index in range(1,len(match.groups())+1):
                nested_list.append(match.group(group_index))
            tapahtumat_list.append(nested_list)
            nested_list = list()
        # remove("accounts/bank_statements/{date}_{user}_tili.csv")
    for i in tapahtumat_list:
        print(i[0][:2])
extract_info("stili.pdf")