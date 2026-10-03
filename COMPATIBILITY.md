# FraudMesh Environment Compatibility

## System

- OS: Windows
- Python: 3.13.1
- Compute: CPU
- CUDA: Not available

## Core ML Stack

- PyTorch: 2.14.1+cpu
- PyTorch Geometric: 2.8.0.post1
- Flower: 1.39.0
- Opacus: 1.6.0

## Data / Experiment Stack

- Polars:
- Pandas:
- NumPy:
- PyArrow:
- Pandera:
- Hydra:
- OmegaConf:
- MLflow:
- DVC:

## ML / Baselines

- Scikit-learn:
- LightGBM:
- XGBoost:

## Serving

- FastAPI:
- Uvicorn:

## Notes

Development is currently CPU-based.

Large experiments may be executed later on college lab hardware, Kaggle, Colab, or cloud infrastructure.

PyTorch, PyTorch Geometric, Flower, and Opacus versions should not be changed without testing and recording a new compatible environment.