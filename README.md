# Django Pipeline i18next

[i18next](http://i18next.com/) compiler for django-pipeline.

## Requirements

- i18next: [i18next](http://i18next.com/)

## Installation

```
pip install git+https://github.com/gcko/django-pipeline-i18next.git
```

Or you can add it to your requirements.txt file like so:

```
-e git+https://github.com/gcko/django-pipeline-i18next.git@3e7affbd91e9bd2abbab405ad2b94b89e439b200#egg=django-pipeline-i18next
```

Where the hash after the `@` sign is the git commit hash

## Usage

```python
# settings.py

PIPELINE_I18NEXT_NAMESPACE = 'Messages'   # default: 'Locale'

PIPELINE_COMPILERS = (
  'pipeline_i18next.i18next.I18nextCompiler',
)
```