from qa_automation2 import qa_connect
# from qa_automation2.qa_infor import get_info_element
dev = qa_connect()
dev.device.unlock()
# a= dev.get_all_text_element(name='com.sec.android.app.shealth:id/title', type_='resource_id')
element = dev.Find_element(name="Camera")
b= dev.get_info_element(element=element)
# element = dev.Find_element(name="Camera")
# if element:
#     print(element.sibling().count)  # Access the count of sibling elements
# # print(dir(dev.device.unlock()))
# element = dev.Find_element(name="Camera")
# # print(dir(element))
# print(element.info)  # Access the parent node

# devive =dev.device
# element = devive(text="Camera")
# print(dir(element))
# if not element:
#     print("Element not found")
# print(element)  # Access the parent node
# print(element.info)  # Access the parent node
# print(dir(element))
# print(dir(element.info))  # Get the count of sibling elements
# print(dir(element.parent))
# print(element.parent.info)
# print(element.parent.info)
# print(dir(element.parent))
# print(a)
# print(dir(element.sibiling()))
# a= get_info_element(element, type_get="childCount")
# print(type(a),a)
# element.click()
# ['_UiObject__view_beside', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#   '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#   '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
#   '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bounds', 
# 'center', 'child', 'child_by_description', 'child_by_instance', 'child_by_text', 'child_selector',
# 'clear_text', 'click', 'click_exists', 'click_gone', 'count', 'down', 'drag_to', 'exists', 'fling', 
# 'from_parent', 'gesture', 'get_text', 'info', 'jsonrpc', 'left', 'long_click', 'must_wait', 'parent', 
# 'pinch_in', 'pinch_out', 'right', 'screenshot', 'scroll', 'selector', 'send_keys', 'session', 'set_text', 'sibling', 
# 'swipe', 'up', 'wait', 'wait_gone', 'wait_timeout']


# | Thuộc tính / Phương thức | Mô tả                                        |
# | ------------------------ | -------------------------------------------- |
# | `parent`                 | Trả về đối tượng cha của node                |
# | `child()`                | Trả về con đầu tiên                          |
# | `sibling()`              | Trả về node cùng cấp                         |
# | `from_parent()`          | Truy cập node từ cha (ngược lại với `child`) |
