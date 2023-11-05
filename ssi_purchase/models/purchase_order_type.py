# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PurchaseOrderType(models.Model):
    _name = "purchase_order_type"
    _inherit = [
        'mixin.master_data',
    ]
    _description = "Purchase Order Type"
    _field_name_string = "Purchase Order Type"
