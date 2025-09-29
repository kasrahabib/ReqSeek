Labeling Inconsistency Experiments with RoBERTa for RQ2

This repository provides training scripts and related resources for reproducing experiments on the impact of label inconsistency levels in requirements classification using the RoBERTa-base model.

## Training Scripts for Simulated Labeling Inconsistency

- [`training_0_inconsistency_roberta_base.ipynb`](./training_0_inconsistency_roberta_base.ipynb)  
  Training script for the baseline model trained on a dataset with **0% label inconsistency**.

- [`training_10_inconsistency_roberta_base.ipynb`](./training_10_inconsistency_roberta_base.ipynb)  
  Training script for the model trained on a dataset with **10% label inconsistency**.

- [`training_20_inconsistency_roberta_base.ipynb`](./training_20_inconsistency_roberta_base.ipynb)  
  Training script for the model trained on a dataset with **20% label inconsistency**.

- [`training_30_inconsistency_roberta_base.ipynb`](./training_30_inconsistency_roberta_base.ipynb)  
  Training script for the model trained on a dataset with **30% label inconsistency**.

- [`training_40_inconsistency_roberta_base.ipynb`](./training_40_inconsistency_roberta_base.ipynb)  
  Training script for the model trained on a dataset with **40% label inconsistency**.

## Model Availability

The `models_with_inconsistency_levels/` directory is intentionally left empty, as the model checkpoints (total size: **138.03 GB**) are not included in this replication package due to GitHub size constraints. All necessary scripts for training, evaluation, and reproduction of results are provided.

While all models are based on publicly available open-source weights, the trained checkpoints may only be shared via private channels that could compromise the double-blind review process.

We will make the models available through appropriate means after the review period.

We appreciate your understanding.
