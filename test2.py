from qa_automation2 import qa_connect
from qa_automation2.qa_infor import get_info_element
dev = qa_connect()
element = dev.Find_element(name="Camera")
print(dir(element))
# a= get_info_element(element, type_get="childCount")
# print(type(a),a)
# element.click()
