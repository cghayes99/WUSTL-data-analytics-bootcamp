#!/opt/anaconda3/bin/python

'''
###################################################################################
# @script   PyBank  main.py                                                       #
# @version  1.0.0                                                                 #
#---------------------------------------------------------------------------------#
# Preforms Financial Analysis on revenue from data input file                     #
#                                                                                 #
# Modification History                                                            #
#                                                                                 #
# Date        Name             Description                                        #
# ----------  -----------      ----------------------------------                 #
# 2018/07/08  (chris)          Original script                                    #
#                                                                                 #
###################################################################################
'''

## Imports
import re, os, csv

# importing mean()
from statistics import mean

## Module Constants
csv_file = 'budget_data.csv'
txt_file = 'budget_data_report.txt'

current_path = os.path.dirname(os.path.abspath(__file__))
input_file  = '{}/Resources/{}'.format(current_path, csv_file)
output_file = '{}/Resources/{}'.format(current_path, txt_file)

field_names = ('Date','Revenue')

## metric points
total_months = 0
total_revenue = 0
average_change = 0

revenue_items = []
revenue_dates = []

## Main functionality

''' open the data file for read only; "U" compestates
    for line endings automatically; Windows/Mac/Unix files

'''
with open(input_file, 'rU') as csvfile:
    rows = csv.DictReader(csvfile, field_names, delimiter=',')
    next(rows)

    for row in rows:
        revenue_dates.append(row['Date'])
        revenue_items.append(int(row['Revenue']))
        total_revenue += int(row['Revenue'])
        total_months += 1
        
    csvfile.close()

''' calculate
    (do math)
'''
average_change    = mean(revenue_items)
greatest_increase = max(revenue_items)
greatest_decrease = min(revenue_items)

greatest_increase_date = revenue_dates[revenue_items.index(greatest_increase)]
greatest_decrease_date = revenue_dates[revenue_items.index(greatest_decrease)]


''' prepare and format output
    to display and write a file
'''
output = (
        '------------------------------------------\n'
        'Financial Analysis\n'
        '------------------------------------------\n'
        'Total Months                :\t{:10}\n'
        'Total Revenue               :\t{:10,.0f}\n'
        'Average Change              :\t{:10,.0f}\n'
        'Greatest Increase in {} :\t{:10,.0f}\n'
        'Greatest Decrease in {} :\t{:10,.0f}\n\n'.format(total_months, total_revenue, average_change,
                                                    greatest_increase_date, greatest_increase,
                                                    greatest_decrease_date, greatest_decrease))

''' write to file
'''
with open(output_file, 'w') as text:
    text.write(output)
    
    text.close()

''' display to screen
'''
print(output)
