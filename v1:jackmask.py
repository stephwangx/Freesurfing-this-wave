#CoNvErT
import pandas as pd
df = pd.read_csv('final.csv')

# get only cortical regions
df_ctx = df.filter(regex='ctx')
df_ctx_suvr = df_ctx.filter(regex='SUVR')
df_ctx_vm = df_ctx.filter(regex='VM')
# dot array
df_dot = pd.DataFrame(df_ctx_suvr.values * df_ctx_vm.values)
# vol sums
reg_sums = df_ctx_vm.sum(axis=1)
# global suvr
gsuvr = df_dot.sum(axis=1) / reg_sums
# dataframe w subjs
df_gsuvr = pd.DataFrame(gsuvr.values, columns=['GSUVR'], index=df.subject_id)
# save df
df_gsuvr.to_csv(global_suvr.csv')
#positive/negative
import pandas as pd

d = pd.read_csv('CLINICAL_RATING.csv')
df = pd.DataFrame(data=d)
df['KZ'] = df.apply(lambda x: "1" if x['KZ'] == "Positive" else "0", axis = 1)
print(df['KZ'])
df.to_csv('y_true.csv', index=True, header=True)
print(df)

#according to cut points
import pandas as pd

d = pd.read_csv('global_suvr.csv')
df = pd.DataFrame(data=d)
df['GSUVR'] = df.apply(lambda x: "1" if x['GSUVR'] > 1.18 else "0", axis = 1)
print(df['GSUVR'])
df.to_csv('y_pred.csv', index=True, header=True)
print(df)

#in jupyter 
import pandas as pd
from sklearn.metrics import accuracy_score
d = pd.read_csv('true.csv')
d2 = pd.read_csv('pred.csv')
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)
df_true = df.filter(regex='y_true')
df2_pred = df2.filter(regex='y_pred')
y_pred = df2_pred
y_true = df_true
rat=accuracy_score(y_true, y_pred)
num=accuracy_score(y_true, y_pred, normalize=False)
print(rat)
print(num)
