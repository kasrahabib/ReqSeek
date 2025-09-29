---
license: mit
base_model: FacebookAI/roberta-base
tags:
- generated_from_keras_callback
model-index:
- name: kasrahabib/roberta-base-finetuned-iso29148-req-detector
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# kasrahabib/roberta-base-finetuned-iso29148-req-detector

This model is a fine-tuned version of [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0257
- Validation Loss: 0.4146
- Epoch: 29

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'weight_decay': None, 'clipnorm': None, 'global_clipnorm': None, 'clipvalue': None, 'use_ema': False, 'ema_momentum': 0.99, 'ema_overwrite_frequency': None, 'jit_compile': True, 'is_legacy_optimizer': False, 'learning_rate': {'module': 'keras.optimizers.schedules', 'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 3570, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, 'registered_name': None}, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 2.4054     | 1.3529          | 0     |
| 1.0479     | 0.6862          | 1     |
| 0.6251     | 0.5206          | 2     |
| 0.4259     | 0.4428          | 3     |
| 0.2732     | 0.4007          | 4     |
| 0.1769     | 0.3710          | 5     |
| 0.1238     | 0.3657          | 6     |
| 0.0966     | 0.3575          | 7     |
| 0.0893     | 0.3619          | 8     |
| 0.0800     | 0.3985          | 9     |
| 0.0624     | 0.3854          | 10    |
| 0.0630     | 0.3802          | 11    |
| 0.0596     | 0.3671          | 12    |
| 0.0492     | 0.4555          | 13    |
| 0.0497     | 0.3371          | 14    |
| 0.0434     | 0.3504          | 15    |
| 0.0450     | 0.4149          | 16    |
| 0.0399     | 0.4440          | 17    |
| 0.0367     | 0.4434          | 18    |
| 0.0381     | 0.4439          | 19    |
| 0.0372     | 0.4125          | 20    |
| 0.0318     | 0.4081          | 21    |
| 0.0318     | 0.3984          | 22    |
| 0.0300     | 0.3933          | 23    |
| 0.0306     | 0.4012          | 24    |
| 0.0282     | 0.4103          | 25    |
| 0.0263     | 0.4319          | 26    |
| 0.0263     | 0.4132          | 27    |
| 0.0251     | 0.4190          | 28    |
| 0.0257     | 0.4146          | 29    |


### Framework versions

- Transformers 4.40.1
- TensorFlow 2.15.0
- Datasets 2.19.1
- Tokenizers 0.19.1
