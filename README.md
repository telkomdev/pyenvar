## Penvy

Python's `.env` loader

### Install
```shell
$ pip install penvy
```

### Unit test
```shell
$ python -m unittest
```

### Usage

Make sure the `.env` file is in your project's `root` folder
```
myproject
   - src/
     - __init__.py
   - main.py
   - .env
```

Assumed the `.env` file looks like this
```.env
USERNAME=admin
PASSWORD='12345'
```

#### Basic usage
```python
import os
import penvy

penvy.load()
print(os.environ.keys())
username = os.environ.get('USERNAME')
print(username)
```

#### Custom .env path

```python
import os
import penvy

penvy.load(path='./config/.env', encoding='utf-8')
print(os.environ.keys())
username = os.environ.get('USERNAME')
print(username)
```