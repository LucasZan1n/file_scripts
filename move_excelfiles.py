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

downloads = "C:\\Users\\duits\\Downloads\\"
dest_dir = "C:\\Users\\duits\\Downloads\\excel_files\\"
file_type = ".xlsx"

check_files(downloads)

excel_f = []

if __name__ == "__main__":
	for file in f[0]:
		if str(file).endswith(filetype):
			excel_f.append(file)
		else:
			continue

	for excelfile in excel_f:
		move_file((downloads + excelfile), (dest_dir + excelfile))