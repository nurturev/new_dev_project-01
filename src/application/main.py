from adapters.s3_loader import S3Loader
from core.employee_growth import process_employee_growth
from core.yoy_growth import calculate_yoy_growth
import pandas as pd

def main():
    bucket_name = "nv-tenant-models"
    file_key = "202/pdl_raw_company_info/pdl_raw_company_info_1732559219.335818.csv"
    
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
