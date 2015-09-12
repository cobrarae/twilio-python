# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.pricing.phone_number.country import (
    Countries,
    Country,
)


class PhoneNumber(NextGenInstanceResource):
    """
    .. attribute:: name
    
        The name
    
    .. attribute:: url
    
        The url
    
    .. attribute:: links
    
        The links
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(PhoneNumber, self).__init__(parent, None)


class PhoneNumbers(NextGenListResource):
    name = "PhoneNumbers"
    mount_name = "phone_numbers"
    key = "phone_numbers"
    instance = PhoneNumber

    def __init__(self, *args, **kwargs):
        super(PhoneNumbers, self).__init__(*args, **kwargs)
        self.countries = Countries(*args, **kwargs)

    def load_instance(self, data):
        """ Override because PhoneNumber does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance