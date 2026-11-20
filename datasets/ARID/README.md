---
pretty_name: Automatic Requirements Identification Dataset (ARID)
language:
- en
task_categories:
- text-classification
tags:
- requirements-engineering
- automatic-requirements-identification
- software-requirements
---

# ARID — Automatic Requirements Identification Dataset

ARID is a manually curated and labeled dataset of ISO 29148-style requirements and auxiliary sentences, developed for the [ReqSeek study](https://github.com/kasrahabib/ReqSeek). The **complete research dataset** was drawn from 23 heterogeneous software requirements specifications (SRSs) and requirements datasets and was used to train and evaluate ReqSeek.

## ARID Column Descriptions

The following table describes the columns of the released ARID dataset.

| Column Name             | Description |
|------------------------|-------------|
| `REQID`                 | Internal identifier assigned by the authors. May contain duplicate values. |
| `REQID_expanded`        | Unique identifier for each requirement in ARID. |
| `Project Name`          | Name of the project from which the requirement originates. |
| `Subproject Name`       | Name of a subproject within the larger project. |
| `Requirement Sentences` | Requirement text. |
| `signal_keyword`        | Manually labeled signal keyword in the sentence (e.g., *shall*, *should*, *will*, *may*, *must*). |
| `ternary_cls` | Manually annotated class: **requirement**, **system-related auxiliary**, or **contextual auxiliary**. |
| `binary_cls` | Binary annotation: **requirement** or **auxiliary** (merging system/context auxiliary). |

## Dataset Size

The original experiments used the **complete research dataset (2,396 instances)**. The public release currently contains **1,331 instances**, with **1,065 instances** excluded because redistribution permissions are restricted or unclear. Public-release changes do not alter the experiments or results reported in the paper.

| Class | Complete Research Dataset | Public Release |
|---|---:|---:|
| `requirement` | 1,050 | 516 |
| `system_related_auxiliary` | 746 | 284 |
| `contextual_auxiliary` | 600 | 531 |
| **Total** | **2,396** | **1,331** |

## Loading

```python
from datasets import load_dataset

arid = load_dataset("kasrahabib/ARID")
```

To view licensing information:

```python
print(arid.info.license)
```

For the locally packaged dataset, see the [dataset usage instructions](https://github.com/kasrahabib/ReqSeek/blob/main/datasets/README.md).

## Licensing and Provenance

ARID contains source material governed by mixed and custom licensing terms and is not distributed under a single unified license. Source-specific attribution and licensing information are preserved in the dataset metadata and can be inspected using `dataset.info.license` or the accompanying `dataset_info.json` file. Users are responsible for complying with the applicable terms of the original sources.

The current public-release composition, withheld sources, and usage notes are documented in the [ReqSeek dataset README](https://github.com/kasrahabib/ReqSeek/blob/main/datasets/README.md). The complete research dataset is preserved separately and is not part of the public release.

## Citation

If you use ARID, please cite the accompanying paper:

```bibtex
@article{habib2026reqseek,
  title  = {ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets},
  author = {Habib, Mohammad Kasra and Umm-e-Habiba and Graziotin, Daniel and Wagner, Stefan},
  year   = {2026},
  note   = {Accepted for publication in ACM Transactions on Software Engineering and Methodology}
}
```
