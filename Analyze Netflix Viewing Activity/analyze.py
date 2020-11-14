# https://www.dataquest.io/blog/python-tutorial-analyze-personal-netflix-data/

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:/Users/A/Downloads/nf/ViewingActivity-sample.csv"
df = pd.read_csv(file_path)
df = df[["Start Time", "Duration", "Title", "Device Type"]]

df["Start Time"] = pd.to_datetime(df["Start Time"], utc=True)
df["Duration"] = pd.to_timedelta(df["Duration"])

# Remove Video preview rows
# print(df["Duration"][5])
df = df[df['Duration'] >= '0 days 00:01:00']

# Convert UTC time to USA
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
df['Start Time'] = df['Start Time'].dt.tz_convert('US/Eastern')


# Extracting 'The Office' show only:
df = df[df["Title"].str.contains("The Office")]

# Extracting some time propertis
df['weekday'] = df['Start Time'].dt.weekday
df['hour'] = df['Start Time'].dt.hour

df.info()

# Analysis:

# df.groupby('weekday').sum().plot.bar()
# plt.show()

df.groupby('hour').count()['Duration'].plot.bar()
plt.show()
