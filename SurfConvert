import sys  # importing system lib/mod
import glob
import os
import pandas as pd

temp_list = [] # creating somewhere to store the current

# what we know
'''
- the dir we're working from
- the file name were looking for
'''
#python3 1step_1.py ./003\*

# find all gtm files in the first argument
directory = sys.argv[1]
gtm_files = glob.glob(os.path.join(directory, '**', 'gtm.stats.dat'), recursive=True)
print(gtm_files)
# create variable for all subject data
gtm_subject_data = []

# for each gtm stats file
for gtm_file in gtm_files:
    # find the session name it belongs to
    session_dir = os.path.dirname(gtm_file)
    session_name = os.path.basename(session_dir)
    # do the stuff we need to
    with open(gtm_file, 'r') as infile:
        for line in infile:  # infile-reading file
            line = line.split()  # splitting all lines in reading file
            line = [session_name, line[2], line[5], line[6]]  # now your lines, instead of a big string is a list. now taking the columns u want
            line = ','.join(line) + '\n'
            temp_list.append(line)  # appending this to list
            gtm_subject_data.append(line)
    # store the results in a new file
    with open(os.path.join(session_dir, 'gtm.stats.csv'), 'w') as outfile: # (w= opening file for writing) creates a new file
        outfile.write("subject_id,ROI,VM,SUVR\n")
        outfile.writelines(temp_list)

''' Step 2:
    Combine all csv files into one csv
'''
with open('combined.csv', 'w') as combined_file:  # write contents of gtm subject data to file
    combined_file.write("subject_id,ROI,VM,SUVR\n")
    combined_file.writelines(gtm_subject_data)
df = pd.read_csv("combined.csv")
df.head()

# pivot dataframe
df_pivot = pd.pivot_table(df,index=["subject_id"], columns=["ROI"], values=["VM","SUVR"])
df_pivot

#OPTIONAL CODE TO CHECK: print(df_pivot.columns)

# set column names to be combination of heirarchical columns (i.e. SUVR, VM)
df_pivot.columns = ['_'.join(col).strip() for col in df_pivot.columns.values ]
df_pivot
print(df_pivot)

df = pd.DataFrame(df_pivot)
df.to_csv('final.csv', index=True, header=True)
print(df)
