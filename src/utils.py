"""
Utility module with example functions for the project.
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any


def create_sample_data(n_samples: int = 100) -> pd.DataFrame:
    """
    Create a sample dataset with random data.
    
    Args:
        n_samples: Number of samples to generate
        
    Returns:
        DataFrame with sample data
    """
    np.random.seed(42)
    
    data = {
        'id': range(1, n_samples + 1),
        'value_a': np.random.normal(0, 1, n_samples),
        'value_b': np.random.exponential(1, n_samples),
        'category': np.random.choice(['X', 'Y', 'Z'], n_samples),
        'date': pd.date_range('2024-01-01', periods=n_samples, freq='D')
    }
    
    return pd.DataFrame(data)


def analyze_data(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyze a DataFrame and return basic statistics.
    
    Args:
        df: DataFrame to analyze
        
    Returns:
        Dictionary with statistics
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    analysis = {
        'shape': df.shape,
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_summary': df[numeric_cols].describe().to_dict() if len(numeric_cols) > 0 else {},
        'categorical_summary': {col: df[col].value_counts().to_dict() 
                              for col in categorical_cols} if len(categorical_cols) > 0 else {}
    }
    
    return analysis


def print_analysis(analysis: Dict[str, Any]) -> None:
    """
    Print analysis in formatted way.
    
    Args:
        analysis: Dictionary with statistics from analysis
    """
    print(f"Dataset shape: {analysis['shape']}")
    print("\nMissing values:")
    for col, missing in analysis['missing_values'].items():
        if missing > 0:
            print(f"  {col}: {missing}")
    
    if analysis['numeric_summary']:
        print("\nNumeric variables summary:")
        for col in analysis['numeric_summary']:
            print(f"  {col}: mean={analysis['numeric_summary'][col]['mean']:.2f}")
    
    if analysis['categorical_summary']:
        print("\nCategorical variables:")
        for col, counts in analysis['categorical_summary'].items():
            print(f"  {col}: {list(counts.keys())}")


if __name__ == "__main__":
    # Test functions
    print("Testing utils module...")
    
    # Create sample data
    df = create_sample_data(50)
    print("Dataset created:")
    print(df.head())
    
    # Analyze data
    analysis = analyze_data(df)
    print("\nAnalysis:")
    print_analysis(analysis)
