# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields


class MassStageUpdate(models.TransientModel):
    _name = 'mass.stage.update'
    _description = 'Mass Stage Update'

    stage_id = fields.Many2one('crm.stage', string='Stage', required=True)
        


    def action_update(self):
        active_ids = self.env.context.get('active_ids', [])
        leads = self.env['crm.lead'].browse(active_ids)
        for lead in leads:
            lead.stage_id = self.stage_id.id
        return {'type': 'ir.actions.act_window_close'}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
