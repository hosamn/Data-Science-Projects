import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


lnk = r'C:\Users\A\Desktop\StarWars.csv'
df = pd.read_csv(lnk, encoding="Latin")
df.shape
# df.columns
# df.info()
# df.iloc[[5]]

# df[df["RespondentID"].isna()]

df = df[df["RespondentID"].notna()]

# df.shape

# df.iloc[[5]]

# df.iloc[:, 1]

df.iloc[:, 1].value_counts(dropna=False)

df.iloc[:, 2].value_counts(dropna=False)

my_mapping = {
    "Yes": True,
    "No": False,
    np.NaN: np.NaN,
}

df.iloc[:, 1] = df.iloc[:, 1].map(my_mapping)
df.iloc[:, 2] = df.iloc[:, 2].map(my_mapping)

df.iloc[:, 1].value_counts(dropna=False)

df.iloc[:, 2].value_counts(dropna=False)

df.iloc[:, 3].str.contains("Star", na=False).value_counts(dropna=False)

df.iloc[:, 3] = df.iloc[:, 3].str.contains("Star", na=False)
df.iloc[:, 4] = df.iloc[:, 4].str.contains("Star", na=False)
df.iloc[:, 5] = df.iloc[:, 5].str.contains("Star", na=False)
df.iloc[:, 6] = df.iloc[:, 6].str.contains("Star", na=False)
df.iloc[:, 7] = df.iloc[:, 7].str.contains("Star", na=False)
df.iloc[:, 8] = df.iloc[:, 8].str.contains("Star", na=False)

# for i in range(3, 9):
#     print(df.iloc[:, i].value_counts())


df.columns
rename_dict = {
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    "Unnamed: 4": "seen_2",
    "Unnamed: 5": "seen_3",
    "Unnamed: 6": "seen_4",
    "Unnamed: 7": "seen_5",
    "Unnamed: 8": "seen_6",
}

df.rename(columns=rename_dict, inplace=True)

df.columns[3:9]

df[df.columns[9:15]] = df[df.columns[9:15]].astype(float)

df[df.columns[9:15]].dtypes

old_names = df.columns[9:15]
new_names = ["ranking_{}".format(i) for i in range(1, 7)]

ren_dict = dict(zip(old_names, new_names))
df.rename(columns=ren_dict, inplace=True)

df.columns[9:15]

[i for i in df.columns if "ranking" in i]

df.columns[9:15]

df[df.columns[9:15]].mean()


# 1. Star Wars: Episode I The Phantom Menace
# 1. Star Wars: Episode II Attack of the Clones
# 1. Star Wars: Episode III Revenge of the Sith
# 1. Star Wars: Episode IV A New Hope
# 1. Star Wars: Episode V The Empire Strikes Back
# 1. Star Wars: Episode VI Return of the Jedi

# df[df.columns[9:15]].mean().plot(kind="bar")

# df[df.columns[3:9]].sum().plot(kind="bar")

# # Males:
# # Seens :
# df[df["Gender"] == "Male"].iloc[:, 3:9].mean().plot(kind="bar")
# # Ranking:
# df[df["Gender"] == "Male"].iloc[:, 9:15].sum().plot.bar()

# # Females:
# # Seens :
# df[df["Gender"] == "Female"].iloc[:, 3:9].mean().plot(kind="bar")
# # Ranking:
# df[df["Gender"] == "Female"].iloc[:, 9:15].sum().plot.bar()

ddd = pd.DataFrame(index=[f'movie_{i}' for i in range(1, 7)])

ddd['seen'] = df.iloc[:, 3:9].sum().values
ddd['rank'] = df.iloc[:, 9:15].mean().values

print(ddd)

# sns.displot(
#     df,
#     x=,
#     col=,
#     row="Gender",
# )

# plt.show()
