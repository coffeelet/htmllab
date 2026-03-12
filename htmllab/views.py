import mimetypes
import os
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

        # 构建完整的 iframe URL（包含 host 和 port）
        scheme = request.scheme
        host = request.get_host()
        iframe_url = f"{scheme}://{host}/{current_page}"

        context = {
            'pages': pages,
            'current_page': current_page,
            'page_count': len(pages),
            'iframe_url': iframe_url,
            'host': host,
        }

        return render(request, 'manage.html', context)
