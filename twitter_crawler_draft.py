import tweepy



def api_setup(consumer_key,consumer_secret,access_key,access_secret):
	"""function to set up api"""
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_key,access_secret)
	return tweepy.API(auth)

def get_usernames(filename):
	"""opens id file. Make sure that first line of id file is empty
	filename paramter is a string with the file's extension"""
	id_file=open(filename,"r")
	ids=id_file.readlines()[1:]
	ids=[(unicode(i).encode("utf-8")).replace("\n","") for i in ids]
	return ids

def data_extractor(api,usernames, count_total,total_tweet_number,file_to_write,classifier,feature_extractor):
	"""parameters:
	api: api to use
	usernames: list of usernames
	count_total: number of tweets to pull at once from a timeline
	total_tweet_number: total number of tweets to pull from a user
	file to write: the file object to write
	classifier: classifier to use
	feature_extractor: feature_extractor to use
	"""
	for username in usernames:
		#initialize the id of the last tweet looked at and the number of tweets of a user that has been pulled so far
		tweet_count=0
		cursor=tweepy.Cursor(api.user_timeline,screen_name=username).items()
		#while the tweet_count is less than the aimed number, stay in this while loop
		while tweet_count<total_tweet_number:
			#try-except block to catch errors (e.g. rate limit)
			try:
				print username
				status=cursor.next()
				print status.user.screen_name
				if len(status.text.split())>=3:
					(result,last_id)=status_processor(status,classifier,feature_extractor)
					tweet_count+=1
					#end extracting information and write it to file
					file_to_write.write(result)
					file_to_write.write("\n")
				print tweet_count
			#catch error
			except tweepy.error.TweepError as error:
				print error
				if type(error[0])==list:
					if type(error[0][0])==dict:
						if error[0][0]["code"]==88:
							print "entering sleep"
							print tweet_count
							time.sleep(960)
							print "exiting sleep"
							continue
				break
			except StopIteration:
				break

def status_processor(status, classifier, feature_extractor):
	"""processes a given status (a JSON object that contains the data to be extracted)
	paramaters:
	-status: JSON file pulled from twitter
	-classifier: a specified classifier used for categorization
	-feature extractor: necessary for the classifier to function properly"""
	screen_name=unicoder(status.user.screen_name)
	screen_name=screen_name.replace(","," ")
	name=unicoder(status.user.name)
	name=name.replace(","," ")
	join_date=unicoder(str(status.user.created_at))
	friends_count=unicoder(str(status.user.friends_count))
	followers_count=unicoder(str(status.user.followers_count))
	statuses_count=unicoder(str(status.user.statuses_count))
	location=unicoder(status.user.location).replace(","," ")
	location=location.strip()
	if location=="":
		location=unicoder("None")
	tweet=unicode(status.text).encode("utf-8")
	tweet=tweet.replace(",","")
	tweet=tweet.replace('\n',"")
	tweet=re.sub(re.compile(r"\s+")," ", tweet)
	print tweet
	tweet_id=unicoder(status.id_str)
	last_id=int(tweet_id)
	lang=unicoder(status.lang)
	if status.geo==None:
		geo=unicoder("No geo available")
	else:
		geo=unicoder(str(status.geo["coordinates"]).replace(",","/"))
	created_at=status.created_at
	created_at_str=unicoder(str(created_at))
	weekday=weekdays[created_at.weekday()]
	for key in times_of_day.keys():
		if created_at.hour in key:
			time_of_day=times_of_day[key]
	media=unicoder("False")
	try:
		if len(status.entities["media"])>0:
			media=unicoder("True")
	except KeyError:
		media=unicoder("False")
	reply_to=unicoder("False")
	if status.in_reply_to_status_id!=None:
		reply_to=unicoder("True")
	is_retweet="False"
	if re.match("RT\s@[^\s]", tweet):
		is_retweet=unicoder("True")
	retweet_count=unicoder(str(status.retweet_count))
	hashtag_count=unicoder(str(len(status.entities["hashtags"])))
	url_count=unicoder(str(len(status.entities["urls"])))
	mention_count=unicoder(str(len(status.entities["user_mentions"])))
	source=unicoder(status.source_url)
	return (screen_name+","+name+","+join_date+","+friends_count+","+followers_count+","+statuses_count+","+location+","+tweet+","+tweet_id+","+lang+","+category+","+geo+","+created_at_str+","+weekday+","+time_of_day+","+media+","+reply_to+","+is_retweet+","+retweet_count+","+hashtag_count+","+url_count+","+mention_count+","+source,last_id)
