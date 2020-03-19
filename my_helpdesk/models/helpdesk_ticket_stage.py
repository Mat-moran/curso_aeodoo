from odoo import fields, models, api


class HelpdeskTicketStage (models.Model):
    _name = 'helpdesk.ticket.stage'
    _description = 'Description'

    name = fields.Char(string="Name", required=True, )



