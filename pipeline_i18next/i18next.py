import yaml
import json
from django.conf import settings

from pipeline.compilers import CompilerBase

class I18nextCompiler(CompilerBase):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.yml')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # No need to recompiled file
        f = open(infile, 'rb')
        # Load the file as a Python Object
        translation = yaml.load(f)
        f.close()
        # Parse out the name of the locale
        locale = unicode.rsplit(infile, '/', 1)[1].strip('.yml')
        # Dump object as a JSON representation
        jsonString = json.dumps(translation)

        # Create Output
        out =  u'(function(global){{' \
               u'global.{0} = global.{0} || {{}};' \
               u'global.{0}.{1} = {{ translation: {2} }};' \
               u' }})(window);'.format(
            getattr(settings, 'PIPELINE_I18NEXT_NAMESPACE', 'Locales'),
            locale,
            jsonString)

        newFile = open(outfile, 'wb')
        newFile.write(out)
        newFile.close()
        # Compiled
        return True