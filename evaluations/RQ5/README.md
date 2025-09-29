# Dataset Comparison and SwaRD Construction

This directory documetns the process of constructing the **SwaRD** dataset using ReqSeek and presents comparisons against human-curated datasets and our blinded (for peer-review) heuristic dataset.

## Repository Contents

- [`re_datasets_for_comparison/`](./re_datasets_for_comparison/)  
  Contains human-curated datasets used to benchmark our heuristics and the **SwaRD** dataset.  
  The license for each SRS is included within its respective subdirectory. Users are required to read and comply with the licensing terms before use.

- [`Identifying_Requirements_for_SwaRD_and_adding_license.ipynb`](./Identifying_Requirements_for_SwaRD_and_adding_license.ipynb)  
  This notebook demonstrates how requirements were identified from the heuristic dataset using **ReqSeek** to create the **SwaRD** dataset.  
  > ⚠️ *This notebook cannot be executed as-is, as it depends on the raw heuristic dataset (blinded for peer review), due to licensing restrictions and the inclusion of non-disclosure protected requirements. It is provided here solely for transparency and documentation of the SwaRD construction process.*

- [`RQ5.ipynb`](./RQ5.ipynb)  
  Evaluates and compares **SwaRD**, the (blinded) heuristic dataset, and two human-curated datasets to address **Research Question 5 (RQ5)**.  
  Interested users can replicate the analysis by placing the provided datasets into the appropriate directory structure using the **HotCRP.com** submission portal.
