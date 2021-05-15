# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class ZooCage(models.Model):
    _name = "zoo.cage"
    _description = "Zoo Cage"
    
    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    length = fields.Float('Length')
    width = fields.Float('Width')
    height = fields.Float('Height')
    description = fields.Text('Description')
    