from odoo import fields, models, api


class HelpdeskSetResponsable(models.TransientModel):
    _name = 'helpdesk.set.responsable'

    def set_responsable(self):
        self.ensure_one() # Para asegurarse de que solo se ejecuta para 1 registro
        ticket = False
        #ticket.responsable_id = self.env.user


