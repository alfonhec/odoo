from odoo import models, fields

#from odooC.odoo.fields import Integer


class EstateProperty(models.Model):
    _name= "estate.property"
    _description = "Estate Property"

    name= fields.Char(string="Nombre de propiedad", required=True)
    description = fields.Text(string="Descripción")
    postcode = fields.Char(string="Código Postal")
    date_availability = fields.Date(string="Fecha de Disponibilidad")
    expected_price = fields.Float(string="Precio Esperado")
    selling_price = fields.Float(string="Precio de Venta")
    bedrooms = fields.Integer(string="Habitaciones")
    living_area = fields.Integer(string="Área Habitable")
    facades = fields.Integer(string="Fachadas")
    garage = fields.Boolean(string="Garaje")
    garden = fields.Char(string="Jardín")
    garden_area = fields.Integer(string="Área del Jardín")
    owner= fields.Char(string="Propietario")
    telephone= fields.Char(string="Nro. Telefono")


#    garden_orientation = fields.Selection(string="Orientación del Jardín")
