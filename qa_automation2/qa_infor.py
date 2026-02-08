from typing import Literal
import warnings

def get_info_element(element,
    type_get:Literal["bounds", "childCount", "className", "contentDescription", "packageName", "resourceName", "text",
        "visibleBounds", "checkable", "checked", "clickable", "enabled", "focusable", "focused", "longClickable", 
        "scrollable", "selected"] = "text")-> str | int | bool | None:
    warnings.warn(
        "The function 'get_info_element' in 'qa_infor' is deprecated and will be removed in a future version. "
        "Please use 'qa_automation.get_info_element' in 'qautomationcore' instead.",
        DeprecationWarning,
        stacklevel=2
    )
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