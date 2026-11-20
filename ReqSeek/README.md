---
license: mit
base_model: FacebookAI/roberta-base
library_name: transformers
pipeline_tag: text-classification
tags:
  - requirements-engineering
  - requirements-identification
  - sentence-classification
  - roberta
---

# ReqSeek

**ReqSeek** is a RoBERTa-base model fine-tuned for sentence-level automatic requirements identification in software requirements specifications (SRSs). It classifies text into three categories:

- **Requirement:** An ISO 29148-style statement expressing a system obligation or provision.
- **System-related auxiliary:** Technical information about a system that does not itself state a requirement.
- **Contextual auxiliary:** Background or document-context information rather than a requirement.

ReqSeek is intended to help identify requirements in heterogeneous SRSs and support the construction of requirements datasets. It processes sentences independently; it is not designed to reconstruct requirements spanning multiple sentences or reliably identify statements that substantially depart from the study's ISO 29148-style definition.

## Training data

The model was trained and evaluated using the **complete ARID research dataset**, which contains **2,396 manually labeled sentence-level instances** collected from **23 heterogeneous SRSs and requirements datasets**: 1,050 requirements, 746 system-related auxiliary instances, and 600 contextual auxiliary instances. The labels were assigned by the study's first author using documented annotation guidelines.

The [publicly distributed ARID dataset](https://huggingface.co/datasets/kasrahabib/ARID) may contain fewer instances because some source materials have redistribution restrictions. See the [replication package](https://github.com/kasrahabib/ReqSeek) for the current release notes. These restrictions do not alter the original training or reported evaluation results.

## Evaluation

On the paper's held-out ARID evaluation set (**480 instances**), ReqSeek achieved the following average scores:

| Precision | Recall | F1 |
|---:|---:|---:|
| 0.95 | 0.95 | 0.95 |

These results describe evaluation on the complete research dataset's held-out split; they are **not** performance estimates for every possible SRS or the currently released ARID subset. The paper also reports out-of-domain evaluation and robustness analyses.

## Training setup

- **Base model:** [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base)
- **Task:** Three-class sentence classification
- **Fine-tuning:** 30 epochs, batch size 16, initial learning rate 2 × 10⁻⁵, no early stopping, zero warm-up steps

## Research and resources

- [ReqSeek replication package](https://github.com/kasrahabib/ReqSeek)
- [ARID dataset](https://huggingface.co/datasets/kasrahabib/ARID)
- [SwaRD dataset](https://huggingface.co/datasets/kasrahabib/SwaRD)


## Citation

If you use ReqSeek in your research, please cite:

```bibtex
@article{habib2026reqseek,
  title  = {ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets},
  author = {Habib, Mohammad Kasra and Umm-e-Habiba and Graziotin, Daniel and Wagner, Stefan},
  year   = {2026},
  note = {Accepted for publication in ACM Transactions on Software Engineering and Methodology}
}
```

