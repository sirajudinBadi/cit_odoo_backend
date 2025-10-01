# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
from odoo import models, api, fields

class StateCity(models.Model):
    _name = "res.state.city"
    _description = "State City"
    _order = 'name'

    name = fields.Char("City")
    state_id = fields.Many2one("res.country.state", string="State", required=True)
    country_id = fields.Many2one("res.country", string="Country", required=True)
