---
pretty_name: Software Requirements Dataset (SwaRD)
language:
- en
task_categories:
- text-classification
tags:
- requirements-engineering
- automatic-requirements-identification
- software-requirements
---

# SwaRD — Software Requirements Dataset

SwaRD was constructed in the [ReqSeek study](https://github.com/kasrahabib/ReqSeek) by applying ReqSeek to a corpus of textual requirements data to automatically identify ISO 29148-style requirements and two types of auxiliary sentences. The complete research dataset contains sentence-level instances derived from 231 SRSs and requirements datasets.

## SwaRD Column Descriptions

The following table describes the columns of the released SwaRD dataset.

| Column Name | Description |
|---|---|
| `REQID` | Internal identifier assigned by the authors; may contain duplicate values. |
| `REQID_expanded` | Unique identifier for each instance in SwaRD. |
| `Project Name` | Name of the project from which the sentence originates. |
| `Subproject Name` | Name of a subproject within the larger project. |
| `Requirement Sentences` | Requirement text. |
| \*`F/NF Classes` | Placeholder for functional (F) versus non-functional (NF) requirement classification. |
| \*`NF Subclasses` | Placeholder for non-functional requirement subclasses (e.g., performance, usability). |
| `isReqSysAuxContAux_with_keyword` | Signal keyword used (e.g., *shall*, *should*, *will*, *may*, *must*). |
| `isReqSysAuxContAux` | Multi-class label: requirement vs. system-related auxiliary vs. contextual auxiliary. |
| `isReqAux` | Binary label: requirement vs. auxiliary (system/context merged). |

**\*Note:** The `F/NF Classes` and `NF Subclasses` columns are currently unpopulated (all values are `None`) and are retained for potential future requirements classification tasks.

## Dataset Size

The original study analyzed the **complete research dataset (40,522 instances)**. The public release currently contains **33,260 instances**; **7,262 instances** are excluded due to source-specific redistribution restrictions or unclear permissions. These public-release exclusions do not change the reported research results.

| Class | Complete Research Dataset | Public Release |
|---|---:|---:|
| `requirement` | 10,201 | 7,168 |
| `system_related_auxiliary` | 25,746 | 23,062 |
| `contextual_auxiliary` | 4,575 | 3,030 |
| **Total** | **40,522** | **33,260** |

## Loading

```python
from datasets import load_dataset

sward = load_dataset("kasrahabib/SwaRD")
```

To view licensing information:

```python
print(sward.info.license)
```

For the locally packaged dataset, see the [dataset usage instructions](https://github.com/kasrahabib/ReqSeek/blob/main/datasets/README.md).


## Licensing and Provenance

SwaRD contains source material governed by mixed and custom licensing terms and is not distributed under a single unified license. Source-specific attribution and licensing information are preserved in the dataset metadata and can be inspected using `sward.info.license` or the accompanying `dataset_info.json` file. Users are responsible for complying with the applicable terms of the original sources.

The current public-release composition and applicable redistribution restrictions are documented in the [ReqSeek dataset README](https://github.com/kasrahabib/ReqSeek/blob/main/datasets/README.md). The complete research dataset is preserved separately and is not part of the public release.

## Citation

If you use SwaRD, please cite the accompanying paper:

```bibtex
@article{habib2026reqseek,
  title  = {ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets},
  author = {Habib, Mohammad Kasra and Umm-e-Habiba and Graziotin, Daniel and Wagner, Stefan},
  year   = {2026},
  note   = {Accepted for publication in ACM Transactions on Software Engineering and Methodology}
}
```
