
## Heroes of Pymoli

# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
csv_file = "Resources/purchase_data.csv"

# Read data file and store into data frame
purchase_data = pd.read_csv(csv_file)

# Clean/Prepare the data
item_data = purchase_data.loc[:,["Item ID", "Item Name", "Price"]]
player_demographics = purchase_data.loc[:, ["Gender", "SN", "Age"]]
player_demographics = player_demographics.drop_duplicates()

# Player Count

# Do the math
player_count = player_demographics.count()[0]

# Make pretty output
player_count_data = pd.DataFrame({"Total Players": [player_count]})

### Player Count

player_count_data

# Purchasing Analysis (Total)

# Do the math
item_count = len(purchase_data["Item ID"].unique())
average_purchase_price = purchase_data["Price"].mean()
purchase_count = purchase_data["Price"].count()
total_revenue = purchase_data["Price"].sum()

# Save to data frame
purchasing_analysis = pd.DataFrame({"Number of Unique Items": item_count,
                                    "Average Purchase Price": average_purchase_price,
                                    "Total Number of Purchases": purchase_count,
                                    "Total Revenue": total_revenue}, index=[0])

# Make pretty output
purchasing_analysis_data = purchasing_analysis.round(2)
purchasing_analysis_data["Average Purchase Price"] = purchasing_analysis_data["Average Purchase Price"].map("${:,.2f}".format)
purchasing_analysis_data["Total Number of Purchases"] = purchasing_analysis_data["Total Number of Purchases"].map("${:,.2f}".format)
purchasing_analysis_data["Total Revenue"] = purchasing_analysis_data["Total Revenue"].map("${:,.2f}".format)

### Purchasing Analysis (Total)

purchasing_analysis_data

# Gender Demographics

# Do the math
gender_demographics_totals = player_demographics["Gender"].value_counts()
gender_demographics_percents = gender_demographics_totals / player_count * 100

# Make pretty output
gender_demographics_data = pd.DataFrame({"Total Count": gender_demographics_totals,
                                         "Percentage of Players": gender_demographics_percents}).round(2)

### Gender Demographics

gender_demographics_data

# Purchasing Analysis (Gender)

# Do the math
gender_purchase_total = purchase_data.groupby(["Gender"]).sum()["Price"].rename("Total Purchase Value")
gender_purchase_average = purchase_data.groupby(["Gender"]).mean()["Price"].rename("Average Purchase Price")
gender_purchase_counts = purchase_data.groupby(["Gender"]).count()["Price"].rename("Purchase Count")
gender_purchase_average_per_person = gender_purchase_total / gender_demographics_data["Total Count"]

# Make pretty output
gender_purchase_data = pd.DataFrame({"Purchase Count": gender_purchase_counts,
                                     "Average Purchase Price": gender_purchase_average.map("${:,.2f}".format),
                                     "Total Purchase Value": gender_purchase_total.map("${:,.2f}".format),
                                     "Average Per Person": gender_purchase_average_per_person.map("${:,.2f}".format)})

### Purchasing Analysis (Gender)

gender_purchase_data

# Age Demographics

# Do the math
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
age_groups_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

player_demographics["Age Ranges"] = pd.cut(player_demographics["Age"], age_bins, labels=age_groups_names)

age_demographics_totals = player_demographics["Age Ranges"].value_counts()
age_demographics_percents = age_demographics_totals / player_count * 100

# Make pretty output
age_demographics_data = pd.DataFrame({"Total Count": age_demographics_totals,
                                      "Percentage of Players": age_demographics_percents.round(2)})

### Age Demographics

age_demographics_data.sort_index()

# Purchasing Analysis (Age)

# Do the math
purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=age_groups_names)

age_purchase_total = purchase_data.groupby(["Age Ranges"]).sum()["Price"].rename("Total Purchase Value")
age_purchase_average = purchase_data.groupby(["Age Ranges"]).mean()["Price"].rename("Average Purchase Price")
age_purchase_counts = purchase_data.groupby(["Age Ranges"]).count()["Price"].rename("Purchase Count")
age_purchase_average_per_person = age_purchase_total / age_demographics_data["Total Count"]

# Make pretty output
age_purchase_data = pd.DataFrame({"Purchase Count": age_purchase_counts,
                                  "Average Purchase Price": age_purchase_average.map("${:,.2f}".format),
                                  "Total Purchase Value": age_purchase_total.map("${:,.2f}".format),
                                  "Average Per Person": age_purchase_average_per_person.map("${:,.2f}".format)})

### Purchasing Analysis (Age)

age_purchase_data.sort_index()

# Top Spenders

# Do the math
user_purchase_total = purchase_data.groupby(["SN"]).sum()["Price"].rename("Total Purchase Value")
user_purchase_average = purchase_data.groupby(["SN"]).mean()["Price"].rename("Average Purchase Price")
user_purchase_counts = purchase_data.groupby(["SN"]).count()["Price"].rename("Purchase Count")

# Make pretty output
user_purchase_data = pd.DataFrame({"Purchase Count": user_purchase_counts,
                                   "Average Purchase Price": user_purchase_average.map("${:,.2f}".format),
                                   "Total Purchase Value": user_purchase_total.map("${:,.2f}".format)})

### Top Spenders

user_purchase_data.sort_values("Purchase Count", ascending=False).head(5)

# Most Popular Items

# Do the math
item_popular_purchase_total = item_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")
item_popular_purchase_price = item_data.groupby(["Item ID", "Item Name"]).min()["Price"]
item_popular_purchase_counts = item_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")

# Make pretty output
item_popular_purchase_data = pd.DataFrame({"Purchase Count": item_popular_purchase_counts,
                                           "Item Price":item_popular_purchase_price.map("${:,.2f}".format),
                                           "Total Purchase Value": item_popular_purchase_total.map("${:,.2f}".format)})

### Most Popular Items

item_popular_purchase_data.sort_values("Purchase Count", ascending=False).head(5)

### Most Profitable Items

item_popular_purchase_data.sort_values("Total Purchase Value", ascending=False).head(5)

### Observable Trends

# Game players who are male between the ages of 20 and 24 tend to purchase more than any other age group.  Females spend has a higher per person purchase price than males.  Players between 30 and 39 have the highest per person purchase price.