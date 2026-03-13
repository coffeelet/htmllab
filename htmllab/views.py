import mimetypes
import os
import re
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator


@method_decorator(xframe_options_exempt, name='dispatch')
class StaticFileView(View):
    """提供 www 目录和 static 目录下的静态文件"""
    
    def get(self, request, path=''):
        # 检查是否是 static 目录请求
        if path.startswith('static/'):
            # 移除 'static/' 前缀
            relative_path = path[7:]  # len('static/') = 7
            base_dir = Path(settings.STATIC_DIR)
        else:
            # 使用 www 目录
            base_dir = Path(settings.WWW_DIR)
            # 如果路径为空，使用 index.html
            if not path:
                path = 'index.html'
            relative_path = path
        
        # 构建完整的文件路径
        file_path = base_dir / relative_path
        
        # 安全检查：确保文件在 base_dir 目录内
        try:
            file_path.resolve().relative_to(base_dir.resolve())
        except ValueError:
            raise Http404("访问被拒绝")
        
        # 检查文件是否存在且是文件
        if not file_path.exists() or not file_path.is_file():
            raise Http404("文件未找到")
        
        # 获取文件的 MIME 类型
        content_type, encoding = mimetypes.guess_type(str(file_path))
        if content_type is None:
            content_type = 'application/octet-stream'
        
        # 返回文件
        return FileResponse(
            open(file_path, 'rb'),
            content_type=content_type,
            as_attachment=False
        )


class ManageView(View):
    """管理模式视图 - 使用 iframe 显示 HTML 页面"""

    def get(self, request):
        """处理 GET 请求"""
        # 获取当前要显示的页面（通过 query string）
        current_page = request.GET.get('page', 'index.html')

        # 扫描 www 目录获取所有 HTML 页面列表
        www_dir = Path(settings.WWW_DIR)
        pages = []

        if www_dir.exists():
            for file_path in www_dir.iterdir():
                if file_path.is_file() and file_path.suffix == '.html':
                    pages.append({
                        'name': file_path.stem,
                        'filename': file_path.name,
                        'title': file_path.stem.replace('-', ' ').replace('_', ' ').title()
                    })

        # 按名称排序
        pages.sort(key=lambda x: x['name'])

        # 构建完整的 iframe URL（使用管理模式的代理URL）
        scheme = request.scheme
        host = request.get_host()
        iframe_url = f"{scheme}://{host}/manage/page/{current_page}"

        context = {
            'pages': pages,
            'current_page': current_page,
            'page_count': len(pages),
            'iframe_url': iframe_url,
            'host': host,
        }

        return render(request, 'manage.html', context)

class GuideBootstrapView(View):
    """Bootstrap 5 快速指南视图"""

    def get(self, request):
        return render(request, 'guide/bootstrap.html')


class GuideHtmlView(View):
    """HTML 快速指南视图"""

    def get(self, request):
        return render(request, 'guide/html.html')


class GuideCssView(View):
    """CSS 快速指南视图"""

    def get(self, request):
        return render(request, 'guide/css.html')


class GuideJavascriptView(View):
    """JavaScript 快速指南视图"""

    def get(self, request):
        return render(request, 'guide/javascript.html')


class GuideJqueryView(View):
    """jQuery 快速指南视图"""

    def get(self, request):
        return render(request, 'guide/jquery.html')


class GuideColorsView(View):
    """Web 颜色指南视图"""

    def get(self, request):
        return render(request, 'guide/colors.html')


@method_decorator(xframe_options_exempt, name='dispatch')
class ManagePageView(View):
    """管理模式页面代理视图 - 返回处理后的 HTML 内容，替换内部链接"""

    def get(self, request, page):
        """处理 GET 请求，返回处理后的 HTML"""
        www_dir = Path(settings.WWW_DIR)
        file_path = www_dir / page
        
        # 安全检查：确保文件在 www 目录内
        try:
            file_path.resolve().relative_to(www_dir.resolve())
        except ValueError:
            raise Http404("访问被拒绝")
        
        # 检查文件是否存在且是文件
        if not file_path.exists() or not file_path.is_file():
            raise Http404("文件未找到")
        
        # 检查是否是 HTML 文件
        if file_path.suffix != '.html':
            # 非 HTML 文件直接返回
            content_type, _ = mimetypes.guess_type(str(file_path))
            if content_type is None:
                content_type = 'application/octet-stream'
            return FileResponse(
                open(file_path, 'rb'),
                content_type=content_type
            )
        
        # 读取 HTML 内容
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except Exception:
            raise Http404("无法读取文件")
        
        # 获取当前 host 用于构建管理 URL
        scheme = request.scheme
        host = request.get_host()
        manage_base_url = f"{scheme}://{host}/manage/"
        
        # 扫描 www 目录获取所有 HTML 页面
        www_dir = Path(settings.WWW_DIR)
        html_pages = set()
        if www_dir.exists():
            for f in www_dir.iterdir():
                if f.is_file() and f.suffix == '.html':
                    html_pages.add(f.name)
                    html_pages.add(f'/{f.name}')  # 带斜杠的版本
        
        # 替换 HTML 中的链接
        # 处理指向 HTML 文件的 <a> 标签，添加 target="_parent"
        # 替换 HTML 中的链接
        def replace_link(match):
            """替换链接并添加 target=_parent"""
            full_tag = match.group(0)
            attrs = match.group(1)

            # 提取 href 值
            href_match = re.search(r'href=["\']([^"\']+)["\']', attrs)
            if not href_match:
                return full_tag

            href = href_match.group(1)

            # 忽略外部链接、锚点和 javascript:
            if any(href.startswith(p) for p in ['http://', 'https://', '#', 'javascript:', 'mailto:', 'tel:']):
                return full_tag

            # 规范化路径：去掉开头的 ./ 和 /
            path_part = href.split('?')[0].split('#')[0]
            href_normalized = path_part.lstrip('./')
            if href_normalized.startswith('/'):
                href_normalized = href_normalized[1:]

            # 检查是否指向 HTML 页面
            is_html = href_normalized.endswith('.html') or ('.' not in href_normalized and href_normalized != '')

            if is_html:
                # 检查是否在 www 目录中
                page_filename = href_normalized if href_normalized.endswith('.html') else f"{href_normalized}.html"

                # 如果这个文件确实存在，则重写为管理链接
                if page_filename in html_pages:
                    manage_url = f"/manage/?page={page_filename}"
                    new_attrs = re.sub(r'href=["\'][^"\']+["\']', f'href="{manage_url}"', attrs)

                    # 强制添加 target="_parent"
                    if 'target=' in new_attrs.lower():
                        new_attrs = re.sub(r'target=["\'][^"\']+["\']', 'target="_parent"', new_attrs, flags=re.IGNORECASE)
                    else:
                        new_attrs = new_attrs.rstrip() + ' target="_parent"'

                    return f'<a{new_attrs}>'

            return full_tag
        # 使用正则表达式匹配所有 <a> 标签
        # 匹配 <a ...> 但不包括 > 在属性值中的情况
        html_content = re.sub(r'<a([^>]+)>', replace_link, html_content)
        
        # 返回处理后的 HTML
        return HttpResponse(html_content, content_type='text/html; charset=utf-8')
