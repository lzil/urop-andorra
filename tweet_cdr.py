import analyze_tweets
import analyze_cdr

tweets_hours = analyze_tweets.main()
cdr_hours = analyze_cdr.main()
print tweets_hours
print cdr_hours

for i in range(24):
	print str(tweets_hours[i][0]) + ': ' + str(tweets_hours[i][1] - cdr_hours[i][1])