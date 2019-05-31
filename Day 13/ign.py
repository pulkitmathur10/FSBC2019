# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('ign.csv')



xbox_filter = (df["score"] > 7) & (df["platform"] == "Xbox One")
freviews = df[xbox_filter]
games_xbox = freviews['title']
print (games_xbox)
xbox_one = df['platform']=="Xbox One"
xbox_one_df = df[xbox_one]
xbox_reviews = xbox_one_df['score_phrase']
xbox_reviews.hist(bins=20,grid=False,xrot=90)


ps4 = df['platform']=="PlayStation 4"
ps4_df = df[ps4]
ps4_reviews = ps4_df['score_phrase']
ps4_reviews.hist(bins=20,grid=False,xrot=90)


