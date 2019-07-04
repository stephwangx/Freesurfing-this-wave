#UPDATE: not using, need to use freesurver GLOBSUVR formula
#steps
#Import final
#run formula for each subject: (GMVM)(ROISUVR)+....(for every region)/sum of(GMVM)
#put information on new line :)
#header: GlobalSUVr



import pandas as pd
import csv
d = pd.read_csv('final.csv')
df = pd.DataFrame(data=d)
suvr = df.iloc[:,
       list(range(34,103))].mean(axis=1)
df["FS_Pipeline_Global_SUVRr"] = suvr
df.to_csv('final.csv', index=True, header=True)
print(df)
