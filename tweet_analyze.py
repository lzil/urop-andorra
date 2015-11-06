#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv, math, re

DATA_FILE = "data/new_twitter_data.csv"
LOCATION_COORDS = {
	'Soldeu':	(42.577608,1.6643343),
	'Canillo':	(42.5665274,1.5977744),
	'Encamp':	(42.5343602,1.5762906),
	'La Massana': (42.5434345,1.5100397),
	'El Pas de la Casa': (42.542445,1.7303751),
	'Andorra la Vella': (42.5050848,1.5116108)
}
LANG = 'es'
common = {
	'fr': set(['a', 'mais', 'je', 'la', 'en', 'de', 'suis', 'il', 'est', 'un', 'me', 'et', 'ça', 'le', 'no', 'se']),
	'es': set(['rt', 'gracias', 'este', 'quiero', 'pero', 'como', 'me', 'esta', 'sin', 'su', 'eres', 'hay', 'mi', 'todo', 'yo', 'muy', 'al', 'fin', 'nos', 'ya', 'a', 'por', 'para', 'es', 'en', 'el', 'la', 'las', 'los', 'lo', 'y', 'une', 'de', 'un', 'una', 'con', 'si', 'le', 'hoy', 'no', 'que', 'se', 'del', 'le', 'tu', 'te', 'mas'])
}

def open_file(filename):
	return open(filename, "r")

def close_file(f):
	return f.close()

def setup_csv_reader(csvf):
	return csv.DictReader(csvf)

def distance(x1, y1, x2, y2):
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + 0.0)

def tweet_locations(csv_reader):
	city_counts = {
		'Soldeu':	[], 
		'Canillo':	[],
		'Encamp':	[],
		'La Massana': [],
		'El Pas de la Casa': [],
		'Andorra la Vella': []
	}
	for count, row in enumerate(csv_reader):
		if row['latitude'] != '' and row['longitude'] != '' and row['lang'] == 'fr':
			mnc = ''
			mnn = float('inf')
			for i in LOCATION_COORDS:
				dst = distance(LOCATION_COORDS[i][0], LOCATION_COORDS[i][1], float(row['latitude']), float(row['longitude']))
				if dst < mnn:
					mnn = dst
					mnc = i
			city_counts[mnc].append(row['text'])
	return city_counts

def tweet_dates(csv_reader):
	months = {
		'Jan': [],
		'Feb': [],
		'Mar': [],
		'Apr': [],
		'May': [],
		'Jun': [],
		'Jul': [],
		'Aug': [],
		'Sep': [],
		'Oct': [],
		'Nov': [],
		'Dec': []
	}
	for count, row in enumerate(csv_reader):
		time = row['created_at']
		if row['lang'] == LANG:
			months[time.split()[1]].append(row['text'])
	return months

def topics(texts):
	d = {}
	for text in texts:
		words = text.split()
		for i in words:
			if i.isalpha() and len(i) > 1 and i.lower() not in common[LANG]:
				if i in d:
					d[i] += 1
				else: d[i] = 1

	ordered = [(k, d.get(k)) for k in sorted(d, key=d.get, reverse=True)]
	return ordered

def main():

	tweets_csv = open_file(DATA_FILE)
	csv_reader = setup_csv_reader(tweets_csv)

	#tweets_data = tweet_locations(csv_reader)
	'''
	for i in tweets_data:
		
		print i
		#print topics(tweets_data[i])
		for j in tweets_data[i]:
			print j
		print '\n'
	'''
	months = tweet_dates(csv_reader)
	for i in months:
		print i
		print topics(months[i])[:100]

	close_file(tweets_csv)

if __name__ == '__main__':
	main()
