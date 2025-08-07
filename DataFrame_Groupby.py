# -*- coding: utf-8 -*-
__author__ = 'Obadero_Samuel'

import pandas as pd
import numpy as np
def to_numeric(s):
    try:
        return pd.to_numeric(s,errors='raise')
    except ValueError:
        return s
# Load Data
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_csv('dataSet/users.txt', engine='python',
                    sep='::', header=None, names=userHeader, encoding='ISO-8859-1')

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_csv('dataSet/movies.txt', engine='python',
                     sep='::', header=None, names=movieHeader, encoding='ISO-8859-1')

ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('dataSet/ratings.txt', engine='python',
                      sep='::', header=None, names=ratingHeader, encoding='ISO-8859-1')

# Merge data
mergeRatings = pd.merge(pd.merge(users, ratings), movies)

# Clone DataFrame


def cloneDF(df):
    a = pd.DataFrame(df.values.copy(), df.index.copy(), df.columns.copy())
    return a.apply(to_numeric)


# Show Films with more votes. (groupby + sorted)
numberRatings = cloneDF(mergeRatings)
numberRatings = numberRatings.groupby(
    'title').size().sort_values(ascending=False)
print('Films with more votes: \n%s' % numberRatings[:10])
print('\n==================================================================\n')


# Show avg ratings movie (groupby + avg)
avgRatings = cloneDF(mergeRatings)
avgRatings = avgRatings.groupby(['movie_id', 'title'])["rating"].mean()
print('Avg ratings: \n%s' % avgRatings[:10])
print('\n==================================================================\n')


# Show data ratings movies (groupby + several funtions)
dataRatings = cloneDF(mergeRatings)
dataRatings = dataRatings.groupby(['movie_id', 'title'])[
    'rating'].agg(['mean', 'sum', 'count', 'std'])
print('Films ratings info: \n%s' % dataRatings[:10])
print('\n==================================================================\n')


# Show data ratings movies, applying a function (groupby + lambda function)
myAvg = cloneDF(mergeRatings)
myAvg = myAvg.groupby(['movie_id', 'title'])['rating'].agg(
    SUM='sum', COUNT=np.size, AVG='mean', myAVG=lambda x: x.sum() / float(x.count()))
print('My info ratings: \n%s' % myAvg[:10])
print('\n==================================================================\n')


# Sort data ratings by created field (groupby + lambda function + sorted)
sortAda = cloneDF(mergeRatings)
sortAda = sortAda.groupby(['movie_id', 'title'])['rating'].agg(
    COUNT=np.size, myAVG=lambda x: x.sum() / float(x.count())).sort_values('COUNT', ascending=False)
print('My info sorted: \n%s' % sortAda[:15])
