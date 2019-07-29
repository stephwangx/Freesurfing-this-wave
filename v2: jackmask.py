
import pandas as pd
df = pd.read_csv('final.csv')
#jack mask regions
df_jack = df.filter(regex='(sup|pr|temp|par|cing|fusi|ros|entor|caudal|cent|hip)')
print(df_jack)

df_ctx_suvr = df_jack.filter(regex='SUVR')
df_ctx_vm = df_jack.filter(regex='VM')

# dot array
df_dot = pd.DataFrame(df_ctx_suvr.values * df_ctx_vm.values)

# vol sums
reg_sums = df_ctx_vm.sum(axis=1)

# global suvr
gsuvr = df_dot.sum(axis=1) / reg_sums

# dataframe w subjs
df_gsuvr = pd.DataFrame(gsuvr.values, columns=['GSUVR'], index=df.subject_id)
print(gsuvr)
df_ctx_suvr = df_jack.filter(regex='SUVR')
df_ctx_vm = df_jack.filter(regex='VM')

# dot array
df_dot = pd.DataFrame(df_ctx_suvr.values * df_ctx_vm.values)

# vol sums
reg_sums = df_ctx_vm.sum(axis=1)

# global suvr
gsuvr = df_dot.sum(axis=1) / reg_sums

# dataframe w subjs
df_gsuvr = pd.DataFrame(gsuvr.values, columns=['GSUVR'], index=df.subject_id)
print(gsuvr)

#create file for predicted GSUVR
df_gsuvr.to_csv('global_suvr_Freesurfer.csv') #change the name

d = df_gsuvr
df = pd.DataFrame(data=d)

#converting values to binary according to the cutpoint
df['GSUVR'] = df.apply(lambda x: "1" if x['GSUVR'] > 1.18 else "0", axis = 1)
print(df['GSUVR']) #optional
df.to_csv('y_pred_Freesurfer.csv', index=True, header=True) #change name for analysis you want to run 
