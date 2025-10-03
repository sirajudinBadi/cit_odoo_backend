# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Caret IT Solutions Pvt. Ltd. (Website: www.caretit.com).           #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################
from odoo import models, fields, api


class TeamMember(models.Model):
    _name = "project.team.member"
    _description = "Project Team Member"

    name = fields.Char("Name", required=True, help="Name of the new team member")
    house_no = fields.Char("House No.", help="House No. for member's address")
    street = fields.Char("Street", help="Street Name for address")
    street2 = fields.Char("Street 2", help="Street 2 Name for address")
    country_id = fields.Many2one("res.country", "Country", required=True, help="Country of a member")
    state_id = fields.Many2one("res.country.state", "State", required=True, help="State of a member")
    city_id = fields.Many2one("res.state.city", "City")
    zip = fields.Char("Zip", required=True, help="Address ZIP/Postal Code")
    user_id = fields.Many2one(
        "res.users",
        required=True,
        help="User associated with this member",
        context = {"search_default_employee" : 1}
    )
    mobile = fields.Char(related='user_id.phone', string="Mobile", required=True, help="Personal Mobile number of a member")
    email = fields.Char(related="user_id.email", required=True, help="Email ID of a member fetched from user")
    gender = fields.Selection(
        selection=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        required=True,
        help="Gender of a member"
    )
    birth_date = fields.Date("Birth Date", help="Member's date of birth")
    user_image = fields.Binary("Image", help="Upload avatar image of a member")
    bio_data = fields.Html("Bio Data", help="Summarise the new member's bio")
    active = fields.Boolean("Active", default=True, help="Member status")
    timesheet_ids = fields.One2many(
        "account.analytic.line",
        "user_id",
        "Timesheets",
        help="Timesheets entries of a user"
    )

