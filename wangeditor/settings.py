# -*- coding: utf-8 -*-
# @Author: theo-l
# @Date:   2017-08-04 20:40:57
# @Last Modified by:   theo-l
# @Last Modified time: 2017-08-04 22:45:21

"""
Image upload action configuration
# Refer: https://www.kancloud.cn/wangfupeng/wangeditor3/335782
"""
WANGEDITOR_IMG_CONFIG = {

    "showLinkImg": True,

    # only need to set the 1 of the following 2 items to enable editor uplaod image
    # if set both the first will have a high priority
    # 'uploadImgShowBase64': False,
    'uploadImgServer': 'wangeditor/upload/',

    # 'uploadImgMaxSize':5 * 1024 * 1024, # 5M default
    # 'uploadImgMaxLength': 10000, # default
    # 'uploadImgParams':{'token':'xxxxxx'},
    # 'uploadFileName':'your file name',
    # 'uploadImgHeaders':{'Accept':'text/x-json'},
    # 'withCredentials':True,
    # 'uploadImgTimeout': 5000, # 5s default
    # 'uploadImgHooks':{},

    # 'customAlert':'function',
    # 'customUploadImg':'function',

}
