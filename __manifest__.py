# -*- coding: utf-8 -*-
{
    'name': "Mercado",

    'summary': """
        Aplicación para Odoo 14 donde se recogen los productos ofertados en
        distintas tiendas de videojuegos.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mario Ortiz Jibaja",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/mercado_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/mercado_videojuego_report.xml',
        'reports/mercado_tienda_report.xml',
        'reports/mercado_impuesto_report.xml'
    ],
    'icon': 'static/description/logo2.png',
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
