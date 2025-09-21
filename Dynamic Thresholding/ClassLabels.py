import numpy as np
def label_generator(predictions):
    class_labels=[]
    for preds in predictions:
        preds = np.array(preds)
        temp_labels=np.round(preds)
        if np.all(temp_labels==0):
            temp_labels[np.argmax(preds)]=1
        class_labels.append(temp_labels)
    return np.array(class_labels)
