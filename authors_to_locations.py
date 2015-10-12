import csv
import matplotlib.pyplot as plt


DATA_FILE = "data/tweet.csv"

def open_file(filename):
	return open(filename, "r")

def close_file(f):
	return f.close()

def setup_csv_reader(csvf):
	return csv.DictReader(csvf)

def analyze_tweets(csv_reader):
	#list of locations
	tweets_data = { }
	author_location_dict = { }
	languages_dict = { }
	hours_dict = { }

	for count, row in enumerate(csv_reader):
		if (count % 250) == 0:
			print count
		author_id = row["author"]
		time      = row["time"]
		lat       = row["lat"]
		lng       = row["lng"]
		if author_location_dict.get(author_id) is None:
			author_location_dict[author_id] = (((lat, lng), time))
		else:
			current_list = list(author_location_dict[author_id])
			current_list.append(((lat,lng), time))
			current_list = tuple(current_list)
			author_location_dict[author_id] = current_list

		if row['lang'] in languages_dict:
			languages_dict[row['lang']] += 1
		else:
			languages_dict[row['lang']] = 1
		hr = row['time'].split(' ')[1].split(':')[0]
		if hr in hours_dict:
			hours_dict[hr] += 1
		else:
			hours_dict[hr] = 1

	tweets_data['author_locations'] = author_location_dict
	tweets_data['languages'] = languages_dict
	tweets_data['hours'] = hours_dict
		
	return tweets_data

def hours_to_list(hours_dict):
	hourList = []
	for hour, num in hours_dict.iteritems():
		hourList.append((hour, num))
	hourList = sorted(hourList, key=lambda x: x[0])
	return hourList

def langs_to_list(lang_dict):
	langList = []
	for lang, num in lang_dict.iteritems():
		langList.append((lang, num))
	langList = sorted(langList, key=lambda x: x[1])
	return langList
	



tweets_csv = open_file(DATA_FILE)
csv_reader = setup_csv_reader(tweets_csv)

tweets_data = analyze_tweets(csv_reader)
print hours_to_list(tweets_data['hours'])
print langs_to_list(tweets_data['languages'])


close_file(tweets_csv)
