
import sys
import os
#testing
# Add the 'src' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import config 
from adapters.s3_loader import S3Loader
from core.employee_growth import process_employee_growth
from core.yoy_growth import calculate_yoy_growth
import pandas as pd


def main():
    bucket_name = config.S3_BUCKET_NAME
    file_key = config.S3_FILE_KEY

    s3_loader = S3Loader(bucket_name)
    df_raw = s3_loader.load_csv(file_key)
    
    employee_growth = process_employee_growth(df_raw)
    print("Employee Growth Data:")
    print(employee_growth.head())
    
    results = []
    for _, row in df_raw.iterrows():
        results.extend(calculate_yoy_growth(row))
    
    yoy_growth_df = pd.DataFrame(results)
    print("Year-over-Year Growth:")
    print(yoy_growth_df.head())

if __name__ == "__main__":
    main()
