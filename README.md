2# Pipeline_for_Data_Visualizations

**Summary** /n

Python scripts to help automate your Tableau data for easier transformation for your visualizations. The tutorial for this code is to be run alongside Medium Article: "How To Prepare Your Data For Visualizations" by Stephanie Lo.  

**Contents** /n

The contents of the repo are split into two: the Python Scripts that run each stage of the Pipeline, and the folders where the inputs/outputs of the Python scripts are delivered. The following contains a brief description of each file/folder: 

**Python Scripts** /n
1. **clean_data.py** - Step 1 of the Pipeline that takes data from inputs and cleans the data.
2. **clean_model.py & clean_brand.py** Step 2 of the Pipeline that transforms clean data to aggregated data that is seperated out in appropriate columns for Visualizations.
3. **hyper_conversion.py** Step 3 of the Pipeline that converts .csv files to .hyper files for easy integration with Tableau in the form of Tableau extracts. 

**Folders** /n

1. **input** - Monthly raw data files, refer to the original dataset from the Government of Canada website [here](https://open.canada.ca/data/en/dataset/42986a95-be23-436e-af15-7c6bf292a2e1). The download name should be "Statistics on the Incentives for Zero-Emission Vehicles (iZEV) Program CSV" (English Version). 
2. **clean_data** - Output of the first Python script clean_data.py
3. **clean_model & clean_brand** - Outputs of scripts from the second stage of the Pipeline
4. **hyper** - Output of Hyper files, converting most recent files only. 

**Software** /n
[Python & VS Code](https://code.visualstudio.com/download)

*Note: The markdown file and visuals were functional as of 6/20/2023, and included data until April 2023. Any subsequent edits or additions to the original data file may mean that you have to adjust the code in order to ensure the pipeline works.*
