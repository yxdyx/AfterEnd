# AfterEnd

> 均采用面向对象形式

都采用面向对象的方法，不要直接写方法

> 项目结构

1.model: 数据库对象（mysql，mongodb（暂时不用），redis（缓存））

2.utils: 工具类，数据流转文件存储、图片url地址设置

3.service: 业务逻辑（注册信息的处理，从数据获取的对象进行相应数据格式化（json），信息安全验证......）

4.static: 存放网页静态资源的文件夹

5.templates: 存放网页文件（html）文件

> 后端进度

1.2018-4-9
在admin内增加录入主席照片的功能
由于使用了ImageField，到时候环境需要安装pillow