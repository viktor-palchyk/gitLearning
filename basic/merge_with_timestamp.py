# -*- coding: utf-8 -*-
import os
import datetime

filename = datetime.datetime.now()

def merge_with_timestamp(directory):
	variable = ""
	path = os.getcwd()
	for el in os.listdir(str(path)+"/"+ directory):
		if ".txt" in el:
			file = open(str(path)+"/"+directory+"/"+el, 'r')
			contents = file.read()
			variable += contents + "\n"
	with open("merged_file_"+filename.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
		file.write(variable)
	print("Success!")
	print(variable)

merge_with_timestamp("Sample-Files")
