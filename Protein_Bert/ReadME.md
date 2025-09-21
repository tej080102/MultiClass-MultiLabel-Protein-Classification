# Protein Subcellular Localization using ProtBERT

This project implements a multi-label protein subcellular localization prediction system using ProtBERT embeddings with various machine learning approaches.

## Project Files

### Core Files
- `Actual_train.ipynb`: Extracts ProtBERT embeddings from protein sequences
- `TrainingProtbert.ipynb`: Main model training implementation
- `protein_bert.h5`: Trained model weights

### Data Files
- `actualtrainprotbertnew.csv`: Training set with ProtBERT features
- `actualtestprotbert_new.csv`: Test set with ProtBERT features
- `indetrainprotbertnew.csv`: Independent training set features
- `indetestprotbertnew.csv`: Independent test set features

### Model Implementation Files
- `SVC_protbert_actual.ipynb`: SVM implementation for actual dataset
- `SVC_protbert_inde.ipynb`: SVM implementation for independent dataset
- `DT_combined.ipynb`: Decision Tree implementation
- `TestingCL1outputs.ipynb`: Testing and evaluation notebook

### Utility Files
- `ClassLabels1.py`: Label generation and processing utilities
- `multiLabelMetrics.py`: Custom evaluation metrics implementation
  - Strict Accuracy
  - Relaxed Accuracy

## Subcellular Locations Predicted
1. Membrane
2. Cytoplasm
3. Nucleus
4. Extracellular
5. Cell membrane
6. Mitochondrion
7. Plastid
8. Endoplasmic reticulum
9. Lysosome/Vacuole
10. Golgi apparatus
11. Peroxisome

## Data Flow
1. Raw protein sequences → ProtBERT embeddings (1024-dimensional features)
2. Feature extraction using `Actual_train.ipynb`
3. Data split into training and test sets
4. Model training using different approaches:
   - Neural Network (TrainingProtbert.ipynb)
   - SVM (SVC_protbert_*.ipynb)
   - Decision Tree (DT_combined.ipynb)
5. Evaluation using custom metrics in `multiLabelMetrics.py`

## Dependencies
- Python 3.x
- PyTorch
- Transformers (Hugging Face)
- TensorFlow/Keras
- Scikit-learn
- Pandas
- NumPy
- CUDA (for GPU acceleration)

## Model Architecture
The main ProtBERT model uses:
- Input: 1024-dimensional protein embeddings
- Binary cross-entropy loss
- Early stopping with patience=20
- Batch size of 256
- Custom thresholding for multi-label prediction

## Evaluation Metrics
1. **Strict Accuracy**: Requires all labels to match exactly
2. **Relaxed Accuracy**: Proportional match of labels

## Usage
1. Extract features:
   ```python
   # Run Actual_train.ipynb for feature extraction
   ```

2. Train models:
   ```python
   # Run TrainingProtbert.ipynb for neural network
   # Run SVC_protbert_actual.ipynb for SVM
   # Run DT_combined.ipynb for Decision Tree
   ```

3. Evaluate:
   ```python
   # Run TestingCL1outputs.ipynb for comprehensive evaluation
   ```
