
## Heroes of Pymoli


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
csv_file = "Resources/purchase_data.csv"

# Read data file and store into data frame
purchase_data = pd.read_csv(csv_file)
```


```python
# Clean/Prepare the data
item_data = purchase_data.loc[:,["Item ID", "Item Name", "Price"]]
player_demographics = purchase_data.loc[:, ["Gender", "SN", "Age"]]
player_demographics = player_demographics.drop_duplicates()
```


```python
# Player Count

# Do the math
player_count = player_demographics.count()[0]

# Make pretty output
player_count_data = pd.DataFrame({"Total Players": [player_count]})
```

### Player Count


```python
player_count_data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Total)

# Do the math
item_count = len(purchase_data["Item ID"].unique())
average_purchase_price = purchase_data["Price"].mean()
purchase_count = purchase_data["Price"].count()
total_revenue = purchase_data["Price"].sum()
```


```python
# Save to data frame
purchasing_analysis = pd.DataFrame({"Number of Unique Items": item_count,
                                    "Average Purchase Price": average_purchase_price,
                                    "Total Number of Purchases": purchase_count,
                                    "Total Revenue": total_revenue}, index=[0])
```


```python
# Make pretty output
purchasing_analysis_data = purchasing_analysis.round(2)
purchasing_analysis_data["Average Purchase Price"] = purchasing_analysis_data["Average Purchase Price"].map("${:,.2f}".format)
purchasing_analysis_data["Total Number of Purchases"] = purchasing_analysis_data["Total Number of Purchases"].map("${:,.2f}".format)
purchasing_analysis_data["Total Revenue"] = purchasing_analysis_data["Total Revenue"].map("${:,.2f}".format)
```

### Purchasing Analysis (Total)


```python
purchasing_analysis_data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$3.05</td>
      <td>$780.00</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender Demographics

# Do the math
gender_demographics_totals = player_demographics["Gender"].value_counts()
gender_demographics_percents = gender_demographics_totals / player_count * 100

# Make pretty output
gender_demographics_data = pd.DataFrame({"Total Count": gender_demographics_totals,
                                         "Percentage of Players": gender_demographics_percents}).round(2)
```

### Gender Demographics


```python
gender_demographics_data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>484</td>
      <td>84.03</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>81</td>
      <td>14.06</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>1.91</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```

### Purchasing Analysis (Gender)


```python
gender_purchase_data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Average Per Person</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>$3.20</td>
      <td>$361.94</td>
      <td>$4.47</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$3.02</td>
      <td>$1,967.64</td>
      <td>$4.07</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>$3.35</td>
      <td>$50.19</td>
      <td>$4.56</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```

### Age Demographics


```python
age_demographics_data.sort_index()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>17</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>22</td>
      <td>3.82</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>107</td>
      <td>18.58</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>258</td>
      <td>44.79</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>77</td>
      <td>13.37</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>52</td>
      <td>9.03</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>31</td>
      <td>5.38</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>12</td>
      <td>2.08</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```

### Purchasing Analysis (Age)


```python
age_purchase_data.sort_index()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Average Per Person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>$2.96</td>
      <td>$82.78</td>
      <td>$3.76</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>$3.04</td>
      <td>$412.89</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>$3.05</td>
      <td>$1,114.06</td>
      <td>$4.32</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>$2.90</td>
      <td>$293.00</td>
      <td>$3.81</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>$2.93</td>
      <td>$214.00</td>
      <td>$4.12</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>$3.60</td>
      <td>$147.67</td>
      <td>$4.76</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>$2.94</td>
      <td>$38.24</td>
      <td>$3.19</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>$3.35</td>
      <td>$77.13</td>
      <td>$4.54</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Spenders

# Do the math
user_purchase_total = purchase_data.groupby(["SN"]).sum()["Price"].rename("Total Purchase Value")
user_purchase_average = purchase_data.groupby(["SN"]).mean()["Price"].rename("Average Purchase Price")
user_purchase_counts = purchase_data.groupby(["SN"]).count()["Price"].rename("Purchase Count")

# Make pretty output
user_purchase_data = pd.DataFrame({"Purchase Count": user_purchase_counts,
                                   "Average Purchase Price": user_purchase_average.map("${:,.2f}".format),
                                   "Total Purchase Value": user_purchase_total.map("${:,.2f}".format)})
```

### Top Spenders


```python
user_purchase_data.sort_values("Purchase Count", ascending=False).head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>5</td>
      <td>$3.79</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>$3.40</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>$3.86</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Asur53</th>
      <td>3</td>
      <td>$2.48</td>
      <td>$7.44</td>
    </tr>
    <tr>
      <th>Inguron55</th>
      <td>3</td>
      <td>$3.70</td>
      <td>$11.11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Popular Items

# Do the math
item_popular_purchase_total = item_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")
item_popular_purchase_price = item_data.groupby(["Item ID", "Item Name"]).min()["Price"]
item_popular_purchase_counts = item_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")

# Make pretty output
item_popular_purchase_data = pd.DataFrame({"Purchase Count": item_popular_purchase_counts,
                                           "Item Price":item_popular_purchase_price.map("${:,.2f}".format),
                                           "Total Purchase Value": item_popular_purchase_total.map("${:,.2f}".format)})
```

### Most Popular Items


```python
item_popular_purchase_data.sort_values("Purchase Count", ascending=False).head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>$1.02</td>
      <td>$8.16</td>
    </tr>
  </tbody>
</table>
</div>



### Most Profitable Items


```python
item_popular_purchase_data.sort_values("Total Purchase Value", ascending=False).head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>63</th>
      <th>Stormfury Mace</th>
      <td>2</td>
      <td>$4.99</td>
      <td>$9.98</td>
    </tr>
    <tr>
      <th>29</th>
      <th>Chaos, Ender of the End</th>
      <td>5</td>
      <td>$1.98</td>
      <td>$9.90</td>
    </tr>
    <tr>
      <th>173</th>
      <th>Stormfury Longsword</th>
      <td>2</td>
      <td>$4.93</td>
      <td>$9.86</td>
    </tr>
    <tr>
      <th>1</th>
      <th>Crucifer</th>
      <td>3</td>
      <td>$3.26</td>
      <td>$9.78</td>
    </tr>
    <tr>
      <th>38</th>
      <th>The Void, Vengeance of Dark Magic</th>
      <td>4</td>
      <td>$2.37</td>
      <td>$9.48</td>
    </tr>
  </tbody>
</table>
</div>



### Observable Trends

> Game players who are male between the ages of 20 and 24 tend to purchase more than any other age group.  Females spend has a higher per person purchase price than males.  Players between 30 and 39 have the highest per person purchase price.
