# Datasets

This directory contains the **ARID** and **SwaRD** datasets developed as part of the **ReqSeek study**.


## Dataset Usage

Both datasets use the Hugging Face `datasets` library, which supports efficient data handling, filtering, mapping, and conversion to other formats.

For additional instructions on exploring, filtering, and converting the datasets, see [`how_to_use_datasets.ipynb`](./how_to_use_datasets.ipynb).


### Prerequisites

Install the required library:

```bash
pip install datasets
```

### Option 1: Load Datasets from This Repository

If you downloaded or cloned the ReqSeek replication package, load the datasets directly from their local directories using `load_from_disk()`:

```python
from datasets import load_from_disk

# Load ARID
arid = load_from_disk("./ARID")

# Load SwaRD
sward = load_from_disk("./SwaRD")
```

These examples assume that the script or notebook is executed from the `datasets/` directory.

### Option 2: Load Datasets Directly from Hugging Face

Alternatively, load **[ARID](https://huggingface.co/datasets/kasrahabib/ARID)** and **[SwaRD](https://huggingface.co/datasets/kasrahabib/SwaRD)** directly from Hugging Face using `load_dataset()`:

```python
from datasets import load_dataset

# Load ARID
arid = load_dataset("kasrahabib/ARID")

# Load SwaRD
sward = load_dataset("kasrahabib/SwaRD")
```

Both approaches provide access to the datasets through the Hugging Face `datasets` library, supporting operations for exploration, filtering, and conversion.

## Dataset Descriptions

### 1. Automatic Requirements Identification Dataset (ARID)

ARID is a manually curated and labeled dataset of ISO 29148-style requirements, system-related auxiliary sentences, and contextual auxiliary sentences collected from 23 heterogeneous Software Requirements Specifications (SRSs) and requirements datasets.

The complete research dataset used in the experiments contains **2,396 instances**. For public redistribution, selected source projects have been excluded pending clarification of their redistribution permissions.

The **publicly released ARID dataset contains 1,331 instances**, distributed as follows:

| Class | Complete Research Dataset | Public Release |
|---|---:|---:|
| requirement | 1,050 | 516 |
| system_related_auxiliary | 746 | 284 |
| contextual_auxiliary | 600 | 531 |
| **Total** | **2,396** | **1,331** |

Overall, **1,065 instances from 10 source-project groups** are excluded from the public version. These exclusions do not affect the original experimental results reported in the paper.

### 2. Software Requirements Dataset (SwaRD)

SwaRD is constructed using ReqSeek to automatically identify requirements and auxiliary sentences from textual requirements data.

The complete research dataset used in the study contains **40,522 sentence-level instances** from 231 SRSs and requirements datasets.

The **publicly released SwaRD dataset contains 33,260 instances**, distributed as follows:

| Class | Complete Research Dataset | Public Release |
|---|---:|---:|
| requirement | 10,201 | 7,168 |
| system_related_auxiliary | 25,746 | 23,062 |
| contextual_auxiliary | 4,575 | 3,030 |
| **Total** | **40,522** | **33,260** |

Overall, **7,262 instances** originating from four source groups, including 13 COEST constituent datasets, are excluded from the public version.

The reported research results are based on the complete SwaRD dataset and remain unchanged.

---

## Public Release Notes

The experiments reported in the accompanying ReqSeek paper were conducted using the complete research versions of ARID and SwaRD.

The publicly released versions contain fewer instances because selected source datasets have been temporarily excluded pending clarification of redistribution permissions.

The following source groups are currently withheld from the public release:

- **OPENCOSS**
- **Dronology**
- **Smarthome Requirements Dataset**
- **COEST**, including its 13 constituent datasets

**These exclusions concern the redistribution of source data and do not change the original experiments or their reported results in the accompanying paper.**

The authors intend to clarify redistribution permissions with the relevant dataset owners and may update the public datasets if additional permissions are obtained.

The complete research datasets are preserved separately and are not part of the public release.

### Public Release Summary

| Dataset | Complete Research Dataset | Excluded Instances | Public Release |
|---|---:|---:|---:|
| ARID | 2,396 | 1,065 | **1,331** |
| SwaRD | 40,522 | 7,262 | **33,260** |

For detailed class distributions of the complete research datasets and their publicly released versions, see Sections 1 and 2 above.

### Release Generation

The public-release datasets are generated using [`create_dataset_release_filtered.ipynb`](./create_dataset_release_filtered.ipynb).

The notebook documents the source-exclusion rules, generates the reduced datasets for public release, updates their source-specific licensing information, and displays the resulting class distributions.

The notebook is provided for **transparency and documentation**. It cannot be executed using only the publicly released materials because it requires access to the complete research datasets, which are preserved separately and are not publicly distributed.