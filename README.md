# NumPy & Pandas Practice

Hands-on practice scripts from learning **NumPy** and **Pandas** as a first step towards Machine Learning.

## NumPy: array manipulation

| File | Topic | What it shows |
|------|-------|---------------|
| `append.py` | `np.append` | Adding an element to the end of a 1D array |
| `insert.py` | `np.insert` | Inserting values at an index (flattened, or along a row/column axis) |
| `dlt.py` | `np.delete` | Removing a row/column from a 2D array |
| `concate.py` | `np.concatenate` | Joining arrays along `axis=0` (rows) and `axis=1` (columns) |
| `stack.py` | `np.stack`, `vstack`, `hstack` | Stacking arrays along a new axis, vertically and horizontally |
| `split.py` | `np.split`, `hsplit`, `vsplit` | Splitting arrays into equal parts |

## Pandas: reading & writing data

A small DataFrame exported to three formats (`data/output.csv`, `data/output.xlsx`, `data/output.json`) to practise Pandas I/O (`to_csv`, `to_excel`, `to_json`).

## How to run

```bash
pip install numpy pandas openpyxl
python append.py
```

## What I learned

- Difference between joining (`concatenate`) and stacking (`stack`)
- How `axis=0` (rows) and `axis=1` (columns) change the result
- Exporting the same data in CSV, Excel and JSON formats

## Next

- More Pandas (filtering, groupby, merging)
- Matplotlib / Seaborn for visualisation
- First ML model with scikit-learn

---
By [Prabhuta Gupta](https://github.com/prabhutaguptaa)
