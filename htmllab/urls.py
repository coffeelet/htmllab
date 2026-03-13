"""
URL configuration for htmllab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from htmllab.views import (
    StaticFileView,
    ManageView,
    ManagePageView,
    GuideBootstrapView,
    GuideHtmlView,
    GuideCssView,
    GuideJavascriptView,
    GuideJqueryView,
    GuideColorsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 管理模式主页面
    path('manage/', ManageView.as_view(), name='manage'),
    # 管理模式页面代理（处理 HTML 链接替换）
    path('manage/page/<str:page>', ManagePageView.as_view(), name='manage_page'),
    # 指南页面
    path('guide/bootstrap/', GuideBootstrapView.as_view(), name='guide_bootstrap'),
    path('guide/html/', GuideHtmlView.as_view(), name='guide_html'),
    path('guide/css/', GuideCssView.as_view(), name='guide_css'),
    path('guide/javascript/', GuideJavascriptView.as_view(), name='guide_javascript'),
    path('guide/jquery/', GuideJqueryView.as_view(), name='guide_jquery'),
    path('guide/colors/', GuideColorsView.as_view(), name='guide_colors'),

    # 根路径 - 显示 index.html
    path('', StaticFileView.as_view(), name='index'),
    # 匹配 www 目录下的所有文件
    re_path(r'^(?P<path>.*)$', StaticFileView.as_view(), name='static_file'),
]
