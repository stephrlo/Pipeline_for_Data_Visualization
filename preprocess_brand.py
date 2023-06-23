import pandas as pd
import os.path as path


inputfile = "/Users/mac/Data/prep_tableau/clean_data/clean_data_2023-04.csv"
outputfile = "clean_brand/ev_vehicle_brands_2023-04.csv" #edit date as needed

# Read in the data
auto_df = pd.read_csv(inputfile)

# Defining the Dataframe and renaming columns
processed_auto = pd.DataFrame(auto_df.groupby(["Vehicle_Make", "Calendar_Year"])["Calendar_Year"].count())
processed_auto = processed_auto.rename(columns={"Calendar_Year": "count"}).reset_index()

# Pivoting the data based on Vehicle Make and Year with their respective counts
processed_auto_pivot = processed_auto.pivot(index='Vehicle_Make', columns='Calendar_Year', values='count').reset_index()

# Defining column list required for the For Loop
col_list = range(2019, 2024)

# Looking at magnitude every 1000 cars - for loop
for year in col_list:
    column_name = f"per_1K_{year}"
    total_column = year
    processed_auto_pivot[column_name] = round(processed_auto_pivot[total_column] / processed_auto_pivot[total_column].sum(), 4) * 1000

#Calculating prop_num_change
processed_auto_pivot["prop_num_change"] = processed_auto_pivot["per_1K_2022"] - processed_auto_pivot["per_1K_2019"]

# Pivoting for totals
cars_per1K = pd.melt(
    processed_auto_pivot,
    id_vars=["Vehicle_Make", "prop_num_change"],
    value_vars=["per_1K_2019", "per_1K_2020", "per_1K_2021", "per_1K_2022", "per_1K_2023"],
    var_name="year",
    value_name="per_1K"
).loc[:, ["Vehicle_Make", "year", "per_1K", "prop_num_change"]]


# Convert the columns to be merged on to the same data type
processed_auto["Calendar_Year"] = processed_auto["Calendar_Year"].astype(str)
cars_per1K["year"] = cars_per1K["year"].astype(str)

#making year names consistent with processed_auto
cars_per1K["year"]= cars_per1K["year"].str.replace("per_1K_", "")

#joining the total counts with 1K totals
ev_totals = processed_auto.merge(cars_per1K, left_on=["Vehicle_Make", "Calendar_Year"], right_on=["Vehicle_Make", "year"], how="left")

#dropping irrevelant column
ev_totals = ev_totals.drop("year", axis=1)

#ranking brand by counts
ev_totals['rank'] = ev_totals.groupby('Calendar_Year')['count'].rank(ascending=False, method="min")
ev_totals = ev_totals.sort_values(['Vehicle_Make', 'Calendar_Year'])

#creating previous rank, lag by rank
ev_totals['previous_rank'] = ev_totals.groupby('Vehicle_Make')['rank'].shift()

# save to csv
print(f"\tWriting outputfile as "+ outputfile)
brand_path = path.abspath(path.join(__file__ ,'../', outputfile ))
ev_totals.to_csv(brand_path,index=False)