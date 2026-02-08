from typing import Literal

def get_info_element(element,
    type_get:Literal["bounds", "childCount", "className", "contentDescription", "packageName", "resourceName", "text",
        "visibleBounds", "checkable", "checked", "clickable", "enabled", "focusable", "focused", "longClickable", 
        "scrollable", "selected"] = "text")-> str | int | bool | None:
    """"
    {
        'bounds': {'bottom': 1348, 'left': 39, 'right': 285, 'top': 1005},
        'childCount': 0,
        'className': 'android.widget.TextView',
        'contentDescription': 'Camera',
        'packageName': 'com.sec.android.app.launcher',
        'resourceName': 'com.sec.android.app.launcher:id/apps_icon',
        'text': 'Camera',
        'visibleBounds': {'bottom': 1348, 'left': 39, 'right': 285, 'top': 1005},
        'checkable': False,
        'checked': False,
        'clickable': True,
        'enabled': True,
        'focusable': True,
        'focused': False,
        'longClickable': True,
        'scrollable': False,
        'selected': False
    }
    """
    if element:
        return element.info.get(type_get)
    return None
# def get_all_text_element(element):
#     """
#     Get all text from element
#     """
#     if element:
#         return element.info.get("text")
#     return None