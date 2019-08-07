import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('/Users/shen/Downloads/homework-6-rantheway-master/USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)

def most_pop(dict):
    return_dict = {'views': 0, 'channel': None}
    
    for k, v in dict.items():
        if int(v) > return_dict['views']:
            return_dict['channel'] = k
            return_dict['views'] = int(v)
    return return_dict

def least_pop(dict):
    return_dict = {'views': float('inf'), 'channel': None }
    for k, v in dict.items():
        if k == 'Unspecified':
            continue
        if int(v) < return_dict['views']:
            return_dict['channel'] = k
            return_dict['views'] = int(v)
    return return_dict
        

def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': None,
                                              'least_pop_num_views': None}
    aggregate_channel = {}
    for item in data[1:]:
        aggregate_channel.setdefault(item['channel_title'], 0)
        aggregate_channel[item['channel_title']] += int(item['views'])
        
    most_popular_channel = most_pop(aggregate_channel)
    least_popular_channel = least_pop(aggregate_channel)
    most_popular_and_least_popular_channel['most_popular_channel'] = most_popular_channel['channel']
    most_popular_and_least_popular_channel['least_popular_channel'] = least_popular_channel['channel']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_popular_channel['views']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_popular_channel['views']
    return most_popular_and_least_popular_channel

def most_liked(dict):
    return_dict = {'likes': 0, 'channel': None}
    
    for k, v in dict.items():
        if int(v) > return_dict['likes']:
            return_dict['channel'] = k
            return_dict['likes'] = int(v)
    return return_dict

def most_disliked(dict):
    return_dict = {'dislikes': 0, 'channel': None}
    
    for k, v in dict.items():
        if int(v) > return_dict['dislikes']:
            return_dict['channel'] = k
            return_dict['dislikes'] = int(v)
    return return_dict

def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}
    aggregate_channel_most_liked = {}
    aggregate_channel_most_disliked = {}
    for item in data[1:]:
        aggregate_channel_most_liked.setdefault(item['channel_title'], 0)
        aggregate_channel_most_disliked.setdefault(item['channel_title'], 0)
        aggregate_channel_most_liked[item['channel_title']] += int(item['likes'])
        aggregate_channel_most_disliked[item['channel_title']] += int(item['dislikes'])
        
    most_liked_channel = most_liked(aggregate_channel_most_liked)
    most_disliked_channel = most_disliked(aggregate_channel_most_disliked)
    most_liked_and_disliked_channel['most_liked_channel'] = most_liked_channel['channel']
    most_liked_and_disliked_channel['most_disliked_channel'] = most_disliked_channel['channel']
    most_liked_and_disliked_channel['num_likes'] = most_liked_channel['likes']
    most_liked_and_disliked_channel['num_dislikes'] = most_disliked_channel['dislikes']
    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    #print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))
