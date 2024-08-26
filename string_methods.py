# Q.5
# Write a solution to find the IDs of the invalid tweets. 
# The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

# Return the result table in any order.

# The result format is in the following example.

# Input: 
# Tweets table:
# +----------+----------------------------------+
# | tweet_id | content                          |
# +----------+----------------------------------+
# | 1        | Vote for Biden                   |
# | 2        | Let us make America great again! |
# +----------+----------------------------------+
# Output: 
# +----------+
# | tweet_id |
# +----------+
# | 2        |
# +----------+

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # filter rows where length of content is > 15
    invalid_df = tweets[tweets['content'].str.len() > 15]
    # Alternative using lambda
    ## invalid_df = tweets[tweets['content'].apply(lambda x: True if len(x)> 15 else False)]

    # obtain only tweet_id of the invalids df
    output_df = invalid_df[['tweet_id']]        # the double brackets ensures a dataframe of the selected collumn is returned
    return output_df

# === test code

# tweets = pd.read_csv('./test_data.csv', sep=',')
# print(invalid_tweets(tweets))