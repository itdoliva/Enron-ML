#!/usr/bin/python

# All original features, ignoring email address
original_features = [
    'poi',
    'salary',
    'to_messages',
    'deferral_payments',
    'total_payments',
    'exercised_stock_options',
    'bonus',
    'restricted_stock',
    'shared_receipt_with_poi',
    'restricted_stock_deferred',
    'total_stock_value',
    'expenses',
    'loan_advances',
    'from_messages',
    'other',
    'from_this_person_to_poi',
    'director_fees',
    'deferred_income',
    'long_term_incentive',
    'from_poi_to_this_person'
    ]

# The below features lists have been produced by printing the sorted feature importances of each classifier

svm_ordered_features = [
    'poi',
    'squared_bonus_ratio',
    'squared_bonus',
    'deferred_income',
    'bonus',
    'bonus_ratio',
    'squared_salary',
    'loan_advances',
    'long_term_incentive',
    'total_payments',
    'restricted_stock_ratio',
    'exercised_stock_options',
    'shared_receipt_with_poi',
    'squared_exercised_stock_options_ratio',
    'total_stock_value',
    'from_poi_to_this_person_ratio',
    'expenses',
    'squared_restricted_stock_ratio',
    'salary',
    'restricted_stock',
    'salary_ratio',
    'from_this_person_to_poi_ratio',
    'director_fees',
    'squared_from_this_person_to_poi_ratio',
    'expenses_ratio',
    'from_poi_to_this_person',
    'squared_expenses_ratio',
    'from_this_person_to_poi',
    'to_messages',
    'squared_expenses',
    'squared_salary_ratio',
    'exercised_stock_options_ratio',
    'from_messages',
    'restricted_stock_deferred',
    'squared_from_poi_to_this_person_ratio',
    'other',
    'deferral_payments'
]

dt_ordered_features = [
    'poi',
    'bonus',
    'squared_bonus',
    'restricted_stock_ratio',
    'expenses',
    'exercised_stock_options',
    'squared_expenses_ratio',
    'salary_ratio',
    'from_messages',
    'squared_from_this_person_to_poi_ratio',
    'squared_salary',
    'salary',
    'to_messages',
    'deferral_payments',
    'total_payments',
    'restricted_stock',
    'shared_receipt_with_poi',
    'restricted_stock_deferred',
    'total_stock_value',
    'loan_advances',
    'other',
    'from_this_person_to_poi',
    'director_fees',
    'deferred_income',
    'long_term_incentive',
    'from_poi_to_this_person',
    'bonus_ratio',
    'expenses_ratio',
    'from_poi_to_this_person_ratio',
    'from_this_person_to_poi_ratio',
    'exercised_stock_options_ratio',
    'squared_expenses',
    'squared_salary_ratio',
    'squared_bonus_ratio',
    'squared_from_poi_to_this_person_ratio',
    'squared_exercised_stock_options_ratio',
    'squared_restricted_stock_ratio'
]
