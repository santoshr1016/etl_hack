#ETL tool
Tool to perform ETL processing for a given dataset.

##How to install
```bash
git clone https://github.com/santoshr1016/etl_hack.git

cd etl_hack

pip install .

python
```

## How to run
##### Provide any load file as input with correct location else it takes default arg
```python
import ETL_package.etl_pipeline as pipe
op = pipe.load()
print(pipe.transform(op))
```
## OR
```python
import ETL_package.etl_pipeline as pipe
op = pipe.load()
ml_input = pipe.transform(op)
```
## Removing package
```bash
pip uninstall ETL-package -y
```

# Design
## Stage 1:
Get the input from the file, removing the invalid line.

## Stage 2:
Extracting the data for the 8 columns only, Named tuples and Ordered Dictionary are used.

Calling the transformation function for each column data.

## Stage 3:
Representing the output in desired way.

### TODOS
Yet to implement hot encoding
