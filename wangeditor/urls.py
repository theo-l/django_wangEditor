# -*- coding: utf-8 -*-
# @Author: theo-l
# @Date:   2017-08-04 20:42:49
# @Last Modified by:   theo-l
# @Last Modified time: 2017-08-04 21:46:09

from django.conf.urls import url
from .settings import WANGEDITOR_IMG_CONFIG

from . import views


urlpatterns = [
    url(r'{}'.format(WANGEDITOR_IMG_CONFIG['uploadImgServer']), views.image_upload, name='editor-img-upload')
]
