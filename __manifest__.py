# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name':'Crm Mass Stage Update',
    'version': '18.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Tools',
    'description':
        """
        This Module add below functionality into odoo

        - Crm Mass Stage Update\n

    """,
    'summary': 'Crm Mass Stage Update',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/mass_stage_update.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:








