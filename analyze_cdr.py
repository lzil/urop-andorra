import csv
import matplotlib.pyplot as plt


DATA_FILE = "data/CDR GROUP/cdrSample.csv"

def open_file(filename):
	return open(filename, "r")

def close_file(f):
	return f.close()

def setup_csv_reader(csvf):
	return csv.DictReader(csvf)

def analyze_cdr(csv_reader):
	cdr_data = { }
	hours_dict = { }

	for count, row in enumerate(csv_reader):
		hr = row['intime'].split()[1].split(':')[0]
		if hr in hours_dict:
			hours_dict[hr] += 1
		else:
			hours_dict[hr] = 1

	cdr_data['hours'] = hours_dict
		
	return cdr_data

def hours_to_list(hours_dict):
	hourList = []
	for hour, num in hours_dict.iteritems():
		hourList.append([hour, num])
	hourList = sorted(hourList, key=lambda x: x[0])
	sm = 0
	for i in hourList:
		sm += i[1]
	for i in range(len(hourList)):
		hourList[i][1] *= 1.0 / sm
	return hourList

def langs_to_list(lang_dict):
	langList = []
	for lang, num in lang_dict.iteritems():
		langList.append((lang, num))
	langList = sorted(langList, key=lambda x: x[1])
	return langList
	



cdr_csv = open_file(DATA_FILE)
csv_reader = setup_csv_reader(cdr_csv)

cdr_data = analyze_cdr(csv_reader)
hours = hours_to_list(cdr_data['hours'])
for i in hours:
	print str(i[0]) + ': ' + str(i[1])


close_file(cdr_csv)
