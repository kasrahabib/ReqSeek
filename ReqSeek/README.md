---
license: cc-by-4.0
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

[![DOI](https://zenodo.org/badge/1463329008.svg)](https://doi.org/10.5281/zenodo.24418048)

**ReqSeek** is a RoBERTa-base model fine-tuned for sentence-level automatic requirements identification in software requirements specifications (SRSs). It classifies text into three categories:

- `requirement`: An ISO 29148-style statement expressing a system obligation or provision.
- `system_related_auxiliary`: Technical information about a system such as explaining an algorithm, architecture, or design.
- `contextual_auxiliary`: Background or document-context information.

ReqSeek is intended to help identify requirements in heterogeneous SRSs and support the construction of ISO 29148-style requirements datasets.


For practical usage, including model inference and custom label mapping, see the [ReqSeek demo notebook](https://github.com/kasrahabib/ReqSeek/blob/main/demo.ipynb).


## Training data

The model was trained and evaluated using the **complete ARID research dataset**, which contains **2,396 manually labeled sentence-level instances** collected from **23 heterogeneous SRSs and requirements datasets**: 1,050 `requirement`, 746 `system_related_auxiliary` instances, and 600 `contextual_auxiliary` instances.

The ARID dataset is available on [Hugging Face](https://huggingface.co/datasets/kasrahabib/ARID). Details on dataset availability, licensing, and release restrictions are documented in the [ReqSeek replication package](https://github.com/kasrahabib/ReqSeek).

## Evaluation

On the paper's held-out ARID evaluation set (**480 instances**), ReqSeek achieved the following average scores:

| Precision | Recall | F1 |
|---:|---:|---:|
| 0.95 | 0.95 | 0.95 |


## Training setup

- **Base model:** [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base)
- **Task:** Three-class sentence classification
- **Fine-tuning:** 30 epochs, batch size 16, initial learning rate 2 × 10⁻⁵, no early stopping, zero warm-up steps



## License

ReqSeek is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

ReqSeek is fine-tuned from [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base), which is distributed under the MIT license. The original base model's copyright and license notices remain applicable.


## Research and resources

- [ReqSeek paper (arXiv:2611.29722)](https://arxiv.org/abs/2611.29722)
- [ReqSeek replication package](https://github.com/kasrahabib/ReqSeek)
- [ARID dataset](https://huggingface.co/datasets/kasrahabib/ARID)
- [SwaRD dataset](https://huggingface.co/datasets/kasrahabib/SwaRD)


## Citation

If you use ReqSeek in your research, please cite the accompanying paper.

**Publication status:** Accepted for publication in *ACM Transactions on Software Engineering and Methodology (TOSEM)*, 2026.

**Preprint:** [arXiv:2611.29722](https://arxiv.org/abs/2611.29722)

**BibTeX:**

```bibtex
@misc{habib2026reqseek,
  title         = {ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets},
  author        = {Mohammad Kasra Habib and Umm-e-Habiba and Daniel Graziotin and Stefan Wagner},
  year          = {2026},
  eprint        = {2611.29722},
  archivePrefix = {arXiv},
  primaryClass  = {cs.SE},
  url           = {https://arxiv.org/abs/2611.29722}
}
```


