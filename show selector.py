import pandas as pd

# list of shows, feelings, genres
shows = [
    ['Breaking Bad', 'Tense', 'crime drama'],
    ['Naurto', 'Excited', 'anime'],
    ['Full House', 'Fun', 'sitcom'],
    ['Vinland Saga', 'Hype', 'anime'],
    ['Gilmore Girls', 'Calm', 'sitcom'],
    ['Shameless', 'Melancholy', 'drama']]
# make it into a dataset using Pandas
shows_df = pd.DataFrame(shows, columns=['show name', 'feeling', 'genre'])

# User feeling input
print('what do you want to feel?')
user_feeling = input()

# filter Panda DataFrame
user_show = shows_df[shows_df['feeling'] == user_feeling]

# display selected show
print(user_show)
