# -*- coding: utf-8 -*-
# @Author: theo-l
# @Date:   2017-08-04 21:26:08
# @Last Modified by:   theo-l
# @Last Modified time: 2017-08-04 21:26:56

from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def image_upload(request):
    """
    This method return the wangEditor image upload data
    You should implement this method by your self
    {
    // errno 即错误代码，0 表示没有错误。
    //       如果有错误，errno != 0，可通过下文中的监听函数 fail 拿到该错误码进行自定义处理
    errno: 0,

    // data 是一个数组，返回若干图片的线上地址
    data: [
        '图片1地址',
        '图片2地址',
        '……'
    ]
}
    """
    if settings.DEBUG:
        print(request.FILES)
        data = {
            'errno': 0,
            'data': [
                "https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png"
            ]
        }
        return JsonResponse(data)
    raise NotImplementedError("You should implement this method by yourself in a real prod env!")
