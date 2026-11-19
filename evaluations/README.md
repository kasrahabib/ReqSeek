# Evaluations

This directory contains the experimental scripts, notebooks, and supporting materials for evaluating ReqSeek, as described in the accompanying paper.

## Directory Contents

1. **[`RQ1/`](./RQ1/)**: Setup, experiments, and evaluation for Research Question 1.
2. **[`RQ2/`](./RQ2/)**: Setup, experiments, and evaluation for Research Question 2.
3. **[`RQ3/`](./RQ3/)**: Setup, experiments, and evaluation for Research Question 3.
4. **[`RQ4/`](./RQ4/)**: Setup, experiments, and evaluation for Research Question 4.
5. **[`RQ5/`](./RQ5/)**: Setup, experiments, and evaluation for Research Question 5.
6. **[`hardware_and_software_specs`](./hardware_and_software_specs)**: Hardware and software specifications used in this research.
7. **[`ReqSeek_Figures/`](./ReqSeek_Figures/)**: Mermaid source files and corresponding figures used in the paper.

## Reproducibility and Data Availability

The experimental notebooks document the methodologies and procedures used in this research, such as data preprocessing, model training, noise generation, and evaluation. However, some experiments cannot be fully reproduced using the publicly released artifacts due to the exclusion of records for which redistribution permissions could not be established (for details, see [`create_dataset_release_filtered.ipynb`](../datasets/create_dataset_release_filtered.ipynb)). Therefore, rerunning experiments using the released dataset subsets may not reproduce the results reported in the paper.

The experimental notebooks reference the original datasets via paths that contain `datasets_with_data`. To use the publicly released datasets, update these paths to point to the `datasets/<dataset-name>` directory at the repository root.

We are following up with relevant source providers regarding redistribution permissions and may update the datasets and replication package as additional materials become eligible for release.

While the finalized ReqSeek application model is publicly available in the repository, the trained experimental models generated during the RQ1 10-fold cross-validation and RQ2 labeling-inconsistency experiments are not hosted due to their substantial storage requirements (approximately 16.86 GB and 138.03 GB, respectively). Interested researchers may contact the authors to request copies of these experimental models.

The reproducibility status and limitations of each research question are summarized below.

| Research Question | Reproducibility Status | Reproducibility Limitations |
|---|---|---|
| **RQ1** | Partially reproducible | The experiments depend on the complete ARID dataset, including records excluded from the public release due to third-party redistribution restrictions. The 10-fold cross-validation experiment also produces trained model artifacts totaling approximately 16.86 GB, which are not included in the repository due to their size. |
| **RQ2** | Partially reproducible | The labeling-inconsistency experiments require the complete ARID dataset. Additionally, the trained experimental models occupy approximately 138.03 GB and are not distributed through GitHub due to their substantial storage requirements. |
| **RQ3** | Partially reproducible  | The experiments depend on the complete ARID dataset, including records that cannot currently be redistributed. |
| **RQ4** | Fully reproducible (verified) | - |
| **RQ5** | Partially reproducible | The experiments depend on the complete ARID and SwaRD datasets and the original UOCSSR source corpus, portions of which cannot currently be redistributed. |



