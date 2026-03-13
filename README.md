# HTML Lab

HTML Lab是一个基于 Django 的 Web 服务器模拟器，可以直接解析和提供 www 目录下的静态文件（HTML、CSS、JavaScript）。 HTML Lab是给WEB初学者一个简单的学习工具。
让初学者更容易理解html, css, js以及服务器之间的关系。

## 功能特性

- **无需数据库**：直接读取文件系统，无需配置数据库
- **静态文件服务**：自动解析 HTML、CSS、JavaScript 文件
- **默认首页**：访问根路径自动加载 `www/index.html`
- **目录安全**：防止目录遍历攻击
- **MIME 类型自动识别**：根据文件扩展名自动设置 Content-Type
- **页面生成工具**：内置命令行工具快速创建新页面
- **管理模式**：可视化页面管理界面，通过 iframe 预览页面

## 项目结构

```
htmlLab/
├── manage.py              # Django 管理命令
├── htmllab/               # 项目配置目录
│   ├── management/        # 自定义管理命令
│   │   └── commands/
│   │       └── createpage.py  # 创建新页面命令
│   ├── templates/         # Django 模板目录
│   │   └── manage.html   # 管理模式界面模板
│   ├── static/            # 静态文件目录
│   │   ├── base.html     # 页面生成模板
│   │   ├── bootstrap/    # Bootstrap CSS/JS
│   │   └── jquery/       # jQuery 库
│   ├── settings.py        # Django 设置
│   ├── urls.py           # URL 路由配置
│   ├── views.py          # 静态文件视图
│   └── wsgi.py           # WSGI 配置
├── www/                   # Web 根目录
│   ├── index.html        # 默认首页
│   ├── style.css         # 样式文件
│   └── script.js         # JavaScript 文件
└── db.sqlite3            # SQLite 数据库（Django 必需，但项目不使用）
```

## 快速开始

### 0. 系统依赖

#### Python

建议使用 Python 3.13 (Only for django 5)

https://www.python.org/downloads/

#### IDE

推荐使用PyCharm, 下载链接

  https://www.jetbrains.com/pycharm/download/

### 1. 安装python依赖

**生产环境：**
```bash
pip install -r requirements.txt
```

**开发环境（包含测试和代码检查工具）：**
```bash
pip install -r requirements-dev.txt
```

或者手动安装最小依赖：
```bash
pip install django>=5.0
```

### 2. 运行开发服务器

```bash
python manage.py runserver
```

服务器启动后，访问 http://127.0.0.1:18000/ 即可查看默认首页。

### 3. 自定义内容

将您的静态文件放入 `www/` 目录：

- `www/index.html` - 默认首页
- `www/about.html` - 可通过 `/about.html` 访问
- `www/css/style.css` - 可通过 `/css/style.css` 访问
- `www/js/app.js` - 可通过 `/js/app.js` 访问

### 4. 创建新页面

使用内置命令快速创建新页面：

```bash
# 创建新页面（基于 htmllab/static/base.html 模板）
python manage.py createpage about

# 创建带自定义标题的页面
python manage.py createpage contact --title "联系我们"

# 使用其他模板文件
python manage.py createpage blog --template other_template.html --title "博客"
```

创建的文件将保存在 `www/` 目录，可直接通过浏览器访问。

**模板系统：**
- 默认模板：`htmllab/static/base.html` - 包含 Bootstrap 5 基础布局
- 模板使用 `{{PAGE_TITLE}}` 和 `{{PAGE_DESCRIPTION}}` 作为占位符
- 自定义模板需放在 `htmllab/static/` 目录下

### 5. 管理模式

访问管理模式界面，可视化管理和预览所有页面：

```
http://127.0.0.1:18000/manage/
```

**管理模式功能：**

- **页面预览**：使用 iframe 嵌套显示 HTML 页面
- **智能链接替换**：页面内的链接（如 `/index.html` 或 `about.html`）会自动替换为管理模式 URL（`http://localhost:18000/manage/?page=index.html`），点击后在管理界面内跳转
- **导航栏**：
  - **页面下拉菜单**：显示所有已创建的页面，点击切换预览
  - **Bootstrap 指南**：链接到 Bootstrap 官方文档
  - **jQuery 指南**：链接到 jQuery API 文档
  - **颜色指南**：链接到 Color Hunt 配色网站
  - **MDN 文档**：链接到 MDN Web 文档
- **实时预览**：自动显示 `www/` 目录下的所有页面
- **页面统计**：显示当前页面总数

## 使用示例

### 访问首页
```
http://127.0.0.1:18000/
```
自动加载 `www/index.html`

### 访问特定文件
```
http://127.0.0.1:18000/about.html
http://127.0.0.1:18000/css/style.css
http://127.0.0.1:18000/js/app.js
```

### 指定端口
```bash
python manage.py runserver 18000
```
访问 http://127.0.0.1:18080/

## 开发指南

### 运行测试

```bash
# 运行所有测试
python manage.py test

# 运行特定测试
python manage.py test htmllab.tests.StaticFileViewTest
```

### 代码规范

项目使用以下工具保持代码质量：

```bash
# 安装开发依赖
pip install flake8 black isort mypy

# 代码检查
flake8 htmllab/

# 代码格式化
black htmllab/

# 导入排序
isort htmllab/
```

更多开发规范请参考 [AGENTS.md](AGENTS.md)。

## 技术栈

- **后端框架**: Django 5.0.3
- **Python 版本**: 3.10+
- **数据库**: SQLite（仅用于 Django 启动，项目不使用）

## 许可证

MIT License
