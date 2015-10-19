import csv


with open('data/hashtags_count.csv', 'rb') as csvfile:
	tags = csv.DictReader(csvfile, dialect=csv.excel_tab)
	counts = []
	for row in tags:
		print row
		counts.append(row['num'], row['hashtag'])
	counts.sort()
	for i in range(15):
		print counts[i][1] + ': ' + counts[i][0]
	f.close()