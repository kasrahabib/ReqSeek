# Replication Package

[![DOI](https://zenodo.org/badge/1463329008.svg)](https://doi.org/10.5281/zenodo.24418048)

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
Contains the ReqSeek model and supporting resources. The model is also available on [Hugging Face](https://huggingface.co/kasrahabib/ReqSeek). For instructions on downloading and using the model, see [`demo.ipynb`](./demo.ipynb).

### 2. [`datasets/`](./datasets/)

Contains the two datasets developed for this study (ARID and SwaRD), along with their documentation and [usage instructions](./datasets/README.md). Both datasets are also available on Hugging Face: [ARID](https://huggingface.co/datasets/kasrahabib/ARID) and [SwaRD](https://huggingface.co/datasets/kasrahabib/SwaRD).

### 3. [`evaluations/`](./evaluations/)

Contains experimental setups, evaluation scripts, results, and supporting materials for the research questions investigated in the paper.

---

## Citation

If you use ReqSeek, ARID, SwaRD, or other materials from this replication package in your research, please cite the associated publication.

For citation details, see [`CITATION.cff`](./CITATION.cff).


## License

Copyright © 2026 Mohammad Kasra Habib.

For licensing information, attribution requirements, and applicable terms for the different components of this replication package, see [`LICENSE.md`](./LICENSE.md).