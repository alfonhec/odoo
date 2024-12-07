{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "HA",
    'category': 'Category',
    'description': """
    Modulo de bienes raices
    """,
    # data files always loaded at installation
    'data': [
       'security/ir.model.access.csv',
       'views/views.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}