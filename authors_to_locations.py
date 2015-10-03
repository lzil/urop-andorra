import csv
import matplotlib.pyplot as plt


DATA_FILE = "data/tweets.csv"

def open_file(filename):
    return open(filename, "r")

def close_file(f):
    return f.close()

def setup_csv_reader(csvf):
    return csv.DictReader(csvf)

def get_author_locations(csv_reader):
    author_location_dict = { }
    count = 0
    for row in csv_reader:
        count += 1
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
    return author_location_dict

tweets_csv = open_file(DATA_FILE)
csv_reader = setup_csv_reader(tweets_csv)

print get_author_locations(csv_reader)

close_file(tweets_csv)
