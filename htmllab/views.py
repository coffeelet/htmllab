import mimetypes
import os
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.views import View


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
