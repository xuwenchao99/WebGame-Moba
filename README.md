# WebGame-Moba

这是基于AcWing的《Django 框架课》制作而成的。项目采用前后端分离的形式，前端纯js实现，并交给客户端进行渲染，而后端则采用Django框架和thrift去实现。最终目的是实现一个简化版的MOBA类游戏。



## 功能

<table>
    <tr>
        <th>界面</th><th>功能模块</th><th>所用技术</th>
    </tr>
    <tr>
        <td rowspan="4">登录界面</td> 
        <td>登录功能</td><td></td>
    </tr>
    <tr>
        <td>注册功能</td><td></td>
    </tr>
    <tr>
        <td>AcWing Web端一键授权登录</td><td>Oauth2</td>
    </tr>
    <tr>
        <td>AcWing App端一键授权登录</td><td>Oauth2</td>
    </tr>
    <tr>
        <td rowspan="6">菜单界面</td>
        <td>单人模式</td><td></td>
    </tr>
    <tr>
        <td rowspan="4">联机对战</td>
        <td>多人同屏（websocket）</td>
    </tr>
    <tr>
        <td>聊天功能（websocket）</td>
    </tr>
    <tr>
        <td>计分功能（websocket、Redis）</td>
    </tr>    
    <tr>
        <td>匹配系统（thrift、Redis）</td>
    </tr>
    <tr>
        <td>退出</td><td></td>
    </tr>
    <tr>
        <td rowspan="3">游戏界面</td>
        <td>地图渲染</td><td>JavaScript</td>
    </tr>
    <tr>
        <td>人物控制</td><td>JavaScript</td>
    </tr>
    <tr>
        <td>交互模式</td><td>JavaScript</td>
    </tr>    
</table>



## 展示界面
登录界面：

![登录界面](https://raw.githubusercontent.com/Fool-coder/PicGo/master/AcWing%20WebGame/%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.png)


注册界面：

![注册界面](https://raw.githubusercontent.com/Fool-coder/PicGo/master/AcWing%20WebGame/%E6%B3%A8%E5%86%8C%E7%95%8C%E9%9D%A2.png)

AcWing一键授权登录：

![AcWing一键登录功能](https://raw.githubusercontent.com/Fool-coder/PicGo/master/AcWing%20WebGame/AcWing%E4%B8%80%E9%94%AE%E6%8E%88%E6%9D%83%E7%99%BB%E5%BD%95.png)

菜单界面：

![菜单界面](https://raw.githubusercontent.com/Fool-coder/PicGo/master/AcWing%20WebGame/%E8%8F%9C%E5%8D%95%E7%95%8C%E9%9D%A2.png)

单人模式：

![单人模式](https://raw.githubusercontent.com/Fool-coder/PicGo/master/AcWing%20WebGame/%E5%8D%95%E4%BA%BA%E6%A8%A1%E5%BC%8F.png)

多人模式：

![多人模式](https://raw.githubusercontent.com/Fool-coder/PicGo/master/AcWing%20WebGame/%E5%A4%9A%E4%BA%BA%E6%A8%A1%E5%BC%8F.PNG)


## 启动项目

### 环境配置

启动`nginx`、`thrift`与`redis`服务：

```bash
sudo /etc/init.d/nginx start
```

```bash
cd match_system/src/
chmod +x main.py
./main.py
```

```bash
sudo redis-server /etc/redis/redis.conf
```
### 服务启动

启动`uwsgi`与`django_channels`服务：

```bash
uwsgi --ini scripts/uwsgi.ini
```

```bash
daphne -b 0.0.0.0 -p 5015 acapp.asgi:application
```

启动项目前请确保服务器的`43`、`80`与`启动项目`端口开放

启动项目：

```bash
python3 manage.py runserver 0.0.0.0:端口号
```
