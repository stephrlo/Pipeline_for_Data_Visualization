import pandas as pd
import pantab

#read in files
brand_df = pd.read_csv('/Users/mac/Data/prep_tableau/clean_brand/ev_vehicle_brands_2023-04.csv')  
model_df = pd.read_csv('/Users/mac/Data/prep_tableau/clean_model/ev_vehicle_models_2023-04.csv')  

#save to hyper file
pantab.frame_to_hyper(brand_df, "hyper/rank_vehicle_brands.hyper", table="rank_vehicle_brands")
pantab.frame_to_hyper(model_df, "hyper/ev_vehicle_models.hyper", table="rank_vehicle_models")