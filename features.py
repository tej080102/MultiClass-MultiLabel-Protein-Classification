import os
import numpy as np
import pandas as pd

# Directories
base_dir = r'/raid/home/tejus/MLMC/Actual_data/HMM/Test_hmm_parsed'
features_dir = r'/raid/home/tejus/MLMC/Actual_data/HMM/Train_hmm_features'
matmul_dir = r'/raid/home/tejus/MLMC/Actual_data/HMM/MatMul'

os.makedirs(features_dir, exist_ok=True)
os.makedirs(matmul_dir, exist_ok=True)

# File availability
files = set(os.listdir(base_dir))
d = {i: int(f"{i}.csv" in files) for i in range(28304)}

def feat_ext(df):
    """Extract 320 pseudo-features from dataframe."""
    V = []
    # Means of first 20 columns
    V.extend(df.iloc[:, :20].mean().values)
    N = len(df)
    for X in range(1, min(16, N)):  # skip invalid lags
        diff = df.iloc[:-X, :20].values - df.iloc[X:, :20].values
        sq_mean = (diff**2).mean(axis=0)
        V.extend(sq_mean)
    while len(V) < 320:
        V.append(np.nan)
    return np.array(V)

# Main loop
for idx in range(1, 28304):
    fname = f"{idx}.csv"
    path = os.path.join(base_dir, fname)

    if d[idx] == 0:
        # Missing file → NaN features, skip matmul
        np.full(320, np.nan).tofile(f"{features_dir}/{idx}.csv", sep=',')
        continue

    try:
        df = pd.read_csv(path, header=None)
        matrix = df.values

        # -------- 1. Features --------
        try:
            x = feat_ext(df)
            x.tofile(f"{features_dir}/{idx}.csv", sep=',')
        except ZeroDivisionError:
            np.full(320, np.nan).tofile(f"{features_dir}/{idx}.csv", sep=',')

        # -------- 2. MatMul --------
        try:
            result = matrix.T @ matrix
            np.savetxt(f"{matmul_dir}/{idx}.csv", result, delimiter=',')
        except Exception as e:
            print(f"[MatMul error] {idx}: {e}")

        print(f"Processed {idx}: Features {len(x)}, MatMul {result.shape}")

    except Exception as e:
        print(f"[General error] {idx}: {e}")
        np.full(320, np.nan).tofile(f"{features_dir}/{idx}.csv", sep=',')

print("\n✅ Processing complete! Features written first, then MatMul.")