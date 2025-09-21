# Protein Subcellular Localization Prediction

This project implements multiple machine learning approaches for predicting protein subcellular localization using various feature extraction methods and model architectures.

## Project Structure

```
├── Features/
│   ├── Actual/                # Features extracted from actual dataset
│   │   ├── HMM/              # Hidden Markov Model features
│   │   └── PSSM/             # Position-Specific Scoring Matrix features
│   └── Independent/           # Features extracted from independent dataset
│       ├── HMM/              # HMM features for independent testing
│       └── PSSM/             # PSSM features for independent testing
├── ML Models/
│   ├── HMM Models/           # Machine Learning models using HMM features
│   └── PSSM Models/          # Machine Learning models using PSSM features
├── Protein_Bert/             # ProteinBERT implementation and results
├── Dynamic_Thresholding/     # Dynamic threshold implementation
├── features.py               # Feature extraction implementation
├── parse_files.py            # HMM file parsing utilities
├── multiLabelMetrics.py      # Evaluation metrics implementation
├── Neural_Network.ipynb      # Neural network implementation and training
└── Data_Analysis.ipynb       # Data analysis and visualization
```

## Features

### Feature Extraction Methods

1. **Hidden Markov Model (HMM)**
   - Implementation in `parse_files.py` for parsing HMM files
   - Two types of features:
     - MatMul: Matrix multiplication based features
     - PseHMM: Pseudo HMM features
   
2. **Position-Specific Scoring Matrix (PSSM)**
   - Similar feature types as HMM:
     - MatMul: Matrix multiplication based features
     - PsePSSM: Pseudo PSSM features

### Machine Learning Models

1. **Traditional ML Models**
   - Random Forest (RF)
   - K-Nearest Neighbors (KNN)
   - Decision Trees (DT)
   - Each model implemented for both HMM and PSSM features

2. **Neural Network**
   - Implementation in `Neural_Network.ipynb`
   - Uses TensorFlow/Keras
   - Multiple layers with dropout for regularization
   - Handles multi-label classification

3. **ProteinBERT**
   - Advanced transformer-based model for protein sequences
   - Located in `Protein_Bert/` directory
   - Includes both training and inference implementations
   - Support Vector Machine (SVM) implementations for both actual and independent datasets

## Evaluation

The project includes comprehensive evaluation metrics implemented in `multiLabelMetrics.py`:
- Strict accuracy metrics
- Relaxed accuracy metrics
- Precision, Recall, and F1 scores
- Support for both binary and multi-label classification

## Dynamic Thresholding

The `Dynamic_Thresholding/` directory contains implementations for:
- Multiple threshold selection strategies
- Testing outputs for different thresholding approaches
- Performance comparison across different methods

## Setup and Usage

1. **Environment Setup**
   - Python 3.x required
   - Key dependencies:
     - TensorFlow
     - Pandas
     - NumPy
     - Scikit-learn
     - h5py

2. **Feature Extraction**
   ```python
   python features.py  # For feature extraction
   python parse_files.py  # For HMM file parsing
   ```

3. **Model Training**
   - For Neural Networks: Run `Neural_Network.ipynb`
   - For ProteinBERT: Use notebooks in `Protein_Bert/` directory
   - For traditional ML models: Use respective notebooks in `ML Models/` directory

4. **Evaluation**
   - Use `multiLabelMetrics.py` for performance evaluation
   - Results are stored in `ANN_Results.xlsx`

## Results

Results and model comparisons are stored in:
- `ANN_Results.xlsx`: Contains performance metrics for different models
- Individual model notebooks contain detailed performance analysis
- Separate evaluation metrics for actual and independent datasets

## Data Organization

- Features are organized into Actual and Independent datasets
- Each feature type (HMM/PSSM) has corresponding training and testing sets
- Results maintain the same organization structure for consistency

## Note

This project implements multiple approaches for protein subcellular localization prediction, allowing comparison between traditional ML methods, neural networks, and transformer-based approaches. The modular structure enables easy extension and modification of different components.