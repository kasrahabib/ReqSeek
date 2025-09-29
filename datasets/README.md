# Directory Content

🔒 **Availability Notice:** These datasets are currently shared exclusively for peer review through the submission portal for the peer-review process.

This directory provides details and instructions on how to use the three datasets: `ARID`, `SwaRD`, `UOCSSR`).




We use Hugging Face `dataset` API for our datasets. Hugging Face datasets offer several advantages:


- Efficient memory usage for large datasets
- Built-in support for filtering, mapping, and streaming
- Easy conversion to/from other formats (`pandas`, `.csv`, `.json`, etc.)
- Consistent structure for replication and benchmarking


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
A manually curated and labeled dataset of ISO/IEC/IEEE 29148 requirements from 23 industrial SRSs. While ReqSeek was trained on the full set, 6 SRSs were excluded from release due to licensing restrictions, leaving requirements from 17 SRSs in the current release. ARID was created to support domain-agnostic training and evaluation of ReqSeek.


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

A large-scale dataset derived by applying ReqSeek to refine and extend earlier resources. It covers three categories:
- `requirement`: 10,201 (primary class of interest)
- `contextual_auxiliary`: 4,575 (useful for other AI tasks, e.g., RAG)
- `system_related_auxiliary`: 25,746 (useful for other AI tasks, e.g., RAG)


The `10,201` instances in the requirement class form the main contribution, representing well-formed requirements, while the auxiliary classes capture surrounding context and system-related information. SwaRD offers high label quality and broad domain coverage, making it suitable for scalable ARI research.


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

---

### Unified Open- and Close-Source Software Requirements Dataset (UOCSSR)
An earlier dataset was created using heuristic-based methods. While useful for initial studies, UOCSSR primarily served as a foundation for developing SwaRD, which improves reliability, consistency, and representativeness.

| Column Name             | Description |
|------------------------|-------------|
| `REQID`                 | Internal identifier assigned by the authors. May contain duplicate values. |
| `REQID_expanded`        | Unique identifier for each requirement in UOCSSR. |
| `Project Name`          | Name of the project from which the requirement originates. |
| `Subproject Name`       | Name of a subproject within the larger project. |
| `Requirement Sentences` | The textual content of the requirement statement. |
| `isF/NF`                | Indicates whether the requirement is **Functional (F)** or **Non-Functional (NF)**. |
| `NF Subclasses`         | If non-functional, specifies the sub-category (e.g., reliability, maintainability). |
