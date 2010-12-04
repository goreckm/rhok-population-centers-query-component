import os
from google.appengine.ext.webapp import template

def render_template(template_file_name,
                    template_values = {}):
    new_template_values = { 'application': { 'name': 'Population Centers in Disaster',
                                             'media_url' : '/media/',
                                             'media_generated_url' : '/media-generated/' }
                          }
    new_template_values.update(template_values)
    
    path = os.path.join(os.path.dirname(__file__) + "/../../../templates/", template_file_name)
    return template.render(path, new_template_values);
