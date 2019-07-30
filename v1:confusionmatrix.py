from sklearn.metrics import confusion_matrix
import pandas as pd
d = pd.read_csv('Mitnec_Minc_y_true.csv') #change accordingly
d2 = pd.read_csv('y_pred_M0.83.csv')#change accordingly
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)
x = df["Amyloid_Clinical_Reads"].tolist() #change accordingly
y = df2["MNI_Pipeline_Global_SUVr"].tolist()#change accordingly
df_confusion = confusion_matrix(x, y)
print (df_confusion)

# Split the data into a training set and a test set
def plot_confusion_matrix(x, y,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
  
    if not title:
        if normalize:
            title = 'Normalized confusion matrix' #change accordingly
        else:
            title = 'Confusion matrix, without normalization' #change accordingly

    # Compute confusion matrix
    cm = confusion_matrix(x, y)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           title=title,
           ylabel='True label', #change accordingly
           xlabel='Predicted label') #change accordingly

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plot_confusion_matrix(x, y,
                      title='Confusion matrix, without normalization') #change accordingly


# Plot normalized confusion matrix
plot_confusion_matrix(x, y, normalize=True,
                      title='Normalized confusion matrix') #change accordingly

plt.show()
