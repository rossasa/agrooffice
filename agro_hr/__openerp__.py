# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'AgroOffice Human Resources Management',
    'version': '0.1',
    'author': 'Proyecto Delice',
    'website': 'http://www.proyectodelice.es',
    'category': 'Project Management',
    'sequence': 10,
    'summary': 'Agriculture, Farms, HR, Payroll, Education & Certs',
    'images': [],
    'depends': [
        'hr', 'agro_base', 'agro_project',
    ],
    'description': """
Vertical Human Resources management for a Farm company
==============================================
    * Agro HR modules
      * Payroll using Timesheets
      * Education & certs
    """,
    'data': [
        'security/ir.model.access.csv',
        'agro_hr_edu_view.xml',
        'agro_hr_advance_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
