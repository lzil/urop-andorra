import csv


with open('tweet.csv', 'rb') as csvfile:
	tweets = csv.DictReader(csvfile, dialect='excel')
	i = 0
	langs = {}
	hrs = {}
	for row in tweets:
		if i > 30:
			#break
			pass
		i += 1
		if row['lang'] in langs:
			langs[row['lang']] += 1
		else:
			langs[row['lang']] = 1
		hr = row['time'].split(' ')[1].split(':')[0]
		if hr in hrs:
			hrs[hr] += 1
		else:
			hrs[hr] = 1
	for lang, num in langs.iteritems():
		print lang + ': ' + str(num)
	print '*****HOURS*****'
	for i in range(24):
		if i < 10:
			i = '0' + str(i)
		i = str(i)
		print i + ': ' + str(hrs[i])