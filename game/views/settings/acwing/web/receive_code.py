from django.shortcuts import redirect
from django.core.cache import cache
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login
from game.models.player.player import Player
from random import randint

def receive_code(request):
    data = request.GET
    code = data.get('code')
    state = data.get('state')

    if not cache.has_key(state):
        return redirect("index")

    apply_access_token_url = "https://www.acwing.com/third_party/api/oauth2/access_token/"
    params = {
        'appid': "652",
        'secret': "76976c2a16c641dab5273c8f84fe15a0",
        'code': code
    }

    access_token_res = requests.get(apply_access_token_url, params).json()

    access_token = access_token_res['access_token']
    openid = access_token_res['openid']

    players = Player.objects.filter(openid=openid)
    if players.exists():
        login(request, players[0].user)
        return redirect("index")
    
    get_userinfo_url = "https://www.acwing.com/third_party/api/meta/identity/getinfo/"
    params = {
        "access_token": access_token,
        "openid": openid
    }

    userinfo_res = requests.get(get_userinfo_url, params=params).json()
    username = userinfo_res['username']
    photo = userinfo_res['photo']

    while User.objects.filter(username=username).exists():
        username += str(randint(0, 9))
    
    user = User.objects.create(username=username)
    player = Player.objects.create(user=user, photo=photo, openid=openid)

    login(request, user)

    return redirect("index")