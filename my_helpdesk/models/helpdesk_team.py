from odoo import fields, models, api


class HelpdeskTeam (models.Model):
    _name = 'helpdesk.team'
    _description = 'Description'

    name = fields.Char(string="Name", required=False, )
    ticket_ids = fields.One2many(comodel_name="helpdesk.ticket",
                                 inverse_name="team_id",
                                 string="Tickets", required=False, )

    team_users_ids = fields.Many2many(comodel_name="res.users",
                                      relation="team_users_rel",
                                      column1="team_id",
                                      column2="users_id",
                                      string="Users", )

    


