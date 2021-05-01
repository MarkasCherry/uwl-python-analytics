# Seminar 9, Exercise 2, Databases and Analytics (CP60056E)
# University of West London
# Assignment 2
# Markas Vysniauskas (21372173)

import numpy as np
import pandas as pd

raw_Data = {
    'Voter_name':
        ['Geek1', 'Geek2', 'Geek3', 'Geek4', 'Geek5', 'Geek6', 'Geek7', 'Geek8'],

    'Voter_age':
        [15, 23, 25, 9, 67, 54, 42, np.NaN]
}

df = pd.DataFrame(raw_Data, columns=['Voter_name', 'Voter_age'])

print(df)

vote = []
for age in df['Voter_age']:
    if age < 18:
        vote.append("No")
    elif age >= 18:
        vote.append("Yes")
    else:
        vote.append("Not sure")

df['Vote'] = vote

print(df)
