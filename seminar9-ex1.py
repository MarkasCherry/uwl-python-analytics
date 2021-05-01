# Seminar 9, Exercise 1, Databases and Analytics (CP60056E)
# University of West London
# Assignment 2
# Markas Vysniauskas (21372173)

# Exercise 1 tasks and outputs:

import pandas as pd

# Create a dictionary with student details
student_details = {
    'Name': ['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind', 'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'],
    'Subject': ['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 'Chemistry',
                'Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 'Chemistry'],
    'Marks': [80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70]
}

# Convert dictionary to a DataFrame

df = pd.DataFrame(student_details)

# print(df)

# Create a new column with Marks
# ranked in descending order

df['Mark_Rank'] = df['Marks'].rank(ascending=0)

# Set index to newly created column and print the df

df = df.set_index('Mark_Rank')

print(df)

# Sort the DataFrame based on the index and print the df

df = df.sort_index()

print(df)

# Rank the marks using the following methods: default, max, bottom. Print the df

df['Mark_Average'] = df['Marks'].rank()
df['Mark_Max'] = df['Marks'].rank(method='max')
df['Mark_Bottom'] = df['Marks'].rank(na_option='bottom')

print(df)

