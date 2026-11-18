# Replication Package

**Associated Publication:** *ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets*. *ACM Transactions on Software Engineering and Methodology (TOSEM)*.

**Authors:** Mohammad Kasra Habib, Umm-e-Habiba, Daniel Graziotin, and Stefan Wagner.

This repository contains the replication package supporting the associated research, including the ReqSeek model, curated datasets, experimental scripts, evaluation results, and accompanying documentation. 

---

## Summary

ReqSeek is a transformer-based approach for automatically identifying software requirements in textual data.

The construction of large and diverse requirements datasets is challenging, particularly when requirements must be identified across heterogeneous Software Requirements Specifications (SRSs). ReqSeek addresses this challenge through transformer-based classification, supporting the development of large-scale requirements datasets for software engineering research.

---

## Repository Contents

### 1. [`ReqSeek/`](./ReqSeek/)

Contains the ReqSeek model and supporting resources. 

- [`demo.ipynb`](./demo.ipynb): Demonstrates how to download and use ReqSeek.

### 2. [`datasets/`](./datasets/)

Contains the two datasets developed for this study, along with documentation and usage instructions:

- **Automatic Requirements Identification Dataset (ARID):** A curated, manually labeled dataset used to train and evaluate ReqSeek.
- **Software Requirements Dataset (SwaRD):** A large-scale requirements dataset constructed using ReqSeek.

### 3. [`evaluations/`](./evaluations/)

Contains experimental setups, evaluation scripts, results, and supporting materials for the research questions investigated in the paper.

---

## Citation

If you use ReqSeek, ARID, SwaRD, or other materials from this replication package in your research, please cite the associated publication.

For citation details, see [`CITATION.cff`](./CITATION.cff).


## License

Copyright © 2026 Mohammad Kasra Habib.

For licensing information, attribution requirements, and applicable terms for the different components of this replication package, see [`LICENSE.md`](./LICENSE.md).