#!/usr/bin/env python3.8
import csv
import re,sys

def plane_data():
	airline_name = re.compile(r"American")
	with open("/Users/vinayak.bhatt/Downloads/Airplane_Crashes_and_Fatalities_Since_1908.csv") as fhand:
		freader = csv.DictReader(fhand)
		#next(freader)
		#all_data = []
		#count = 0
		d = {}
		#lst = []
		for var in freader:
			#print(var["Date"])
			if var.get(var["Fatalities"]) != "" and var.get(var["Date"]) != "" :
				date_plane = (var["Date"].split("/")[2])
				if d.get(date_plane) == None:
					d[date_plane] = var["Fatalities"]+":"+var["Date"]+", "
				else:
					d[date_plane] += var["Fatalities"]+" : "+var["Date"]+", "
				#print(f"checking for {date_plane}")
				#lsd.append([date_plane][])
					#d[date_plane] = d[date_plane].append(var["Fatalities"],var["Date"])
			#if (re.search(airline_name, var["Operator"])):

					#print(date_plane, var["Fatalities"])
					#count += 1
				#print(var["Fatalities"], var["Date"], var["Operator"])
					#print(var)

		print(d)
	#deaths.sort(reverse=True)

		#print(var)

	#print(int(var["Time"].split(":")[0]))
if __name__ == "__main__":
	plane_data()
