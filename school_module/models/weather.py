from odoo import models, fields, api
from odoo.exceptions import ValidationError, AccessError


class resSettings(models.TransientModel):
    _inherit = "res.config.settings"

    api_key = fields.Char("API KEY",config_parameter='school_module.api_key')

class weather(models.Model):
    _name = "weather.weather"

    name = fields.Char(string="Name of the City")
    temparature = fields.Char("Temparature")


    def weather_update(self):
        api_key = self.env['ir.config_parameter'].sudo().get_param('school_module.api_key')
        print("Api Key---------->>",api_key)

        import requests
        name = self.name
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q": f"{name}"}
        print("querystring----->>",querystring)

        headers = {
            "X-RapidAPI-Key": f"{api_key}",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(type(response))
        data = response.json()
        print("data------->>>",data)
        self.temparature = data['current']['temp_c']
        #     print(response.temp_c,"OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        #
        # print(response.json())



