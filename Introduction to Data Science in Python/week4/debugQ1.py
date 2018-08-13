import re
import pandas as pd
import numpy as np
#pd.set_option('display.max_colwidth',10000000,'max_rows',10000000)

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    raw = pd.read_table(r"university_towns.txt",header = None)
    list = pd.DataFrame(columns = ['State','RegionName'])
    count = 0
    for i in range(len(raw)):
        if '[edit]' in raw.values[i][0]:
            State = raw.values[i][0].split('[')[0].rstrip()
        else:
            Region = raw.values[i][0].split('(')[0].rstrip()
            list.loc[count] = {'State': State, 'RegionName': Region}
            count += 1    
    return list



# list of unique states
stateStr = """
Ohio, Kentucky, American Samoa, Nevada, Wyoming
,National, Alabama, Maryland, Alaska, Utah
,Oregon, Montana, Illinois, Tennessee, District of Columbia
,Vermont, Idaho, Arkansas, Maine, Washington
,Hawaii, Wisconsin, Michigan, Indiana, New Jersey
,Arizona, Guam, Mississippi, Puerto Rico, North Carolina
,Texas, South Dakota, Northern Mariana Islands, Iowa, Missouri
,Connecticut, West Virginia, South Carolina, Louisiana, Kansas
,New York, Nebraska, Oklahoma, Florida, California
,Colorado, Pennsylvania, Delaware, New Mexico, Rhode Island
,Minnesota, Virgin Islands, New Hampshire, Massachusetts, Georgia
,North Dakota, Virginia
"""
#list of regionName entries string length
regNmLenStr = """
06,08,12,10,10,04,10,08,09,09,05,06,11,06,12,09,08,10,12,06,
06,06,08,05,09,06,05,06,10,28,06,06,09,06,08,09,10,35,09,15,
13,10,07,21,08,07,07,07,12,06,14,07,08,16,09,10,11,09,10,06,
11,05,06,09,10,12,06,06,11,07,08,13,07,11,05,06,06,07,10,08,
11,08,13,12,06,04,08,10,08,07,12,05,06,09,07,10,16,10,06,12,
08,07,06,06,06,11,14,11,07,06,06,12,08,10,11,06,10,14,04,11,
18,07,07,08,09,06,13,11,12,10,07,12,07,04,08,09,09,13,08,10,
16,09,10,08,06,08,12,07,11,09,07,09,06,12,06,09,07,10,09,10,
09,06,15,05,10,09,11,12,10,10,09,13,06,09,11,06,11,09,13,37,
06,13,06,09,49,07,11,12,09,11,11,07,12,10,06,06,09,04,09,15,
10,12,05,09,08,09,09,07,14,06,07,16,12,09,07,09,06,32,07,08,
08,06,10,36,09,10,09,06,09,11,09,06,10,07,14,08,07,06,10,09,
05,11,07,06,08,07,05,07,07,04,06,05,09,04,25,06,07,08,05,08,
06,05,11,09,07,07,06,13,09,05,16,05,10,09,08,11,06,06,06,10,
09,07,06,07,10,05,08,07,06,08,06,30,09,07,06,11,07,12,08,09,
16,12,11,08,06,04,10,10,15,05,11,11,09,08,06,04,10,10,07,09,
11,08,26,07,13,05,11,03,08,07,06,05,08,13,10,08,08,08,07,07,
09,05,04,11,11,07,06,10,11,03,04,06,06,08,08,06,10,09,05,11,
07,09,06,12,13,09,10,11,08,07,07,08,09,10,08,10,08,56,07,12,
07,16,08,04,10,10,10,10,07,09,08,09,09,10,07,09,09,09,12,14,
10,29,19,07,11,12,13,13,09,10,12,12,12,08,10,07,10,07,07,08,
08,08,09,10,09,11,09,07,09,10,11,11,10,09,09,12,09,06,08,07,
12,09,07,07,06,06,08,06,15,08,06,06,10,10,10,07,05,10,07,11,
09,12,10,12,04,10,05,05,04,14,07,10,09,07,11,10,10,10,11,15,
09,14,12,09,09,07,12,04,10,10,06,10,07,28,06,10,08,09,10,10,
10,13,12,08,10,09,09,07,09,09,07,11,11,13,08,10,07
"""

df = get_list_of_university_towns()

cols = ["State", "RegionName"]

print('Shape test: ', "Passed" if df.shape ==
      (517, 2) else 'Failed')
'''
print('Index test: ',
      "Passed" if df.index.tolist() == list(range(517))
      else 'Failed')
'''
print('Column test: ',
      "Passed" if df.columns.tolist() == cols else 'Failed')
print('\\n test: ',
      "Failed" if any(df[cols[0]].str.contains(
          '\n')) or any(df[cols[1]].str.contains('\n'))
      else 'Passed')
print('Trailing whitespace test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\s+$')) or any(df[cols[1]].str.contains(
              '\s+$'))
      else 'Passed')
print('"(" test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\(')) or any(df[cols[1]].str.contains(
              '\('))
      else 'Passed')
print('"[" test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\[')) or any(df[cols[1]].str.contains(
              '\]'))
      else 'Passed')

states_vlist = [st.strip() for st in stateStr.split(',')]

mismatchedStates = df[~df['State'].isin(
    states_vlist)].loc[:, 'State'].unique()
print('State test: ', "Passed" if len(
    mismatchedStates) == 0 else "Failed")
if len(mismatchedStates) > 0:
    print()
    print('The following states failed the equality test:')
    print()
    print('\n'.join(mismatchedStates))

df['expected_length'] = [int(s.strip())
                         for s in regNmLenStr.split(',')
                         if s.strip().isdigit()]
regDiff = df[df['RegionName'].str.len() != df['expected_length']].loc[
    :, ['RegionName', 'expected_length']]
regDiff['actual_length'] = regDiff['RegionName'].str.len()
print('RegionName test: ', "Passed" if len(regDiff) ==
      0 else ' \nMismatching regionNames\n {}'.format(regDiff))

regDiff.to_excel('output.xlsx')
