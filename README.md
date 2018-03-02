# SportShop电商网站

## 依赖库
* Python 2.7
* Django 1.8
* Pillow
* Jieba


## 实现功能
#### 管理员（商家）
1、 商品管理页

* 商品发布
* 商品删除

2、 订单管理页

* 查看订单列表
* 查看订单详情
* 对订单进行发货操作

#### 顾客
1、商城首页

* 商品搜索（按标题模糊搜索）
* 按类别浏览商品

2、商品详情页

* 选择尺寸、颜色、数量
* 加入购物车

3、购物车

* 删除商品
* 结算（省略了付款流程...）

4、我的订单

* 取消订单（未发货状态下）
* 确认收货（已发货状态下）

5、个人中心

* 收货地址管理



## 项目配置
### 创建虚拟环境（可选）

1. 安装Virtualenv

```
pip install virtualenv
```

2. 创建虚拟环境

```
virtualenv env
```

3. 启动虚拟环境

```
source env/bin/activate
```

### 数据库

创建并同步数据模型 
```
python manage.py makemigrations
python manage.py migrate
```

### 设置URL路由

修改settings.py

### 静态文件配置
1. 在settings.py中添加 STATIC_URL = '/static/'
2. 在SportShop根目录下添加static文件夹，用于放置静态文件
3. 在模板中引用静态文如下	

```
<!-- Bootstrap -->
    {% load static %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'css/dashboard.css' %}" rel="stylesheet">
```

### 媒体文件配置
1. 在settings.py中添加 STATIC_URL = '/static/'

```
MEDIA_ROOT = 'media/'

MEDIA_URL = 'media/'
```
2. urls.py进行如下修改

```
urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

