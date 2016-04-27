# -*- coding: utf-8 -*-

from flask import current_app, Markup
from flask import json
from werkzeug.urls import  url_encode
JSONEncoder = json.JSONEncoder


# RECAPTCHA_TEMPLATE = u'''
# <script src='%s' async defer></script>
# <div class="g-recaptcha" %s></div>
# '''



RECAPTCHA_TEMPLATE=u'''
<div id="captcha"></div>
    <script src="%s"></script>
				<script>
				    var handler = function (captchaObj) {
				         // 将验证码加到id为captcha的元素里
				         captchaObj.appendTo("#captcha");
				     };
				    $.ajax({
				        // 获取id，challenge，success（是否启用failback）
				        url: "/auth/getcaptcha",
				        type: "get",
				        dataType: "json", // 使用jsonp格式
				        success: function (data) {
				            // 使用initGeetest接口
				            // 参数1：配置参数，与创建Geetest实例时接受的参数一致
				            // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
				            initGeetest({
				                gt: data.gt,
				                challenge: data.challenge,
				                product: "embed", // 产品形式
				                offline: !data.success
				            }, handler);
				        }
				    });
				</script>
'''
__all__ = ["RecaptchaWidget"]


class RecaptchaWidget(object):

    def recaptcha_html(self):
        # html = current_app.config.get('RECAPTCHA_HTML')
        # if html:
        #     return Markup(html)
        script='http://static.geetest.com/static/tools/gt.js'
        # snippet = u' '.join([u'data-%s="%s"' % (k, attrs[k]) for k in attrs])
        return Markup(RECAPTCHA_TEMPLATE % (script))

    def __call__(self, field, error=None, **kwargs):
        """Returns the recaptcha input HTML."""



        return self.recaptcha_html()