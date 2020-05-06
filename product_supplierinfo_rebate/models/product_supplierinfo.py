# -*- coding: utf-8 -*-
# Copyright 2019 ForgeFlow
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    rebate_price = fields.Float(
        string="Rebate Price"
    )
    rebate_mult = fields.Float(
        compute='_compute_rebate_percent',
        store=True,
        digits=dp.get_precision('Product Price'),
        string='Rebate Mult.',
    )

    # instead of computing make something similar to sale_markup module

    rebate_discount = fields.Float(
        compute='_compute_rebate_percent',
        store=True,
        digits=dp.get_precision('Product Price'),
        string='Rebate Disc (%)',
    )

    @api.multi
    @api.depends('price', 'rebate_price')
    def _compute_rebate_percent(self):
        for line in self:
            if not (line.price and line.rebate_price):
                continue
            try:
                line.rebate_discount = (1 - (
                    line.rebate_price / line.price)) * 100
                line.rebate_mult = (line.rebate_price / line.price)
            except ZeroDivisionError:
                line.rebate_discount = 0.0
                line.rebate_mult = 0.0
