#collect submissions that contain target stock sticker using Psaw(a 3rd-party wrapper for searching reddit via the Pushshift API which maintains a copy of reddit objects)

import praw
from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

#logging into Reddit API with account registered for project purpose
reddit = praw.Reddit(client_id='y1TQB6oXy3deCw' , 
                     client_secret='71tO5JhHKOxu0_0gfMzxnG4XKcFmlA' ,
                     username='Born-Pass494', 
                     password='pythonproject', 
                     user_agent='Born-Pass494One')

api = PushshiftAPI()

start_time=int(dt.datetime(2020, 1, 1).timestamp())
end_time=int(dt.datetime(2021, 1, 1).timestamp())
target_stocks=['run','penn','sedg','sam','qdel','halo','cree','gnrc','sail','iivi',\
              'nvax','vxrt','gnpx','veri','celh','plug','codx','nls','grwg','awh',\
              'aapl','msft','nke','crm','dis','cat','hd','wmt','hon','unh']


for item in range(len(target_stocks)):
    sub_data=target_stocks[item]+'_sub.csv'
    comm_data=target_stocks[item]+'_comm.csv'
    test2_sub=api.search_submissions(q="{}".format(target_stocks[item]), after=start_time, before=end_time,\
                                     subreddit='wallstreetbets',\
                                     filter=['author', 'id', 'num_comments', 'score', 'title', 'selftext']) #selected attributes to minimise file size
    df = pd.DataFrame(test2_sub)
#removing submissions with zero comments
    df == 0
    df = df[~(df==0).any(axis=1)]
    df.to_csv(sub_data, index=False)
##collect comments using Praw (the original Python wrapper for the Reddit API)
#create a list submission ids from the submission file to retrieve corresponding comments
    id_list=df["id"].tolist()
    result=list()
    for item in range(len(id_list)):
        submission = reddit.submission(id="{}".format(id_list[item]))
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            data={'link_id': [comment.link_id], 'comm_score': [comment.score], 'comm_body': [comment.body], 'comm_time': [comment.created_utc]}
            result.append(data)
    frame=pd.DataFrame(result)
    frame.to_csv(comm_data, index=False)          
