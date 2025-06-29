import numpy as np 
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import random

def poison_data(X,y, poison_fraction=0.05, random_seed=42):
    np.random.seed(random_seed)
    n_samples = len(y)
    n_poison = int(poison_fraction * n_samples)
    poison_indices = np.random.choice(n_samples, n_poison, replace=False)
    y_poisoned = y.copy()

    classes = np.unique(y)
    for idx in poison_indices:
        current = y[idx]
        y_poisoned[idx] = classes[(np.where(classes == current)[0][0] + 1) % len(classes)]
    return y_poisoned

    
def main():
  X, y = load_iris(return_X_y=True)

  # Train clean model
  clf_clean = LogisticRegression(max_iter=200)
  clf_clean.fit(X, y)
  preds_clean = clf_clean.predict(X)
  acc_clean = accuracy_score(y, preds_clean)

  # Train poisoned model
  y_poisoned = poison_data(X, y, poison_fraction=0.1)
  clf_pois = LogisticRegression(max_iter=200)
  clf_pois.fit(X, y_poisoned)
  preds_pois = clf_pois.predict(X)
  acc_pois = accuracy_score(y, y)

  print(f"Clean model accuracy: {acc_clean:.3f}")
  print(f"Poisoned model accuracy on true labels: {acc_pois:.3f}")

if __name__ == "__main__":
  main()


