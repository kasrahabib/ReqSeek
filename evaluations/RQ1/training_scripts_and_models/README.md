## Model Availability

The `mdoels/` directory is intentionally left empty, as the model checkpoints (total size: **~30 GB**) are not included in this replication package due to GitHub size constraints. All necessary scripts for training, evaluation, and reproduction of results are provided.

While all models are based on publicly available open-source weights, the trained checkpoints may only be shared via private channels that could compromise the double-blind review process. 

We will make the models available through appropriate means after the review period.

We appreciate your understanding.


## Model Training Scripts

The following notebooks are used to train the selected candidate models using **10-fold cross-validation**:

- [`10_fold_training_all_mini_l6v2.ipynb`](./10_fold_training_all_mini_l6v2.ipynb)  
- [`10_fold_training_bert_base_cased.ipynb`](./10_fold_training_bert_base_cased.ipynb)
- [`10_kfold_training_gpt2.ipynb`](./10_kfold_training_gpt2.ipynb)
- [`10_kfold_training_roberta_base.ipynb`](./10_kfold_training_roberta_base.ipynb)


The notebook below is used to train the **final ReqSeek model** using a fixed **80/20 train–test split**, based on the benchmarking results. The selected model is initialized **from its original pre-training weights (trained from scratch for fine-tuning)**:
- [`ReqSeek_training.ipynb`](./ReqSeek_training.ipynb)


