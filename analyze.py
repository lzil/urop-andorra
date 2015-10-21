import csv


with open('data/tweet.csv', 'rb') as csvfile:
	tweets = csv.DictReader(csvfile, dialect='excel')
	i = 0
	langs = {}
	hrs = {}
	src = {}
	words = []
	f = open('locs.txt', 'w')
	g = open('words.txt', 'w')
	for row in tweets:
		words += row['text'].split()
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
	wds = ['que', 'en', 'lo', 'por', 'a', 'le', 'pero', 'y', 'de', 'eu', 'si', 'yo', 'esta', 'un', 'una', 'es', 'tu', 'la', 'el', 'del', 'los', 'al', 'com', 'como', 'e', 'ir', 'em', 'todo', 'ya', 'ver', 'nos', 'ja', 'va', 'ser', 'les', 'et', 'mi', 'con', 'da', 'sei', 'no', 'se', 'um', 'ha', 'to', 'para', 'je', 'eres', 'asi', 'mis', 'so', 'algo', 'is', 'na']
	for i in words:
		if i.lower() not in wds and len(i) != 1:
			g.write(i + ' ')
	f.close()
	g.close()