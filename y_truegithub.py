import pandas as pd


d = pd.read_csv('CLINICAL_RATING.csv') #change accordingly
df = pd.DataFrame(data=d)
df['KZ'] = df.apply(lambda x: "1" if x['KZ'] == "Positive" else "0", axis = 1) #change accordingly
print(df['KZ']) #change accordingly
df.to_csv('y_true.csv', index=True, header=True) #change accordingly
print(df)
