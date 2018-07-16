#ETL tool
Tool to perform ETL processing for a given dataset.

##How to install
```bash
git clone https://github.com/santoshr1016/etl_hack.git

cd etl_hack

pip install .

python
```

##How to run
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
###TODOS
Yet to implement hot encoding