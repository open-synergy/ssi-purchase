# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = [
        "purchase.order",
        "mixin.policy",
    ]

    qty_to_receive = fields.Float(
        string="Qty To Receive",
        compute="_compute_receive",
        store=True,
    )
    qty_received = fields.Float(
        string="Qty Received",
        compute="_compute_receive",
        store=True,
    )
    percent_received = fields.Float(
        string="Percent Received",
        compute="_compute_receive",
        store=True,
    )

    receive_product_ok = fields.Boolean(
        string="Can Receive Product",
        compute="_compute_policy",
        compute_sudo=True,
    )

    allowed_picking_type_ids = fields.Many2many(
        string="Allowed Deliver To",
        related="type_id.allowed_picking_type_ids",
    )

    @api.depends(
        "order_line",
        "order_line.qty_to_receive",
        "order_line.qty_received",
    )
    def _compute_receive(self):
        for record in self:
            qty_to_receive = qty_received = percent_received = 0.0
            for line in record.order_line:
                qty_to_receive += line.qty_to_receive
                qty_received += line.qty_received
            if qty_to_receive != 0.0:
                try:
                    percent_received = qty_received / qty_to_receive
                except ZeroDivisionError:
                    percent_received = 0.0
            record.qty_received = qty_received
            record.percent_received = percent_received
            record.qty_to_receive = qty_to_receive

    def _compute_policy(self):
        _super = super()
        _super._compute_policy()

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "receive_product_ok",
        ]
        res += policy_field
        return res

    def action_view_picking(self):
        _super = super()
        action = _super.action_view_picking()
        picking_id = action.get("res_id")
        if action and picking_id:
            picking = self.env["stock.picking"].browse(picking_id)
            if picking.picking_type_id and picking.picking_type_id.category_id:
                ctx = dict(action.get("context", {}))
                ctx["default_picking_type_category_id"] = (
                    picking.picking_type_id.category_id.id
                )
                action["context"] = ctx
        return action

    @api.onchange("company_id")
    def _onchange_company_id(self):
        self.picking_type_id = False

    @api.onchange("type_id")
    def _onchange_picking_type_id(self):
        self.picking_type_id = False
        if self.type_id and self.type_id.default_picking_type_id:
            self.picking_type_id = self.type_id.default_picking_type_id.id
