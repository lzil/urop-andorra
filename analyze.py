import csv


with open('data/tweet.csv', 'rb') as csvfile:
	tweets = csv.DictReader(csvfile, dialect='excel')
	i = 0
	langs = {}
	hrs = {}
	src = {}
	f = open('locs.txt', 'w')
	for row in tweets:
		if row['lat'] != '':
			f.write('[' + str(row['lat']) + ','+str(row['lng'])+'],')
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
		if row['source'] in src:
			src[row['source']] += 1
		else:
			src[row['source']] = 1
	print '*****LANGUAGES*****'
	langList = []
	sm = 0
	for lang, num in langs.iteritems():
		langList.append((lang, num))
		sm += num
	langList = sorted(langList, key=lambda x: x[1])
	for i in langList:
		print i[0] + ': ' + str(i[1])
	print '*****HOURS*****'
	hourList = []
	for hour, num in hrs.iteritems():
		hourList.append((hour, num))
	hourList = sorted(hourList, key=lambda x: x[0])
	for i in hourList:
		print i[0] + ': ' + str(i[1])

	print '*****Sources*****'
	sourceList = []
	for source, num in src.iteritems():
		sourceList.append((source, num))
	sourceList = sorted(sourceList, key=lambda x: x[1])
	for i in sourceList:
		print i[0] + ': ' + str(i[1])
	f.close()