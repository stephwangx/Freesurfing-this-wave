import pandas as pd
df = pd.read_csv('finaledit.csv') #change 
df_early = df.filter(regex='(precuneus|posteriorcingulate|isthmuscingulate|insula|medialorbitofrontal|lateralorbitofrontal)')
df_ctx_suvr = df_early.filter(regex='SUVR')
reg_sums = df_ctx_suvr.mean(axis=1)
print (reg_sums)
df_gsuvr = pd.DataFrame(reg_sums.values, columns=['earlySUVR'], index=df.subject_id)

df_gsuvr.to_csv('earlysuvr_Freesurfer.csv')
