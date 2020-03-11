from odoo import fields, models,_


class HelpdeskTicket (models.Model):

    # Atributos
    _name = 'helpdesk.ticket'
    _description = 'Moodulo para gestionar los tickets de soporte en Odoo.'

    # Campos
    name = fields.Char(string='Name',required=True)
    desription = fields.Text(string='Description')
    date_deadline = fields.Datetime(string='Limit Date')
    


