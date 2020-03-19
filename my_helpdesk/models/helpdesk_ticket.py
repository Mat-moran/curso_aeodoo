from odoo import fields, models,_


class HelpdeskTicket (models.Model):

    # Atributos
    _name = 'helpdesk.ticket'
    _description = 'Modulo para gestionar los tickets de soporte en Odoo.'

    # Campos
    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    date_deadline = fields.Datetime(string='Limit Date')
    team_id = fields.Many2one(comodel_name="helpdesk.team",
                              string="team",
                              required=False, )
    user_ids = fields.Many2many(comodel_name="res.users",
                                relation="helpdesk_ticket_user_rel",
                                column1="ticket_id",
                                column2="user_id",
                                string="Users", )
    responsable_id = fields.Many2one(comodel_name="res.users",
                                     string="Responsable", required=False, )

    def set_responsable(self):
        self.ensure_one() # Para asegurarse de que solo se ejecuta para 1 registro
        self.responsable_id = self.env.user
    


