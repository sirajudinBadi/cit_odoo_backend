# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
{
    'name': 'Project Team',
    'summary': 'Project management module covering teams and member operations',
    'description': '''Aims to manage the operations of team and member for project.''',
    'version': '19.0.1.0',
    'author': 'Caret It Solutions PVT. LTD.',
    'category': 'Project',
    'website': 'https://caretit.com',
    'depends': ["base", 'project'],
    "installable" : True,
    "application" : True,
    'data': [
        "security/ir.model.access.csv",
        "demo/demo_cities.xml",
        "views/project_team_member_menus_action.xml",
        "views/project_team_member_views.xml",
    ],
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    "assets" : {
        "web.assets_backend" : [
            "cit_project_team/static/src/css/styles.css",
        ]
    }
}

