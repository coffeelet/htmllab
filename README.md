# HTML Lab

一个基于 Django 的 Web 服务器模拟器，可以直接解析和提供 www 目录下的静态文件（HTML、CSS、JavaScript）。

## 功能特性

- **无需数据库**：直接读取文件系统，无需配置数据库
- **静态文件服务**：自动解析 HTML、CSS、JavaScript 文件
- **默认首页**：访问根路径自动加载 `www/index.html`
- **目录安全**：防止目录遍历攻击
- **MIME 类型自动识别**：根据文件扩展名自动设置 Content-Type

## 项目结构

```
htmlLab/
├── manage.py              # Django 管理命令
├── htmllab/               # 项目配置目录
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

### 1. 安装依赖

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

服务器启动后，访问 http://127.0.0.1:8000/ 即可查看默认首页。

### 3. 自定义内容

将您的静态文件放入 `www/` 目录：

- `www/index.html` - 默认首页
- `www/about.html` - 可通过 `/about.html` 访问
- `www/css/style.css` - 可通过 `/css/style.css` 访问
- `www/js/app.js` - 可通过 `/js/app.js` 访问

## 使用示例

### 访问首页
```
http://127.0.0.1:8000/
```
自动加载 `www/index.html`

### 访问特定文件
```
http://127.0.0.1:8000/about.html
http://127.0.0.1:8000/css/style.css
http://127.0.0.1:8000/js/app.js
```

### 指定端口
```bash
python manage.py runserver 8080
```
访问 http://127.0.0.1:8080/

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

- **后端框架**: Django 6.0.3
- **Python 版本**: 3.10+
- **数据库**: SQLite（仅用于 Django 启动，项目不使用）

## 许可证

MIT License
