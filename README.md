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

django-pipeline-i18next takes input from Yaml and converts it to namespaced javascript object which can then 
be referenced from your i18next initalizer. The following is an example of usage:

Create your localized message files:

```yaml
#en_US.yml
global:
  hello: Hello World!
```

Add the following to your settings:

```python
# settings.py

PIPELINE_I18NEXT_NAMESPACE = 'Messages'   # defaults to : 'Locale'

PIPELINE_COMPILERS = (
  'pipeline_i18next.i18next.I18nextCompiler',
)

# add the message files to PIPELINE_JS
PIPELINE_JS = {
    'bundle': {
        'source_filenames': (
          ...
          'locales/en_US.yml',
          ...
        ),
        'output_filename': 'js/bundle.js',
    }
}

```

The Yaml file will be compiled down to a javascript file namespaced under ```window.[PIPELINE_I18NEXT_NAMESPACE]```

Next, in your initialization for i18next, add the following:

```javascript
//init.js

i18n.init({ resStore: window.Messages });

```

And that's it!
