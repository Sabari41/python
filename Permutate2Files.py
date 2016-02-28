#!/usr/bin/python

f1 = "C:\\Users\\Saba\\Downloads\\Gap Scan\\UPC_70_30.dat"
f2 = "C:\\Users\\Saba\\Downloads\\Gap Scan\\Date.dat"
f3 = "C:\\Users\\Saba\\Downloads\\Gap Scan\\UPC_Exclusions.csv"
#UPCs = open(f1,"r")
#UPC = UPC1.readLines()
#Dates = open(f2,"r")
#Date = Date1.readLines()
with open(f3,"w") as outfile:
	for UPC in open(f1,"r").readlines():
		for Date in open(f2,"r").readlines():
			UPC1 = UPC.strip()
			Date1 = Date.strip()
			outfile.write('"'+UPC1+'","'+Date1+'"\n')
