import numpy as np
def label_generator(predictions):
    #thresholds =  np.mean(predictions, axis=0)
    thresholds = np.max(predictions, axis=0)
    thresholds=0.1*thresholds
    class_labels = []
    for preds in predictions:
        preds = np.array(preds)
        
        temp_labels = np.where(preds > thresholds, 1, 0)
        class_labels.append(temp_labels)
    return np.array(class_labels)