# FakeModel

#### Language: Python

## Model Description

FakeModel is a fake model that dosn't do anything.

## References

- Citation to a publication on a theory the model uses
- Citation to a dataset the model uses
- Citation to a code (e.g. repository, documentation) that the model uses

## Relevant Equations

![img](http://latex.codecogs.com/svg.latex?r_{growth}=\frac{r_{photo}}{2})

## Requirements

- yggdrasil

## Running the model on the provided example data

### Without yggdrasil

```
python src/fakemodel.py Input/input.txt Output/output.txt
```

### With yggdrasil

```
yggrun fakemodel.yml fakemodel_files.yml
```

## Model Inputs/Outputs

### Inputs

Name                | Units       | Data Type | File/Argument   | Description
------------------- | ----------- | --------- | --------------- | -----------
photosynthesis_rate | umol/m**2/s | float     | Input/input.txt | The photosynthetic rate.


### Outputs

Name        | Units | Data Type | Description
----------- | ----- | --------- | -----------
growth_rate | cm/s  | float     | The vertical growth rate.


## Tests

### Test 1: Confirm output

#### Command to run test

```
python src/fakemodel.py Input/input.txt Output/output.txt
```

#### Command to evaluate test

```
diff Output/output.txt Output/expected.txt
```
