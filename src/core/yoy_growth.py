import pandas as pd
import json

def calculate_yoy_growth(row):
    if pd.isnull(row['employee_count_by_month_by_level']):
        return []
    
    try:
        raw_counts = row['employee_count_by_month_by_level'].replace("'", '"')
        counts = json.loads(raw_counts)
    except (json.JSONDecodeError, AttributeError):
        return []
    
    yearly_data = {}
    for month, levels in counts.items():
        year = month.split('-')[0]
        if year not in yearly_data:
            yearly_data[year] = {}
        for level, count in levels.items():
            yearly_data[year][level] = yearly_data[year].get(level, 0) + count

    results = []
    sorted_years = sorted(yearly_data.keys())
    for i in range(1, len(sorted_years)):
        curr_year, prev_year = sorted_years[i], sorted_years[i - 1]
        for level in yearly_data[curr_year]:
            if level in yearly_data[prev_year]:
                prev_count = yearly_data[prev_year][level]
                curr_count = yearly_data[curr_year][level]
                if prev_count > 0:
                    percent_increase = ((curr_count - prev_count) / prev_count) * 100
                    results.append({
                        "created_at": row["created_at"],
                        "domain_name": row["domain_name"],
                        "level": level,
                        "year": curr_year,
                        "percent_increase": percent_increase
                    })
    return results
