

This directory supports the evaluation of model generalizability beyond controlled experimental setups, using real-world Software Requirements Specifications (SRS) documents.

## Repository Contents

- [`three_real_world_srs/`](./three_unseen_srs/)  
  Contains three real-world SRS documents used for **out-of-distribution evaluation**.  
  > ⚠️ *One of the SRS documents originates from the authors and contains hardcoded institutional affiliations that could compromise the double-blind review process. Therefore, it has been temporarily removed and will be released under an appropriate open-source license after the review period.* We appreciate your understanding.

The original licenses for the remaining two SRS (NTP and RMOS) documents are provided within each subdirectory. Users are requested to read and comply with their licensing terms before use. 

- [`RQ4_evaluation.ipynb`](./RQ4_evaluation.ipynb)  
  Jupyter notebook containing results for **Research Question 4 (RQ4)**. This notebook assesses the ability of **ReqSeek** to generalize to out-of-distribution SRS documents not seen during training.




