"""
Management command to create a new HTML page in www directory.
Uses htmllab/static/base.html as template.
"""

import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create a new HTML page in www directory using base.html as template'

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            type=str,
            help='Name of the HTML file to create (e.g., about.html)'
        )
        parser.add_argument(
            '--title',
            type=str,
            default=None,
            help='Page title (default: uses filename without extension)'
        )
        parser.add_argument(
            '--template',
            type=str,
            default='base.html',
            help='Template file to use (default: base.html in htmllab/static/)'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        title = options['title']
        template_name = options['template']
        
        # Ensure filename has .html extension
        if not filename.endswith('.html'):
            filename += '.html'
        
        # Set default title if not provided
        if title is None:
            title = filename.replace('.html', '').replace('-', ' ').replace('_', ' ').title()
        
        # Define paths
        www_dir = Path(settings.WWW_DIR)
        static_dir = Path(settings.STATIC_DIR)
        template_path = static_dir / template_name
        target_path = www_dir / filename
        
        # Check if template exists
        if not template_path.exists():
            raise CommandError(
                f'Template file "{template_name}" not found in {static_dir}'
            )
        
        # Check if target file already exists
        if target_path.exists():
            raise CommandError(
                f'File "{filename}" already exists in www directory'
            )
        
        # Read template content
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
        except Exception as e:
            raise CommandError(f'Failed to read template: {e}')
        
        # Replace placeholders
        page_content = template_content.replace(
            '{{PAGE_TITLE}}',
            title
        )
        
        # Replace description
        page_content = page_content.replace(
            '{{PAGE_DESCRIPTION}}',
            f'Generated page: {title}'
        )
        
        # Write new file
        try:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(page_content)
        except Exception as e:
            raise CommandError(f'Failed to create file: {e}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created "{filename}" with title "{title}"'
            )
        )
        self.stdout.write(f'File location: {target_path}')
