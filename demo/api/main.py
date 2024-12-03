"""
API setup.
"""
from django.contrib.auth.decorators import user_passes_test
from ninja import NinjaAPI

from .services import register_error_handlers
from ninja.security import SessionAuth

from polls.api.endpoints import router as polls_router


api = NinjaAPI(
    title="Auto Ninja",
    description="Automatically generated API",
    auth=SessionAuth(),
    docs_url="/",
    docs_decorator=user_passes_test(lambda user: user.is_staff),
    urls_namespace="api",
)
register_error_handlers(api)


api.add_router("", polls_router)

