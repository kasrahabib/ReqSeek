# Dataset Comparison and SwaRD Construction

This directory documents the process of constructing the **SwaRD** dataset using **ReqSeek** and presents its evaluation against human-curated datasets and UOCSSR.
## Repository Contents

- [`re_datasets_for_comparison/`](./re_datasets_for_comparison/)  
  Contains human-curated datasets used to benchmark **UOCSSR** and the **SwaRD** dataset. 
 
- [`A_Sample_Requirements_Identified_by_ReqSeek_in_the_SwaRD_Dataset.ipynb`](./A_Sample_Requirements_Identified_by_ReqSeek_in_the_SwaRD_Dataset.ipynb)
Jupyter notebook generating representative samples of requirements identified by ReqSeek in the SwaRD dataset for qualitative inspection and appendix inclusion.

- [`Identifying_Requirements_for_SwaRD_and_adding_license.ipynb`](./Identifying_Requirements_for_SwaRD_and_adding_license.ipynb)  
  This script contains instructions to identify requirements from the UOCSSR dataset using **ReqSeek** to create the **SwaRD** dataset.  
  > ⚠️ *This notebook cannot be executed as-is, as it depends on the raw UOCSSR dataset. Due to licensing restrictions and the inclusion of non-disclosure protected requirements, we cannot release the UOCSSR dataset in full. It is provided here solely for transparency and documentation of the SwaRD construction process.*

- [`RQ5.ipynb`](./RQ5.ipynb)  
  Evaluates and compares **SwaRD**, **UOCSSR**, and two human-curated datasets (KIB3, NTP, and RMOS) to address **Research Question 5**.  
