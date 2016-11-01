#   Dietfacts Application
from openerp import models, fields

class Dietfacts_product_template(models.Model):
    _name='product.template'
    _inherit='product.template'

    calories = fields.Integer("Calories")
    servingsize = fields.Float("Serving Size")
    lastupdated =fields.Date("Last Updated")
    water=fields.Float("Type of Galoon")

