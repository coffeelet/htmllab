# HTML Lab 使用指南

欢迎使用 **HTML Lab**！这是一个简单的 Web 服务器模拟器，旨在帮助你学习和练习 HTML、CSS 和 JavaScript。

## 1. 快速开始

要启动本地开发服务器，请在项目目录中打开终端并运行：

```bash
python manage.py runserver 18000
```

服务器启动后，打开浏览器并访问：
[http://127.0.0.1:18000/](http://127.0.0.1:18000/)

## 2. 你的工作空间：`www/` 目录

`www/` 文件夹是你主要编写代码的地方。存放在此目录中的任何文件都会被 Web 服务器直接解析。

- **`index.html`**：这是你的网站首页。当你访问 `http://127.0.0.1:18000/` 时，默认会显示这个文件。
- **添加新文件**：你可以在此目录中创建新的 HTML、CSS 或 JS 文件。例如，如果你创建了 `about.html`，可以通过 `http://127.0.0.1:18000/about.html` 访问它。
- **子目录**：你可以通过文件夹来组织文件。如果你创建了 `css/style.css`，它的访问路径将是 `http://127.0.0.1:18000/css/style.css`。

## 3. 管理模式 (Management Mode)

HTML Lab 提供了一个**管理模式**，让你能够轻松地预览和切换所有页面。

访问地址：[http://127.0.0.1:18000/manage/](http://127.0.0.1:8000/manage/)

### 管理模式功能：
- **页面切换器**：通过下拉菜单快速切换 `www/` 目录下的所有 HTML 文件。
- **智能链接**：在管理模式下点击页面内的链接，会在管理界面内自动跳转，方便连续预览。
- **快捷链接**：快速访问 Bootstrap、jQuery 和 MDN Web 文档等学习资源。

## 4. 快速创建新页面

除了手动创建文件，你还可以使用内置命令基于 Bootstrap 5 模板快速生成一个新页面：

```bash
python manage.py createpage my-new-page --title "我的新页面标题"
```

这会自动在 `www/` 目录下生成 `my-new-page.html`。

## 5. 学习资源

本实验环境包含了一些内置的快速入门指南：

- **HTML 指南**：[http://127.0.0.1:8000/guide/html/](http://127.0.0.1:8000/guide/html/)
- **CSS 指南**：[http://127.0.0.1:8000/guide/css/](http://127.0.0.1:8000/guide/css/)
- **JS 指南**：[http://127.0.0.1:8000/guide/javascript/](http://127.0.0.1:8000/guide/javascript/)
- **Bootstrap 指南**：[http://127.0.0.1:8000/guide/bootstrap/](http://127.0.0.1:8000/guide/bootstrap/)
- **jQuery 指南**：[http://127.0.0.1:8000/guide/jquery/](http://127.0.0.1:8000/guide/jquery/)
- **颜色配色指南**：[http://127.0.0.1:8000/guide/colors/](http://127.0.0.1:8000/guide/colors/)


## 初学者小贴士
- 在刷新浏览器查看效果前，请确保已经保存了文件。
- 使用浏览器的“检查”工具（通常按 F12 或右键点击页面 > 检查）来调试你的 HTML 和 CSS。
- 如果页面无法加载，请检查运行 `python manage.py runserver 18000` 的终端窗口是否有错误提示。
