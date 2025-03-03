from tarfile import data_filter

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250303.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
