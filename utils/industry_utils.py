import pandas as pd

# Define the industry mapping
industry_mapping = {
    'Financial Services': ['Financial Services', 'Finance', 'Finance General', 'Other Capital Markets/Institutions'],
    'IT Services and Consulting': ['IT Services and IT Consulting', 'Information Technology & Services', 'Technology, Information and Media', 'Information Technology', 'Software Development & Design'],
    'Maritime': ['Maritime Transportation', 'Maritime'],
    'Construction': ['Commercial & Residential Construction', 'Construction'],
    'Telecommunications': ['Telecommunications', 'Cable & Satellite', 'Satellite Telecommunications'],
    'Manufacturing': ['Manufacturing', 'Industrial Machinery Manufacturing', 'Computer Hardware Manufacturing'],
    'Software Development': ['Software Development', 'Software Development & Design', 'Software'],
    'Education': ['Education Administration Programs', 'Colleges & Universities', 'Education', 'Higher Education'],
    'Healthcare': ['Health Care', 'Hospitals and Health Care', 'Medical Practices'],
    'Retail': ['Retail', 'Consumer Goods', 'E-Commerce'],
    'Transportation': ['Transportation', 'Truck Transportation'],
    'Energy': ['Oil and Gas', 'Renewable Energy Power Generation'],
    'Non-profit': ['Non-profit Organizations', 'Charitable Organizations & Foundations'],
    'Government': ['Government Administration', 'Government']
}

def standardize_industry(industry):
    for standard, variations in industry_mapping.items():
        if any(var in industry for var in variations):
            return standard
    return industry

