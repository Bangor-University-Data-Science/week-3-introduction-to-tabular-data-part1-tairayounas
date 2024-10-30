import pandas as pd

def create_feature_type_dict(df: pd.DataFrame) -> dict:
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            if column in ['Age', 'Fare'] or len(df[column].unique()) > 20:  # Treat Age and Fare as continuous
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].dtype == 'object':
            feature_types['categorical']['nominal'].append(column)


    ordinal_features = ['Pclass']
    feature_types['categorical']['ordinal'].extend(ordinal_features)

    return feature_types
