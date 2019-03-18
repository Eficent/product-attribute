# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    template_code = fields.Char(
        string='Template Reference',
        default=lambda self: self.default_code
    )

    @api.multi
    def name_get(self):
        return [(template.id, '%s%s' % (
            template.default_code and '[%s] ' % template.default_code or
            template.template_code and '[%s] ' % template.template_code or '',
            template.name)) for template in self]
