# Replication Package for **ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets**

📄 **Usage Restriction Prior to Paper Publication**  
This repository is provided solely as a replication package for the peer review process.
**Do not use, modify, or redistribute any content until the paper is officially published.** After publication, this repository will be archived on Zenodo with an open license.  

--- 

## Summary  
This replication package supports our paper titled: **ReqSeek: Transformer-Based Automatic Requirements Identification for Building Large Requirements Datasets**, which introduces a transformer-based approach (ReqSeek) for automatically identifying requirements in textual data. Many deep-learning methods require large datasets, but collecting labeled requirements data is challenging. Our work aims to facilitate the creation of large-scale requirements datasets for training AI models.

---


## Repository Content  
1. **[`ReqSeek/`](./ReqSeek/)**  
   - This is the ***ReqSeek*** model; the best performing model. For more details, refer to the paper.

   - [`demo.ipynb`](./demo.ipynb): This notebook demonstrates how to download and use `ReqSeek.`
   - **Note**: To run `ReqSeek`, you might need GPU power

2. **[`datasets/`](./datasets/)**  
   - **Will contain** our curated requirements datasets. The three curated datasets (`ARID`, `SwaRD`, `BLINDED-DATASET`) are exclusively submitted for review through the submission portal.
   - Includes a tutorial on how to load and use them. 
   -  We will **make all three datasets publicly available,** after the peer-review process is complete.

3. **[`evaluations`](./evaluations/)**: Contains setup, experiments, and evaluation for all RQs.

---

## 🔒 License  
Copyright © Mohammad Kasra Habib, 2025. All rights reserved.  
**Strictly no use, modification, or distribution permitted until paper publication.**  
Post-publication, this repository will be archived on Zenodo under an open license. 