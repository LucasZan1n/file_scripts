import os
from os import walk
from move_excelfiles import check_files

f = []

downloads = "C:\\Users\\duits\\Downloads\\"
dest_folder = downloads + "exe_files\\"

for (dirpath, dirnames, filenames) in walk(downloads):
	f.append(filenames)

exe_files = []

for file in f[0]:
	if str(file).endswith(".exe"):
		exe_files.append(file)

for exe_file in exe_files:
	os.rename((downloads + exe_file), (dest_folder + exe_file))