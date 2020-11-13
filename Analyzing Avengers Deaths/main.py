# https://github.com/fivethirtyeight/data/tree/master/avengers
# https://fivethirtyeight.com/features/avengers-death-comics-age-of-ultron/

import pandas as pd
import matplotlib.pyplot as plt

lnk = "https://raw.githubusercontent.com/fivethirtyeight/data/master/avengers/avengers.csv"
avengers = pd.read_csv(lnk, encoding="windows-1252")
cols = avengers.columns
hd = avengers.head(5)

# We only want to keep the Avengers who were introduced after 1960.
#     Store only the rows describing Avengers added in 1960 or later in true_avengers.

true_avengers = pd.DataFrame()
true_avengers = avengers[avengers["Year"] >= 1960]
true_avengers["Year"].hist()

# We're interested in the total number of deaths each character experienced, so we'd like to have a single field containing that information. Right now, there are five fields (Death1 to Death5), each of which contains a binary value representing whether a superhero experienced that death or not. For example, a superhero could experience Death1, then Death2, and so on until the writers decided not to bring the character back to life.
# We'd like to combine that information in a single field so we can perform numerical analysis on it more easily.
#     Create a new column, Deaths, that contains the number of times each superhero died. The possible values for each death field are YES, NO, and NaN for missing data.
#         Keep all of the original columns (including Death1 to Death5) and update true_avengers with the new Deaths column.

true_avengers["Deaths"] = 0

for i in range(1, 6):
    true_avengers["Deaths"] = true_avengers["Deaths"] + (true_avengers[f"Death{i}"] == "YES")

print(true_avengers["Deaths"].value_counts())


# For our final task, we want to verify that the Years since joining field accurately reflects the Year column. For example, if an Avenger was introduced in the Year 1960, is the Years since joining value for that Avenger 55?
#     Calculate the number of rows where Years since joining is accurate.
#         Because this challenge was created in 2015, use that as the reference year.
#         We want to know for how many rows Years since joining was correctly calculated as the Year value subtracted from 2015.
#         Assign the integer value describing the number of rows with a correct value for Years since joining to joined_accuracy_count.


joined_accuracy_count = (true_avengers["Years since joining"] == (2015 - true_avengers["Year"])).value_counts()

print(joined_accuracy_count)
