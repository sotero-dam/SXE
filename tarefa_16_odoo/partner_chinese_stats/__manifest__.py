{
    'name': "Chinese Horoscope Stats",
    'summary': """
        Añade campos de fecha de nacimiento, edad y signo del horóscopo chino a los contactos.
    """,
    'description': """
        Módulo sencillo para extender las funcionalidades del módulo de Contactos
        (res.partner) añadiendo la fecha de nacimiento y campos calculados
        de edad y horóscopo chino.
    """,
    'author': "Kitty Cat",
    'website': "https://www.kittyweb.com",
    'category': 'Sales/CRM',
    'version': '1.0',

    'depends': ['base', 'contacts'], 

    'data': [

        'views/partner_views.xml', 
    ],
    
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}