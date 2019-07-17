import pandas as pd
df = pd.read_csv('final.csv')

# get jack mask regions

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
df_gsuvr.to_csv('global_suvr.csv')
