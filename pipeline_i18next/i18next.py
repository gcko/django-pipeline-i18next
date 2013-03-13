import yaml
import json
from django.conf import settings

from pipeline.compilers import SubProcessCompiler

class I18nextCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
      return filename.endswith('.yml')

    def compile_file(self, infile, outfile, outdated=False, force=False):
      if not outdated and not force:
        return  # No need to recompiled file
      # Load the file as a Python Object
      locale = yaml.load(infile)
      # Dump object as a JSON representation
      return "(function(global){" \
           + "global.Locales = global.Locales || {};" \
           + "global.Locales." \
           + "})(window);" \
           + json.dumps(locale)