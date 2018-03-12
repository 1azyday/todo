## TODO——基于Socket的自制Web框架
* 底层Socket，实现对HTTP协议各类请求的解析、调取。框架实现Cookies、Session、静态文件读取等功能。
* MVC架构，解耦业务逻辑和表现逻辑。（M）实现数据CURD操作的ORM，以json格式存于本地；（V）页面采用Jinja模板，由路由函数最终传参渲染；（C）自制框架负责解析请求，调取相应的路由函数来实现数据操作，并返回用户视图给客户端。
* 实现了user的基本功能（登录注册、权限控制，用户记录），用户密码加盐hash保存保存。
* 实现了todo的基本功能（新增、编辑、删除）。
* 前后端分离，通过后端api接口，负责数据交互。
* 页面数据修改，实现基于ajax技术的异步刷新，无需手动刷新页面。


- ### 注册登录

    ![image](https://github.com/1azyday/todo/blob/master/README/%E7%99%BB%E5%BD%95%E6%B3%A8%E5%86%8C.gif)

- ### 新增todo

    ![image](https://github.com/1azyday/todo/blob/master/README/%E6%96%B0%E5%A2%9E.gif)

- ### 编辑删除

    ![image](https://github.com/1azyday/todo/blob/master/README/%E7%BC%96%E8%BE%91%E5%88%A0%E9%99%A4.gif)
