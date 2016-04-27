from wtforms.fields import Field

from . import widgets
from .validators import Recaptcha

__all__ = ["RecaptchaField"]


class RecaptchaField(Field):
    widget = widgets.RecaptchaWidget()

    # error message if recaptcha validation fails
    recaptcha_error = None

    def __init__(self,  captacha_id,private_key,label='',validators=None,**kwargs):
        validators = validators or [Recaptcha(captacha_id,private_key)]
        super(RecaptchaField, self).__init__(label, validators, **kwargs)