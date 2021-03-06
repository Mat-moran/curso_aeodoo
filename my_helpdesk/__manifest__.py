# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.orglicenses/agpl.html)
{
    'name': 'HelpDesk-curso',
    'version': '13.0.0.0.0',
    'summary': 'Módulo para gestionar problemas, garantías, etc...',
    'category': 'Customer Relationship Management',
    'author': 'Amadeo Morán Guerrero',
    'maintainer': 'Amadeo Morán Guerrero',
    'license':'AGPL-3',
    'data':[
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'wizard/helpdesk_set_responsable_view.xml',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_ticket_stage.xml',
        'views/helpdesk_team.xml',
        'views/res_user_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
