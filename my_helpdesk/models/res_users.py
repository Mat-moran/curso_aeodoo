from odoo import fields, models, api


class ResUsers (models.Model):
    _inherit = 'res.users'

    helpdesk_code = fields.Char(string="Helpdesk Code",
                                required=False, )
    ticket_ids = fields.Many2many(comodel_name="helpdesk.ticket",
                                  relation="helpdesk_ticket_user_rel",
                                  column1="user_id",
                                  column2="ticket_id",
                                  string="Tickets", )

