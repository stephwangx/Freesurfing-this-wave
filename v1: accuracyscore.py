import pandas as pd
import csv
from sklearn.metrics import accuracy_score

#accuracy score
d = pd.read_csv('Mitnec_Freesurfer_y_true.csv')
d2 = pd.read_csv('Mitnec_Freesurfer_y_pred.csv')
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)
df_true = df.filter(regex='Amy')
df2_pred = df2.filter(regex='GSUVR')
a=accuracy_score(df_true, df2_pred)

#numpy.float64 to string
rat='%.2f' % a
print(rat)

#numpy.float64 to string 
b= accuracy_score(df_true, df2_pred, normalize=False)
num='%.2f' % b
print(num)

#create list for the results
new=[('accuracy ratio\n'+ rat + '\n','number of corrects\n'+ num + '\n')]
print(new)
csvData = new

#results into csv file
with open('accuracyscore.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()
