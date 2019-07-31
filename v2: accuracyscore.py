import pandas as pd
from sklearn.metrics import accuracy_score
d = pd.read_csv('Mitnec_Minc_y_true.csv')
d2 = pd.read_csv('y_pred_M0.83.csv')
y = ('y_pred_M0.83.csv')
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)
df_true = df.filter(regex='Amy')
df2_pred = df2.filter(regex='MNI')
a=accuracy_score(df_true, df2_pred)
rat='%.2f' % a
print(rat)

b= accuracy_score(df_true, df2_pred, normalize=False)
num='%.2f' % b
print(num)
new=[rat, num]

import csv
row = [y, rat, num]
head = ['Cut','Accuracy Ratio', 'Accuracy Number'] #silence this row if it's not the first time
with open('FreeAR.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(head) #silence this row if it's not the first time
    writer.writerow(row)
    
csvFile.close()
