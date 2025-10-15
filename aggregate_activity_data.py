import pandas as pd
import numpy as np
from pathlib import Path

def aggregate_subject_activity(filepath):
    df = pd.read_csv(filepath)
    
    return {
        'mean_activity': df['activity'].mean(),
        'sd_activity': df['activity'].std(),
        'median_activity': df['activity'].median(),
        'total_activity': df['activity'].sum(),
        'min_activity': df['activity'].min(),
        'max_activity': df['activity'].max(),
        'n_observations': len(df)
    }

def process_group(folder_path, group_label):
    folder = Path(folder_path)
    results = []
    
    for csv_file in sorted(folder.glob('*.csv')):
        subject_id = csv_file.stem
        metrics = aggregate_subject_activity(csv_file)
        metrics['subject_id'] = subject_id
        metrics['group'] = group_label
        results.append(metrics)
    
    return pd.DataFrame(results)

def main():
    base_path = Path('/Users/dheerajpv/Documents/SPSS/Depresjon')
    
    condition_df = process_group(base_path / 'condition', 'condition')
    control_df = process_group(base_path / 'control', 'control')
    
    activity_summary = pd.concat([condition_df, control_df], ignore_index=True)
    
    scores = pd.read_csv(base_path / 'scores.csv')
    
    activity_summary['subject_number'] = activity_summary['subject_id'].str.extract(r'(\d+)')[0].astype(int)
    scores['subject_number'] = scores['number'].str.extract(r'(\d+)')[0].astype(int)
    
    final_dataset = pd.merge(
        activity_summary,
        scores,
        on='subject_number',
        how='left'
    )

    # Remove duplicates to keep only first occurrence of each subject
    final_dataset = final_dataset.drop_duplicates(subset=['subject_id'])

    final_dataset['group_numeric'] = final_dataset['group'].map({'control': 0, 'condition': 1})
    
    column_order = [
        'subject_id', 'subject_number', 'group', 'group_numeric',
        'mean_activity', 'sd_activity', 'median_activity', 
        'total_activity', 'min_activity', 'max_activity', 'n_observations',
        'days', 'gender', 'age', 'afftype', 'melanch', 'inpatient',
        'edu', 'marriage', 'work', 'madrs1', 'madrs2'
    ]
    
    final_dataset = final_dataset[column_order]
    
    output_path = base_path / 'depression_analysis_dataset.csv'
    final_dataset.to_csv(output_path, index=False)
    
    return final_dataset

if __name__ == '__main__':
    df = main()