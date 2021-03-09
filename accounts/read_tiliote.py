# import tabula
# from os import path
# import re

# # Read pdf into a list of DataFrame
# # dfs = tabula.read_pdf("tili.pdf", pages='all')

# # Read remote pdf into a list of DataFrame
# # dfs2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# # convert PDF into CSV
# if path.exists("output_tili.csv"):
#     print("file already uploaded")
# else:
#     tabula.convert_into("tili.pdf", "output_tili.csv", output_format="csv", pages='all')

# # convert all PDFs in a directory
# # tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')

# with open("output_tili.csv", "r") as f:
#     read_file = f.read()
#     # tapahtumat_list = re.compile(r'(\d{2}\.\d{4}\.\d{4}\.\d{2})(.*?)(\d*,\d{2}[+-])')
#     tapahtumat_object = re.compile(r'(\d{2}\.\d{2}\s\d{2}\.\d{2})(.*?)(,,,,,+)"(\d*\.?\d*\.?\d{1,3},\d{2}[+-])"')#read only line with amount
#     matches = tapahtumat_object.finditer(read_file)
#     tapahtumat_list = list()
#     nested_list = list()
#     for match in matches:
#         for group_index in range(1,len(match.groups())+1):
#             nested_list.append(match.group(group_index))
#         tapahtumat_list.append(nested_list)
#         nested_list = list()
#     for i in tapahtumat_list:
#         print(i)



import tabula
from os import path, remove
import re


# convert PDF into CSV
def extract_info(tiliote, user, date):
    tapahtumat_list = list()
    nested_list = list()
    tabula.convert_into(tiliote, f"accounts/bank_statements/{date}_{user}_tili.csv", output_format="csv", pages='all')

    
    with open(f"accounts/bank_statements/{date}_{user}_tili.csv", "r") as f:
        read_file = f.read()
        tapahtumat_object = re.compile(r'(\d{2}\.\d{2}\s\d{2}\.\d{2})(.*?)(,,,,,+)"(\d*\.?\d*\.?\d{1,3},\d{2}[+-])"')#read only line with amount
        matches = tapahtumat_object.finditer(read_file)
        for match in matches:
            print("function", match)
            # tapahtumat_list.append(match)
            for group_index in range(1,len(match.groups())+1):
                nested_list.append(match.group(group_index))
            tapahtumat_list.append(nested_list)
            nested_list = list()
        # remove("accounts/bank_statements/{date}_{user}_tili.csv")
    return tapahtumat_list









