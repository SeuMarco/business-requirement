# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Business Requirement Deliverable Resource Template',
    'category': 'Business Requirements Management',
    'summary': """Manage default resource lines in your
               deliverable sales package from product template""",
    'version': '8.0.1.0.1',
    'website': 'https://www.elico-corp.com/',
    "author": "Elico Corp, Odoo Community Association (OCA)",
    'depends': [
        'business_requirement_deliverable',
    ],
    'image': [
        'static/description/icon.png',
        'static/img/bus_req_default.png',
        'static/img/bus_req_default2.png'
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/business_requirement_deliverable_default.xml",
    ],
    'demo': [
        'data/business_requirement_deliverable_resource_template_demo.xml'
    ],
    'license': 'AGPL-3',
    'installable': False,
}
