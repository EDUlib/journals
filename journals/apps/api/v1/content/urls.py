"""
Wagtail APIs
"""
from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.router import WagtailAPIRouter

wagtail_router = WagtailAPIRouter('content')

wagtail_router.register_endpoint('pages', PagesAPIEndpoint)
