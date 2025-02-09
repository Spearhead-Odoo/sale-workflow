# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from lxml import etree

from odoo.addons.base.tests.common import BaseCommon


class TestSalePartnerSelectableOption(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_sale_order(self):
        result = self.env["sale.order"].get_view(
            self.env.ref("sale.view_order_form").id,
            "form",
        )
        doc = etree.XML(result["arch"])
        field = doc.xpath("//field[@name='partner_id']")
        domain = field[0].get("domain")
        self.assertTrue("('sale_selectable', '=', True)" in domain)
