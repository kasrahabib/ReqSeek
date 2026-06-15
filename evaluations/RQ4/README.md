

This directory supports the evaluation of domain-agnosticism and generalizability beyond controlled experimental setups, using unseen Software Requirements Specifications (SRS) documents.

## Repository Contents

- [`three_unseen_srs/`](./three_unseen_srs/)  
  Contains the three unseen SRS documents used for **post hoc out-of-distribution evaluation**.  

The original licenses for the remaining two SRS documents (NTP and RMOS) are provided in each subdirectory. Users are requested to read and comply with their licensing terms before use. 

- [`RQ4_evaluation.ipynb`](./RQ4_evaluation.ipynb)  
  Jupyter notebook containing results for **Research Question 4** confirming **ReqSeek's** domain-agnosticism and its generalization ability to out-of-distribution SRS documents not seen during training.

- [`rq4_error_characterization.xlsx `](./rq4_error_characterization.xlsx)  
  Contains manual characterization of ReqSeek's error on three unseen SRS.

