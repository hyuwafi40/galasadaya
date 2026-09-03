SIDEBAR_MENUS = [
    {
        "category": "Home",
        "items": [
            {
                "title": "Dashboard",
                "url": "core:index",
                "icon": "fa-house",
                "roles": ["reguler", "administrator", "developer"],
            },
            {
                "title": "Profiles",
                "url": "#",
                "icon": "fa-users",
                "roles": ["administrator", "developer"],
            },
        ],
    },
    {
        "category": "Configuration",
        "items": [
            {
                "title": "Users",
                "url": "core:account",
                "icon": "fa-user-gear",
                "roles": ["developer"],
            },
            {
                "title": "Brand",
                "url": "core:brand",
                "icon": "fa-copyright",
                "roles": ["developer"],
            },
            {
                "title": "Advertisements",
                "url": "core:ads",
                "icon": "fa-ad",
                "roles": ["administrator", "developer"],
            },
        ],
    },
    {
        "category": "Asset",
        "items": [
            {
                "title": "Pages",
                "url": "core:pages",
                "icon": "fa-file",
                "roles": ["administrator", "developer"],
            },
            {
                "title": "Categories",
                "url": "core:categories",
                "icon": "fa-folder",
                "roles": ["administrator", "developer"],
            },
            {
                "title": "Tags",
                "url": "core:tags",
                "icon": "fa-tags",
                "roles": ["administrator", "developer"],
            },
            {
                "title": "Carousels",
                "url": "core:carousels",
                "icon": "fa-image",
                "roles": ["administrator", "developer"],
            },
        ],
    },
    {
        "category": "Blog",
        "items": [
            {
                "title": "Articles",
                "url": "core:articles",
                "icon": "fa-newspaper",
                "roles": ["reguler", "administrator", "developer"],
            },
            {
                "title": "Galleries",
                "url": "core:galleries",
                "icon": "fa-images",
                "roles": ["reguler", "administrator", "developer"],
            },
        ],
    },
]


def get_menus_for_role(role):
    filtered = []
    for category in SIDEBAR_MENUS:
        items = [item for item in category["items"] if role in item.get("roles", [])]
        if items:
            filtered.append({"category": category["category"], "items": items})
    return filtered
