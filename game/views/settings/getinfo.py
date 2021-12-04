from django.http import JsonResponse
from game.models.player.player import Player

def getinfo_acapp(request):
    player = Player.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'username': player.user.username,
        'photo': player.photo,
    })


def getinfo_web(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'result': "未登录"
        })
    else:
        player = Player.objects.get(user=user)
        return JsonResponse({
            'result': "success",
            'username': player.user.username,
            'photo': player.photo,
        })

def getinfo(request):
    plateform = request.GET.get('platform')
    if plateform == "ACAPP":
        return getinfo_acapp(request)
    elif plateform == "WEB":
        return getinfo_web(request)