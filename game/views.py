from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Falioss.gcores.com%2Fuploads%2Fimage%2F13c926bc-01c2-4c56-b532-ed2da92d1423_watermark.png&refer=http%3A%2F%2Falioss.gcores.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1638769162&t=4dd2001d10f16349323197fbe6d0a807", width = 1500>'
    line3 = '<hr>'
    line4 = '<a href = "/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.52miji.com%2Fimage%2F2016%2F09%2F23%2F146e29c3c001304525aa6aeb40485faa.jpg&refer=http%3A%2F%2Fimg.52miji.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1638771673&t=a9193cf9b5a97e0ebab65b248c16d291">'
    line3 = '<a href = "/">返回主界面</a>'
    return HttpResponse(line1 + line3 + line2)
