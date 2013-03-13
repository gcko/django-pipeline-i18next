# Django Pipeline i18next

[i18next](http://i18next.com/) compiler for django-pipeline.

## Requirements

- i18next: [i18next](http://i18next.com/)

## Installation

```
pip install git+https://github.com/gcko/django-pipeline-i18next.git
```

## Usage

```python
# settings.py

PIPELINE_COMPASS_BINARY = '/usr/local/bin/compass'   # default: '/usr/bin/env compass'
PIPELINE_COMPASS_ARGUMENTS = '-c path/to/config.rb'  # default: ''

PIPELINE_COMPILERS = (
  'pipeline_compass.compass.CompassCompiler',
)
```