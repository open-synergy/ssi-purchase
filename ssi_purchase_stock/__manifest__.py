# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase + Inventory Integration",
    "version": "14.0.1.5.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_purchase",
        "purchase_stock",
        "ssi_m2o_configurator_mixin",
    ],
    "data": [
        "security/res_group_data.xml",
        "security/ir_rule_data.xml",
        "data/policy_template_data.xml",
        "views/stock_warehouse_views.xml",
        "views/purchase_order_views.xml",
        "views/purchase_order_type_views.xml",
    ],
    "demo": [],
}
