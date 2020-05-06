import os
from os import walk

def move_file(file_path, file_dest):
	os.rename(file_path, file_dest)

f = []
dp = []
dn = []

def check_files(directory):
	#Fill in path to directory
	for (dirpath, dirnames, filenames) in walk(directory):
		f.append(filenames)
		dp.append(dirpath)
		dn.append(dirnames)

downloads = "C:\\Users\\User\\Downloads\\"
dest_dir = "C:\\Users\\User\\Downloads\\excel_files\\"

check_files(downloads)

excel_f = []

for file in f[0]:
	if str(file).endswith(".xlsx"):
		excel_f.append(file)
	else:
		continue

for excelfile in excel_f:
	move_file((downloads + excelfile), (dest_dir + excelfile))