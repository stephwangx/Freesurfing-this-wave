from sklearn.metrics import confusion_matrix
import pandas as pd
d = pd.read_csv('Mitnec_Minc_y_true.csv')
d2 = pd.read_csv('y_pred_M0.83.csv')
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)
x = df["Amyloid_Clinical_Reads"].tolist()
y = df2["MNI_Pipeline_Global_SUVr"].tolist()
df_confusion = confusion_matrix(x, y)
print (df_confusion)
