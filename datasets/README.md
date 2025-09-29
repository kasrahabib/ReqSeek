# Datasets:


This directory provides details and instruction how to use the three datasets (`ARID`, `SwaRD`, `BLINDED-DATASET`) that were made available via the HotCRP submission portal during the peer-review process.

- 🔒 **Access Notice**: These datasets are currently shared exclusively for peer review.
- 📢 We will **make them publicly available; open-source,** after the peer-review process is complete.

We use Hugging Face API `dataset` format for our datasets. Hugging Face datasets offer several advantages:


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

Load the datasets using:

```python
from datasets import load_from_disk

# Load SwaRD dataset
sward = load_from_disk("<path-to-dataset>/SwaRD/")
sward
```

Output:
```
Dataset({
	features: ['REQID', 'REQID_expanded', 'Project Name', 'Subproject Name', 'Requirement Sentences', 'isF/NF', 'NF Subclasses', 'isReqSysAuxContAux_with_keyword', 'isReqSysAuxContAux', 'isReqAux'], num_rows: 40522
})
```

## Selecting the Requirements

You can filter the ```requirements from the auxilariy classes using:
```python
sward.filter(lambda col: col['isReqAux'] == 'requirement')
```

Output:
```
Dataset({
    features: ['REQID', 'REQID_expanded', 'Project Name', 'Subproject Name', 'Requirement Sentences', 'isF/NF', 'NF Subclasses', 'isReqSysAuxContAux_with_keyword', 'isReqSysAuxContAux', 'isReqAux'],
    num_rows: 10201
})
```

## Converting the Dataset to Other Formats

```python
sward.to_pandas()
```

Or

```python 
sward.to_dict()
```

# Datasets Columns and Description

## SwaRD 

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

## UOCSSR

| Column Name             | Description |
|------------------------|-------------|
| `REQID`                 | Internal identifier assigned by the authors. May contain duplicate values. |
| `REQID_expanded`        | Unique identifier for each requirement in UOCSSR. |
| `Project Name`          | Name of the project from which the requirement originates. |
| `Subproject Name`       | Name of a subproject within the larger project. |
| `Requirement Sentences` | The textual content of the requirement statement. |
| `isF/NF`                | Indicates whether the requirement is **Functional (F)** or **Non-Functional (NF)**. |
| `NF Subclasses`         | If non-functional, specifies the sub-category (e.g., reliability, maintainability). |

---

## ARID

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


