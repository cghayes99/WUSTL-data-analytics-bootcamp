#!/opt/anaconda3/bin/python

'''
###################################################################################
# @script   PyPoll  main.py                                                       #
# @version  1.0.0                                                                 #
#---------------------------------------------------------------------------------#
# Tallys Election Results and create results from data input file                 #
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
csv_file = 'election_data.csv'
txt_file = 'election_results.txt'

current_path = os.path.dirname(os.path.abspath(__file__))
input_file  = '{}/Resources/{}'.format(current_path, csv_file)
output_file = '{}/Resources/{}'.format(current_path, txt_file)

field_names = ('Voter ID','County','Candidate')

## metric points
total_votes = 0
vote_result = {}
vote_count = []

candidates = []
candidates_set = set()
candidates_uniq = []

election_results = ''

## Main functionality

''' open the data file for read only; "U" compestates
    for line endings automatically; Windows/Mac/Unix files

'''
with open(input_file, 'rU') as csvfile:
    rows = csv.DictReader(csvfile, field_names, delimiter=',')
    next(rows)

    for row in rows:
        candidates.append(row['Candidate'])
        candidates_set.add(row['Candidate'])
        total_votes += 1
    csvfile.close()

''' calculate
    (do math)
'''
for candidate in candidates_set:
    candidates_uniq.append(candidate)
    candidate_count = candidates.count(candidate)
    vote_count.append(candidate_count)
    
    percent = (candidate_count / total_votes) * 100
    vote_result[candidate] = {'percent' : round(percent, 2), 'count' : candidate_count}

winner = candidates_uniq[vote_count.index(max(vote_count))]

''' prepare and format output
    to display and write a file
'''
for candidate in candidates_set:
    election_results += '{:10}\t: {:10.2f}%\t{:10,.0f}\n'.format(candidate, vote_result[candidate]['percent'], vote_result[candidate]['count'])

output = (
        '------------------------------------------\n'
        'Election Results\n'
        '------------------------------------------\n'
        'Total Votes     :{:25,.0f}\n'
        '------------------------------------------\n'
        '{}'
        '------------------------------------------\n'
        'Winner          :{:^25}\n'
        '------------------------------------------\n'.format(total_votes, election_results, winner))

''' write to file
'''
with open(output_file, 'w') as text:
    text.write(output)
    
    text.close()

''' display to screen
'''
print(output)
