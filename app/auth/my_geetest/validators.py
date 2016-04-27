try:
    import urllib2 as http
except ImportError:
    # Python 3
    from urllib import request as http

from flask import request, current_app,session

from wtforms import ValidationError
from werkzeug.urls import url_encode
from flask.ext.wtf._compat import to_unicode,to_bytes
from geetest import GeetestLib
import json





__all__ = ["Recaptcha"]


class Recaptcha(object):
    """Validates a ReCaptcha."""

    def __init__(self, captcha_id,private_key,message=None):
        self.captcha_id=captcha_id
        self.private_key=private_key
    def __call__(self, form, field):
        gt = GeetestLib(self.captcha_id, self.private_key)
        challenge = request.form[gt.FN_CHALLENGE]
        validate = request.form[gt.FN_VALIDATE]
        seccode = request.form[gt.FN_SECCODE]
        status = session[gt.GT_STATUS_SESSION_KEY]
        user_id = session["random_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        result = True if result else False
        if not result:
            raise ValidationError()
        return result

