# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrderType(models.Model):
    _inherit = "purchase_order_type"

    def _get_domain(self):
        domain = "[('code','=','incoming')]"
        return domain

    picking_type_selection_method = fields.Selection(
        default="domain",
        selection=[("manual", "Manual"), ("domain", "Domain"), ("code", "Python Code")],
        string="Deliver To Selection Method",
        required=True,
    )
    picking_type_domain = fields.Text(
        string="Deliver To Domain",
        default="[]",
    )
    picking_type_python_code = fields.Text(
        string="Deliver To Python Code",
        default="result = []",
    )
    allowed_picking_type_ids = fields.Many2many(
        string="Allowed Deliver To",
        comodel_name="stock.picking.type",
        relation="picking_type_2_purchase_order_type_rel",
        column1="type_id",
        column2="picking_type_id",
        domain=lambda x: x._get_domain(),
    )
    default_picking_type_id = fields.Many2one(
        comodel_name="stock.picking.type",
        string="Default Deliver To",
        domain="[('id', 'in', allowed_picking_type_ids)]",
    )
