from django.http import JsonResponse
from urllib.parse import quote
from random import randint
from django.core.cache import cache
from django.shortcuts import redirect

def get_state():
    res = ""
    for i in range(8):
        res += str(randint(0, 9))
    return res

def apply_code(request):
    appid = "652"
    redirect_uri = quote("https://app652.acapp.acwing.com.cn/settings/acwing/acapp/receive_code")
    scope = "userinfo"
    state = get_state()

    cache.set(state, True, 7200)  # 有效期2小时
    
    return JsonResponse({
        'result': "success",
        'appid': appid,
        'redirect_uri': redirect_uri,
        'scope': scope,
        'state': state,
    })