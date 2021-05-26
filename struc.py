from pprint import pprint

struc_dic = {'my_project':
                 [{'settings':
                       ['__init__.py',
                        'dev.py',
                        'prod.py']},
                  {'mainapp':
                       ['__init__.py',
                        'models.py',
                        'views.py',
                        {'templates':
                             [{'mainapp':
                                   ['base.html',
                                    'index.html']}]}]},
                  {'authapp':
                       ['__init__.py',
                        'models.py',
                        'views.py',
                        {'templates':
                             [{'authapp':
                                   ['base.html',
                                    'index.html']}]}]}]}
pprint(struc_dic)

import yaml

to_yaml = struc_dic

with open('sw_templates.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)

with open('sw_templates.yaml') as f:
    print(f.read())
# my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
