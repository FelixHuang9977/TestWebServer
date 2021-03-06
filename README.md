## TestWebServer
2018.5.10更新。

架构：Nginx + Gunicorn + Django（MySQL），前端使用React + Axios，在Nanopi-Neo上测试。

以后会使用Nanopi2 fire做单独的Nginx 负载均衡服务器

## 进度安排：
- [X] 搭建环境，完成MySQL、Nginx配置
- [X] Django 后端简单搭建
- [X] 完全的前后端分离
- [X] 实现前端发送用户名与密码到后端（axios post）
- [X] 实现后端将用户验证数据返回到前端
- [X] ~~Toast适配~~ 使用Span标签来进行警告与提示
- [X] 考虑传输的安全问题(CSRF Solved)
- [X] 实现登陆后的跳转(使用React-Router)
- [X] 使用Redux来实现登陆后鉴权信息保存（未鉴权的用户将会被redirect到home）
- [X] 实现多页面跳转
- [X] 实现前端注册与登录功能
- [X] 实现较复杂后端逻辑
- [X] 注册功能进一步完善
- [ ] Nginx未发现静态资源，向后端Django发起请求获得资源
- [X] 使用cookies来实现不登录即可访问信息（optional）
- [ ] 完善HomeView，实现一些其他功能
- [X] WebPack学习&精简

- 已知问题：
	1. 实验服务器Nginx 用户为 root（不为默认的www-data），MySQL的django用户权限过大（update这个权限应该进一步限制在固定的表内，而不为全部的库权限）。
	2. SecretKey没有特别好的解决方法。
