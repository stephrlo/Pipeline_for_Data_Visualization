import pandas as pd 
import os.path as path

inputfile = "/Users/mac/Data/prep_tableau/input/izev-april-2023.csv"
outputfile = 'clean_data/clean_data_2023-04.csv'

# Read in the data
df = pd.read_csv(inputfile)
print(f"The dataframe has {df.shape[0]} rows and {df.shape[1]} columns")

#removing certain columns
clean_df = df[df.columns[~df.columns.isin(['Incentive Request Date', 'Government of Canada Fiscal Year (FY)','Dealership Province / Territory '
                                           'Dealership Postal Code','BEV/PHEV/FCEV - Battery equal to or greater than 15 kWh or \nElectric range equal to or greater than 50 km',
                                           'BEV, PHEV  ? 15 kWh or PHEV < 15 kWh (until April 24, 2022) \nand\nPHEV ?  50 km or PHEV < 50 km and  FCEVs ? 50 km or FCEVs < 50 km\n(April 25, 2022 onward)',
                                           'Individual or Organization \n(Recipient)','Country'])]]

# shortening longer column names
clean_df = clean_df.rename({"Battery-Electric Vehicle (BEV), Plug-in Hybrid Electric Vehicle (PHEV) or Fuel Cell Electric Vehicle (FCEV)" : "EV_Type",
                     "Recipient Province / Territory":"Province.Recipient"},axis="columns")

# adding underscores between column names
clean_df.columns = clean_df.columns.str.strip()
clean_df.columns = clean_df.columns.str.replace(' ', '_')

# removing nulls
clean_df = clean_df.dropna(how="all")

# dictionary to replace values with a specified string when duplicates
replacements = {"\\bsmart (EQ )fortwo (cabriolet|coupe)" : "Smart Electric",
                "\\bsmart fortwo electric drive (cabriolet|coupe)" : "Smart Electric",
                "\\bVolvo C40?( Recharge)\\b|Volvo XC40" : "Volvo C40",
                "\\bNissan Leaf?( Plus)" : "Nissan Leaf",
                "\\bMINI (3 Door|Cooper SE 3 Door)?( Hatch)|MINI Cooper SE 3 Door" : "MINI 3 Door",
                "Hyundai Ioniq PHEV|Hyundai Ioniq Plug-In hybrid" : "Hyundai Ioniq PHEV",
                "\\bHyundai Ioniq electric?( Plus)\\b" : "Hyundai Ioniq electric",
                "\\bChevrolet Bolt\\b" : "Chevrolet Bolt",
                "\\bAudi Q4 50 e-tron Quattro|Audi Q4 e-tron Quattro\\b" : "Audi Q4 e-tron Quattro" }

# For loop to replace strings in Vehicle Make and Model colum
for old, new in replacements.items():
  clean_df["Vehicle_Make_and_Model"] = clean_df["Vehicle_Make_and_Model"].str.replace(old, new, regex=True)

# save to csv
print(f"\tWriting outputfile as "+ outputfile)
clean_path = path.abspath(path.join(__file__ ,'../', outputfile ))
clean_df.to_csv(clean_path,index=False)