import mimetypes
import os
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.views import View


class StaticFileView(View):
    """提供 www 目录下的静态文件"""
    
    def get(self, request, path=''):
        www_dir = Path(settings.WWW_DIR)
        
        # 如果路径为空，使用 index.html
        if not path:
            path = 'index.html'
        
        # 构建完整的文件路径
        file_path = www_dir / path
        
        # 安全检查：确保文件在 www 目录内
        try:
            file_path.resolve().relative_to(www_dir.resolve())
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
