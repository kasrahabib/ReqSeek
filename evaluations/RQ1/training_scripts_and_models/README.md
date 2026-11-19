## Model Training Scripts

The following notebooks are used to train the selected candidate models using **10-fold cross-validation**:

- [`10_fold_training_all_mini_l6v2.ipynb`](./10_fold_training_all_mini_l6v2.ipynb)  
- [`10_fold_training_bert_base_cased.ipynb`](./10_fold_training_bert_base_cased.ipynb)
- [`10_kfold_training_gpt2.ipynb`](./10_kfold_training_gpt2.ipynb)
- [`10_kfold_training_roberta_base.ipynb`](./10_kfold_training_roberta_base.ipynb)


The notebook below is used to train the **final ReqSeek model** using a fixed **80/20 train–test split**, based on the benchmarking results. The selected model is initialized **from its original pre-training weights (trained from scratch for fine-tuning)**:
- [`ReqSeek_training.ipynb`](./ReqSeek_training.ipynb)


