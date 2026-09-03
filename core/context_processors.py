from core.access import get_user_role
from core.services import get_brand
from core.menu import get_menus_for_role
from core.breadcrumb import get_breadcrumb_title


def core_context(request):
    role = get_user_role(request.user)
    menus = get_menus_for_role(role) if role else []
    brand = get_brand()
    breadcrumb_title = get_breadcrumb_title(request, menus)
    return {
        "brand": brand,
        "menus": menus,
        "breadcrumb_title": breadcrumb_title,
        "developer_name": "GALA SAGALA",
        "developer_url": "#",
    }
