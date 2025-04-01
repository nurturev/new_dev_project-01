import pandas as pd
import ast

def process_employee_growth(df_raw):
    data = []
    for _, row in df_raw.iterrows():
        domain_name = row['domain_name']
        try:
            monthly_data = ast.literal_eval(row['employee_count_by_month'])
        except (ValueError, SyntaxError):
            continue
        
        monthly_df = pd.DataFrame(list(monthly_data.items()), columns=['month', 'employee_count'])
        monthly_df['month'] = pd.to_datetime(monthly_df['month'], format='%Y-%m')
        monthly_df['quarter'] = monthly_df['month'].dt.to_period('Q')

        for quarter, group in monthly_df.groupby('quarter'):
            first_month_count = group.iloc[0]['employee_count']
            last_month_count = group.iloc[-1]['employee_count']
            percent_increase = ((last_month_count - first_month_count) / first_month_count) * 100

            data.append({
                'created_at': group.iloc[-1]['month'],
                'domain_name': domain_name,
                'quarter': str(quarter),
                'percent_increase': percent_increase
            })

    return pd.DataFrame(data)
