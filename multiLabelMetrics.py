import numpy as np
class accuracy:
    def __init__(self,predictions,actual):
        self.predictions=predictions
        self.actual=actual

    def strictAccuracy(self):
        my_preds=[]
        if self.predictions.shape!=self.actual.shape:
            print('Shapes of Predictions and Actual do not match')
            return None
        else:
            for i in range(self.predictions.shape[0]):
                count = 0
                for j in range(self.predictions.shape[1]):
                    if self.predictions[i][j]==self.actual[i][j]:
                        count+=1
                my_preds.append(count//self.predictions.shape[1])
            my_preds=np.array(my_preds)
            return np.mean(my_preds)*100

    def relaxedAccuracy(self):
        my_preds=[]
        if self.predictions.shape!=self.actual.shape:
            print('Shapes of Predictions and Actual do not match')
            return None
        else:
            for i in range(self.predictions.shape[0]):
                count = 0
                for j in range(self.predictions.shape[1]):
                    if self.predictions[i][j]==self.actual[i][j]:
                        count+=1
                my_preds.append(count/self.predictions.shape[1])
            my_preds=np.array(my_preds)
            return np.mean(my_preds)*100
