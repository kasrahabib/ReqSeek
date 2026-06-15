# Directory Content

🔒 **Availability Notice:** These datasets are currently shared exclusively for peer review through the submission portal for the peer-review process.

This directory provides details and instructions on how to use the two datasets: `ARID`, `SwaRD`).




We use Hugging Face `dataset` API for our datasets. Hugging Face datasets offer several advantages:


- Efficient memory usage for large datasets
- Built-in support for filtering, mapping, and streaming
- Easy conversion to/from other formats (`pandas`, `.csv`, `.json`, etc.)
- Consistent structure for replication and benchmarking

## View Example Requirements

To explore a small sample of requirements on ARID and SwaRD without loading the full dataset, see the notebook:[`A_Sample_Requirements_Identified_by_ReqSeek_in_the_SwaRD_Dataset.ipynb`](./A_Sample_Requirements_Identified_by_ReqSeek_in_the_SwaRD_Dataset.ipynb)

## Prerequisite

Make sure you have the `datasets` library installed:

```bash
pip install datasets
```

## Loading the Datasets

Load the datasets using Hugging Face dataset:

```python
from datasets import load_from_disk

# Load SwaRD dataset
sward = load_from_disk("<path-to-dataset>/SwaRD/")
```

### To View Each Dataset's Licenses
Each dataset is governed by its own license. After loading, you can use the dataset variable holding the dataset and access its license as follow:

```python
print(sward.info.license)
```

### Converting from Hugging Face to Pandas

```python
sward.to_pandas()
```

### Converting from Hugging Face to Dictionary

```python 
sward.to_dict()
```

See Hugging Face for conversion to other supported dataset formats. 


---

## Datasets Columns and Description



### Automatic Requirements Identification Dataset (ARID)
ARID is a manually curated and labeled dataset of ISO 29148-style requirements and auxiliary sentences collected from `23` publicly available SRSs and requirements datasets. ReqSeek was trained and evaluated on the full ARID dataset, which contains `2,396` instances: `1,050 requirement`, `600 contextual_auxiliary`, and `746 system_related_auxiliary`. However, six source projects were excluded from the public release because of licensing restrictions or insufficient licensing clarity. The current releasable version, therefore, contains instances from `17` source projects and comprises `1,609` instances: `686 requirement`, `598 contextual_auxiliary`, and `325 system_related_auxiliary`.

#### ARID Column Descriptions
The table below reports the metadata and column schema of the released ARID dataset, including identifiers, project provenance information, sentence text, signal keywords, and manual annotation labels.

| Column Name             | Description |
|------------------------|-------------|
| `REQID`                 | Internal identifier assigned by the authors. May contain duplicate values. |
| `REQID_expanded`        | Unique identifier for each requirement in ARID. |
| `Project Name`          | Name of the project from which the requirement originates. |
| `Subproject Name`       | Name of a subproject within the larger project. |
| `Requirement Sentences` | The textual content of the requirement statement. |
| `signal_keyword`        | Manually labeled signal keyword in the sentence (e.g., *shall*, *should*, *will*, *may*, *must*). |
| `binary_cls`            | Manually annotated class: **requirement**, **system-related auxiliary**, or **contextual auxiliary**. |
| `ternary_cls`           | Binary annotation: **requirement** or **auxiliary** (merging system/context auxiliary). |


---

### Software Requirements Dataset (SwaRD) 
SwaRD is constructed using our proposed ReqSeek model for automatic identification of requirements. SwaRD consists of `40,522` sentence-level instances from `231` publicly available SRSs and datasets. It comprises three classes: `10,201 requirement`, `4,575 contextual_auxiliary`, and `25,746 system_related_auxiliary` instances.

#### SwaRD Column Descriptions
The table below reports the metadata and column schema of the released SwaRD dataset, including identifiers, project provenance information, sentence text, signal keywords, and ReqSeek-identified classification labels.

| Column Name                         | Description |
|------------------------------------|-------------|
| `REQID`                             | Internal identifier assigned by the authors. May contain duplicate values. |
| `REQID_expanded`                   | Unique identifier for each requirement in SwaRD. |
| `Project Name`                     | Name of the project from which the requirement originates. |
| `Subproject Name`                  | Name of a subproject within the larger project. |
| `Requirement Sentences`           | The textual content of the requirement statement. |
| `isF/NF`                           | Indicates whether the requirement is **Functional (F)** or **Non-Functional (NF)**. |
| `NF Subclasses`                   | If non-functional, specifies the sub-category (e.g., performance, usability). |
| `isReqSysAuxContAux_with_keyword` | Identifies the signal keyword used (e.g., *shall*, *should*, *will*, *may*, *must*). |
| `isReqSysAuxContAux`              | Indicates if the sentence is a **requirement**, **system-related auxiliary**, or **contextual auxiliary**. |
| `isReqAux`                        | Binary label: whether the sentence is a **requirement** or an **auxiliary** (system/context merged). |