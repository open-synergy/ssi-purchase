# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    type_id = fields.Many2one(
        comodel_name='purchase_order_type',
        string='Type',
        required=True,
        readonly=True,
        states={
            "draft": [("readonly", False)],
        },
    )
