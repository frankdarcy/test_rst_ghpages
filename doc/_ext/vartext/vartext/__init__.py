# Support replacement of text in RST files as specified in 
# vartext_replacements, a dictionary with...
# key: the text to find the RST files
# value: the text to insert in place of the key

def processReplacements(app, docname, source):
    result = source[0]
    for key in app.config.vartext_replacements:
        result = result.replace(key, app.config.vartext_replacements[key])
    source[0] = result

def setup(app):
   app.add_config_value('vartext_replacements', {}, True)
   app.connect('source-read', processReplacements)
