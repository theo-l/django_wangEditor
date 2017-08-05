# -*- coding: utf-8 -*-
# @Author: liang
# @Date:   2017-08-04 17:23:54
# @Last Modified by:   theo-l
# @Last Modified time: 2017-08-04 21:54:33

from __future__ import unicode_literals
from django.forms import widgets
from .settings import WANGEDITOR_IMG_CONFIG


class RichTextEditor(widgets.Textarea):
    template_name = 'wangeditor/richtext.html'

    def __init__(self, attrs=None, **kwargs):
        super(RichTextEditor, self).__init__(attrs)
        self.kwargs = kwargs or {}

    class Media:
        css = {
            'all': (
                ('css/wangEditor.css'),
            )
        }

        js = (
            ('js/wangEditor.js'),
        )

    def get_context(self, name, value, attrs):
        context = super(RichTextEditor, self).get_context(name, value, attrs)
        if value is None:
            value = ''
        context['widget']['value'] = value
        context['config'] = WANGEDITOR_IMG_CONFIG
        print("widget context: ", context)
        return context
