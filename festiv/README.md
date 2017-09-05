# FESTIV (Python)

### Installation

- Install [Miniconda2](https://conda.io/miniconda.html)
- Run the following `pip install git+git://github.com/kdheepak/psst.git@v0.1.3`
- Run the following `conda install -c conda-forge coincbc`

### Troubleshooting

When building the HELICS python extension, use `conda`.

```bash
conda install cython
```

The above is required to build the Cython extension. The following may also work as an alternative.

```bash
pip install cython
```

```bash
conda install libgcc
```

This is possibly required to make sure that the gcc used by Cython is the most recent.

### Run

```python
python main.py
```

