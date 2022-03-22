# More to come ...

### Important Pykson has a bug in class FloatField
Pykson > __init__.py > Line 112 should be changed to have a conversion to float on the value
```
if value is not None and not isinstance(float(value), float):
```