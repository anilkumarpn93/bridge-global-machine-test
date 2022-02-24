from django.urls import include, path
from .versioned.v1.urls import url_patterns

url_patterns = [
    path(r'v1/', include(url_patterns))
]
