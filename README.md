# Kommit test

| dependencies | code example |
| ------ | ------ |
| sys | pip install sys|
| requests | pip install requests |


Code example in the command prompt:

Get all params of people table
```
python main.py select * from people
```

Get name param of people table example
```sh
python main.py select name from people
```

If you need show more params, without spaces write separated by ','
```python
python main.py select name,gender from people
```
