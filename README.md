# dtables

dtables is a Python based minimalistic framework for exploratory data analysis. This project is under development. A rough [API map is available](https://manasgarg.gitbooks.io/dtables/content/load-data.html).

## Goals

* **Minimal** - Quick to learn and get going. Useful for programmers who are just dabbling in data analysis. Not necessarily for pros whose day job is data analysis. Focus on "one way to solve problems" rather than "different ways to match different situations".
* **Complete** - Minimal does not mean incomplete. Do not leave important use cases unaddressed. Try to address them without adding concepts.

Performance is not an initial goal. The current objective is to make it work well for smallish datasets (10s of MBs).

## Features

### Loaders
- [x] load_dict
- [x] load_tuples
- [x] load_csv
- [ ] load_json
- [ ] load_table

### Overview
- [x] column names
- [ ] dtypes
- [ ] shape
- [ ] describe

### Column name Slicing
- [ ] name based
- [ ] position based 


### Dtable Slicing
#### Column Based
- [ ] single column name
- [ ] array of column names
- [ ] column name range
- [ ] single position
- [ ] array of position
- [ ] range of position
- [ ] boolean array based

#### Row based
- [ ] single position
- [ ] array of position
- [ ] range of position
- [ ] boolean array based

### Assignment
- [ ] overwrite existing columns
- [ ] add new columns
- [ ] overwrite existing rows

### Vectorized operations
- [ ] arithmetic
- [ ] comparison
- [ ] broadcasting

### Transformation
- [ ] row apply
- [ ] column apply

### Reshaping
- [ ] pivot
- [ ] melt

### Extending
- [ ] append
- [ ] join

### Aggregates
- [ ] sort
- [ ] group apply
