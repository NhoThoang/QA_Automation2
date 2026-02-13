import time, sys
from typing import Literal, List
from uiautomator2 import Direction
import uiautomator2 as u2
from qa_automation2.loginfor import setup_logger
from qa_automation2.adbcore import *

class qa_automation:
    def __init__(self, device:str=None, device_infor: dict=None, log_dir:str="logs"):
        self.device = device
        self.logger = setup_logger(name=device_infor.get("model"), log_dir=log_dir)
    def wait_activity(self, activity_name:str, timeout:int=10)-> bool:

        if not self.device.wait_activity(activity_name, timeout=timeout):
            self.logger.error(f"Activity {activity_name} did not load within {timeout} seconds.")
            return False
        return True
    def wait_for_element(self, 
                         name: str | List[str], 
                         type_: Literal[
                             "text", "text_contains", "text_matches", "text_startswith", 
                             "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                             "resource_id", "resource_id_matches", 
                             "xpath", 
                             "class_name", "class_name_matches"
                         ] = "text",
                         timeout: int = 10,
                         index: int = 0) -> object:
        start_time = time.time()
        while time.time() - start_time < timeout:
            element = self.Find_element(name, type_, index)
            if element:
                return element
            time.sleep(0.5)
        return False
    def abd_shell(self, command:str) -> str | bool:
        res = self.device.shell(command)
        if res.exit_code == 0:
            return res.output.strip()
        return False
    def start_app(self, package_name:str) -> bool:
        if self.device.app_start(package_name):
            return True
        return False
    def stop_app(self, package_name:str) -> bool:
        if self.device.app_stop(package_name):
            return True
        return False

    def press_key(self, key: str) -> bool:
        """
        Press a key like 'home', 'back', 'left', 'right', 'up', 'down', 'center',
        'menu', 'search', 'enter', 'delete', 'recent', 'volume_up', 'volume_down',
        'volume_mute', 'camera', 'power'.
        """
        try:
            self.device.press(key)
            return True
        except Exception as e:
            self.logger.error(f"Error pressing key {key}: {e}")
            return False

    def get_info_element(self, element,
                                type_get:Literal["bounds", "childCount", "className", "contentDescription",
                                 "packageName", "resourceName", "text","visibleBounds", "checkable", "checked",
                                 "clickable", "enabled", "focusable", "focused", "longClickable",
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
    def get_all_text_element(self, 
                             name: str | List[str] = "", 
                             type_: Literal[
                                 "text", "text_contains", "text_matches", "text_startswith", 
                                 "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                                 "resource_id", "resource_id_matches", 
                                 "xpath", 
                                 "class_name", "class_name_matches"
                             ] = "text",
                             index: int = 0,
                             action: Literal["text_all", "text_child", "talkback_all", "talkback_child"] = "text_all") -> List[str] | None:
        """
        Get all text/talkback from element or screen
        """
        if action == "text_all":
            nodes = self.device.xpath("//*[string-length(@text) > 0]").all()
            return [node.text for node in nodes]
            
        elif action == "talkback_all":
            nodes = self.device.xpath("//*[string-length(@content-desc) > 0]").all()
            return [node.attrib.get("content-desc") for node in nodes]

        element = self.Find_element(name=name, type_=type_, index=index)
        if element: 
            children = element.child()
            
            if action == "text_child":
                return [el.info.get("text") for el in children if el.info.get("text")]
            
            elif action == "talkback_child":
                return [el.info.get("contentDescription") for el in children if el.info.get("contentDescription")]
                
        return None
    def Find_element(self, 
                     name: str | List[str], 
                     type_: Literal[
                         "text", "text_contains", "text_matches", "text_startswith", 
                         "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                         "resource_id", "resource_id_matches", 
                         "xpath", 
                         "class_name", "class_name_matches"
                     ] = "text",
                     index: int = 0) -> object:
        if isinstance(name, list):
            for n in name:
                element = self.Find_element(name=n, type_=type_, index=index)
                if element:
                    return element
            return False

        selector_map = {
            "text": "text",
            "text_contains": "textContains",
            "text_matches": "textMatches",
            "text_startswith": "textStartsWith",
            "resource_id": "resourceId",
            "resource_id_matches": "resourceIdMatches",
            "talkback": "description",
            "talkback_contains": "descriptionContains",
            "talkback_matches": "descriptionMatches",
            "talkback_startswith": "descriptionStartsWith",
            "class_name": "className",
            "class_name_matches": "classNameMatches"
        }
        
        element = None
        if type_ == "xpath":
            element = self.device.xpath(name)
        elif type_ in selector_map:
            kwargs = {selector_map[type_]: name}
            element = self.device(**kwargs)
        else:
            # print(f'Type "{type_}" not supported. Supported keys: {", ".join(selector_map.keys())}, xpath')
            self.logger.error(f'Type "{type_}" not supported. Supported keys: {", ".join(selector_map.keys())}, xpath')
            return False

        if index is not None and index >= 0:
            element = element[index]

        if element.exists:
            return element
        return False


    def Touch(self, 
              name: str | List[str], 
              type_: Literal[
                  "text", "text_contains", "text_matches", "text_startswith", 
                  "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                  "resource_id", "resource_id_matches", 
                  "xpath", 
                  "class_name", "class_name_matches"
              ] = "text", 
              index: int = 0,
              long_: bool = False) -> bool:
        element = self.Find_element(name=name, type_=type_, index=index)
        if element:
            if long_:
                element.long_click()
            element.click()
            return True
        return False

    def scroll(self, type_:Literal["up", "down", "left", "right", "top", "bottom"]="up",
            scale:float=0.9, box:list[int, int, int, int]=None,duration:float=None, steps:float=None):
        if type_ =="top":
            self.device(scrollable=True).scroll.toBeginning()
        elif type_ =="bottom":
            self.device(scrollable=True).scroll.toEnd()
        elif type_=="up":
            self.device.swipe_ext(direction=Direction.UP, scale=scale, box=box, duration=duration, steps=steps)
        elif type_=="down":
            self.device.swipe_ext(direction=Direction.DOWN, scale=scale, box=box, duration=duration, steps=steps)
        elif type_ == "left":
            self.device.swipe_ext(direction=Direction.LEFT, scale=scale, box=box, duration=duration, steps=steps)
        elif type_ == "right":
            self.device.swipe_ext(direction=Direction.RIGHT, scale=scale, box=box, duration=duration, steps=steps)
        else:
            return False        
    def scroll_to_find_element(self, 
                               name: str | List[str], 
                               type_: Literal[
                                   "text", "text_contains", "text_matches", "text_startswith", 
                                   "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                                   "resource_id", "resource_id_matches", 
                                   "xpath", 
                                   "class_name", "class_name_matches"
                               ] = "text",
                               index: int = 0,
                               type_scroll: Literal["up", "down", "left", "right", "top", "bottom"] = "up",
                               max_scrolls=20, delay=0.5, scale: float = 0.9, box: list[int, int, int, int] = None,
                               duration: float = None, steps: float = None) -> bool:
        last_ui = ""
        for _ in range(max_scrolls):
            element = self.Find_element(name=name, type_=type_, index=index)
            if element:
                return element
            current_ui = self.device.dump_hierarchy(compressed=True)
            if current_ui == last_ui:
                break
            self.scroll(type_=type_scroll, scale=scale, box=box, duration=duration, steps=steps)
            time.sleep(delay)
            last_ui = current_ui
        return False


    def scroll_and_click_element(self, 
                                 name: str | List[str], 
                                 type_: Literal[
                                     "text", "text_contains", "text_matches", "text_startswith", 
                                     "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                                     "resource_id", "resource_id_matches", 
                                     "xpath", 
                                     "class_name", "class_name_matches"
                                 ] = "text",
                                 index: int = 0,
                                 type_scroll: Literal["up", "down", "left", "right", "top", "bottom"] = "up",
                                 max_scrolls=20, delay=0.5, scale: float = 0.9, box: list[int, int, int, int] = None,
                                 duration: float = None, steps: float = None) -> bool:
        element = self.scroll_to_find_element(name, type_, index, type_scroll, max_scrolls, delay, scale, box, duration, steps)
        if element:
            element.click()
            return True
        return False
    def scroll_up_down_find_element(self, 
                                    name: str | List[str], 
                                    type_: Literal[
                                        "text", "text_contains", "text_matches", "text_startswith", 
                                        "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                                        "resource_id", "resource_id_matches", 
                                        "xpath", 
                                        "class_name", "class_name_matches"
                                    ] = "text",
                                    index: int = 0,
                                    type_scroll: Literal["updown", "letfright"] = "updown",                           
                                    max_scrolls=20, delay=0.5, scale: float = 0.9, box: list[int, int, int, int] = None,
                                    duration: float = None, steps: float = None) -> bool:
        if type_scroll == "updown":
            element = self.scroll_to_find_element(name, type_, index, "up", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            element = self.scroll_to_find_element(name, type_, index, "down", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            return False
        elif type_scroll == "letfright":
            element = self.scroll_to_find_element(name, type_, index, "left", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            element = self.scroll_to_find_element(name, type_, index, "right", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            return False
        else:
            print(f"{type_scroll} wrong please input correct updown or letfright")
            return False

    def scroll_up_down_find_element_click(self, 
                                          name: str | List[str], 
                                          type_: Literal[
                                              "text", "text_contains", "text_matches", "text_startswith", 
                                              "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                                              "resource_id", "resource_id_matches", 
                                              "xpath", 
                                              "class_name", "class_name_matches"
                                          ] = "text",
                                          index: int = 0,
                                          type_scroll: Literal["updown", "letfright"] = "updown",                           
                                          max_scrolls=20, delay=0.5, scale: float = 0.9, box: list[int, int, int, int] = None,
                                          duration: float = None, steps: float = None) -> bool:
        element = self.scroll_up_down_find_element(name, type_, index, type_scroll, max_scrolls, delay, scale, box, duration, steps)
        if element:
            element.click()
            return True
        return False

    def send_text(self, 
                  text: str, 
                  name: str | List[str] = None, 
                  type_: Literal[
                      "text", "text_contains", "text_matches", "text_startswith", 
                      "talkback", "talkback_contains", "talkback_matches", "talkback_startswith", 
                      "resource_id", "resource_id_matches", 
                      "xpath", 
                      "class_name", "class_name_matches"
                  ] = "text",
                  index: int = 0,
                  clear: bool = False,
                  press_enter: bool = False,
                  click_before: bool = True) -> bool:
        """
        Send text to an element or the currently focused element.
        - If name is provided, it finds the element using Find_element.
        - If clear is True, it clears the text before sending the new text or send_keys.
        - If click_before is True, it clicks on the element before sending text.
        - If press_enter is True, it presses the Enter key after sending the text.
        """
        if name:
            element = self.Find_element(name=name, type_=type_, index=index)
            if element:
                if click_before:
                    element.click()
                if clear:
                    element.clear_text()
                element.set_text(text)
                if press_enter:
                    self.device.press("enter")
                return True
            else:
                self.logger.error(f"Element not found to send text: {name}")
                return False
        else:
            if clear:
                 self.device.clear_text()
            self.device.send_keys(text)
            if press_enter:
                self.device.press("enter")
            return True

    def manage_screen(self, action: Literal["on", "off", "check"] = "check") -> bool:
        """
        Manage screen state: check if on, turn on, or turn off.
        """
        if action == "check":
            return self.device.info.get('screenOn')
        elif action == "on":
             self.device.screen_on()
             return True
        elif action == "off":
             self.device.screen_off()
             return True
        return False
    
    def click_element_relative(self, 
                               anchor_text: str, 
                               target_type: Literal["radio", "checkbox", "button", "text", "edit", "switch"] = "radio", 
                               direction: Literal["left", "right", "up", "down", "sibling"] = "right",
                               timeout: int = 5) -> bool:
        """
        Click an element relative to an anchor text.
        This is useful for forms where labels are static but inputs have dynamic IDs.
        
        Usage:
        qa.click_element_relative("Gender", "radio", "right") -> Finds "Gender", clicks radio button to its right.
        qa.click_element_relative("Enable Notifications", "switch", "right") -> Finds text, clicks switch.
        """
        # Map common types to standard/common Android classes
        # If target_type is not in map, it is treated as a raw class name or resource-id part if needed, 
        # but for simplicity here we assume it's a class map or raw class name.
        class_map = {
            "radio": "android.widget.RadioButton",
            "checkbox": "android.widget.CheckBox",
            "switch": "android.widget.Switch",
            "button": "android.widget.Button",
            "text": "android.widget.TextView",
            "edit": "android.widget.EditText",
            "image": "android.widget.ImageView"
        }
        
        target_class = class_map.get(target_type)
        if not target_class:
            # If not in map, assume user passed a valid class name (e.g. android.view.View)
            target_class = target_type

        # Find anchor
        anchor = self.device(text=anchor_text)
        if not anchor.exists(timeout=timeout):
           self.logger.error(f"Anchor text '{anchor_text}' not found")
           return False

        # Find relative target
        target = None
        if direction == "left":
            target = anchor.left(className=target_class)
        elif direction == "right":
            target = anchor.right(className=target_class)
        elif direction == "up":
            target = anchor.up(className=target_class)
        elif direction == "down":
            target = anchor.down(className=target_class)
        elif direction == "sibling":
            # Sibling is tricky, uiautomator2 usually implies sibling by subsequent selection from parent 
            # or by just chaining if possible. 
            # Ideally: anchor.sibling(className=...) might not exist directly as 'sibling' method in basic wrapper, 
            # but we can use `right` or `left` or XPath if needed. 
            # However, uiautomator2 has .sibling() selector support in chaining:
            target = anchor.sibling(className=target_class)
        
        if target and target.exists:
            target.click()
            return True
        
        self.logger.error(f"Target '{target_type}' ({target_class}) not found {direction} of '{anchor_text}'")
        return False
    
    def click_child_element(self, 
                            parent_name: str, 
                            child_name: str, 
                            parent_type: Literal[
                                "text", "text_contains", "resource_id", "xpath", "class_name"
                            ] = "resource_id",
                            child_type: Literal["text", "resource_id", "class_name", "description"] = "text",
                            index: int = 0,
                            child_index: int = 0) -> bool:
        """
        Find a parent element and click a specific child inside it.
        Example: Find a list item (parent) by its ID/XPath and click the 'Delete' button (child) inside it.
        child_index uses 'instance' in uiautomator2 to select the Nth matching child.
        """
        # 1. Find the parent element object first using existing Find_element
        # Note: Find_element returns a UIObject but might be wrapped or pure. 
        # Assuming Find_element returns a uiautomator2 UIObject.
        parent = self.Find_element(name=parent_name, type_=parent_type, index=index)
        
        if not parent:
            self.logger.error(f"Parent element '{parent_name}' not found")
            return False

        # 2. Define child selector based on type
        # We need to construct arguments for the .child() method of uiautomator2
        child_kwargs = {}
        if child_type == "text":
            child_kwargs["text"] = child_name
        elif child_type == "resource_id":
            child_kwargs["resourceId"] = child_name
        elif child_type == "class_name":
            child_kwargs["className"] = child_name
        elif child_type == "description":
            child_kwargs["description"] = child_name
            
        if child_index > 0:
            child_kwargs["instance"] = child_index

        # 3. Find child inside parent and click
        try:
            # The parent object from uiautomator2 supports .child(**kwargs)
            child = parent.child(**child_kwargs)
            if child.exists:
                child.click()
                return True
            else:
                self.logger.error(f"Child '{child_name}' ({child_type}) index {child_index} not found inside parent")
                return False
        except Exception as e:
            self.logger.error(f"Error clicking child: {e}")
            return False
            
    def zoom_screen(self, 
                    action: Literal["in", "out"] = "out", 
                    percent: int = 100, 
                    steps: int = 50,
                    element_name: str | List[str] = None, 
                    element_type: str = "resource_id"
                    ) -> bool:
        """
        Perform zoom in/out (pinch) gesture on screen or specific element.
        action: "in" (shrink) or "out" (expand)
        """
        try:
            target = self.device
            if element_name:
                el = self.Find_element(element_name, element_type)
                if el:
                    target = el
                else: 
                     return False

            if action == "in":
                # pinch_in: 2 fingers move closer
                target.pinch_in(percent=percent, steps=steps)
            elif action == "out":
                 # pinch_out: 2 fingers move apart
                target.pinch_out(percent=percent, steps=steps)
            return True
        except Exception as e:
            self.logger.error(f"Error zooming {action}: {e}")
            return False
            
    # --- Advanced Gestures ---
    def drag_element(self, 
                     source_name: str, 
                     dest_name: str = None, 
                     dest_x: int = None, 
                     dest_y: int = None,
                     duration: float = 0.5,
                     type_: str = "text") -> bool:
        """
        Drag an element to another element or coordinates.
        """
        try:
            source = self.Find_element(source_name, type_)
            if not source:
                self.logger.error(f"Source element '{source_name}' not found for drag")
                return False
            
            if dest_name:
                dest = self.Find_element(dest_name, type_)
                if dest:
                    source.drag_to(dest, duration=duration)
                    return True
                else: 
                     self.logger.error(f"Destination element '{dest_name}' not found")
                     return False
            elif dest_x is not None and dest_y is not None:
                source.drag_to(dest_x, dest_y, duration=duration)
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error dragging: {e}")
            return False

    def double_click(self, name: str, type_: str = "text") -> bool:
        """ Double click an element """
        el = self.Find_element(name, type_)
        if el:
            el.click()
            el.click() # uiautomator2 doesn't have explicit double_click on object, so we simulate
            # or use gesture: self.device.double_click(x, y) if we get bounds
            return True
        return False

    # --- System Operations ---
    def capture_screenshot(self, filename: str) -> bool:
        """ Capture screenshot to file """
        try:
            self.device.screenshot(filename)
            self.logger.info(f"Screenshot saved to {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")
            return False

    def open_system_ui(self, target: Literal["notification", "quick_settings"]) -> bool:
        """ Open notification shade or quick settings """
        try:
            if target == "notification":
                self.device.open_notification()
            elif target == "quick_settings":
                self.device.open_quick_settings()
            return True
        except Exception as e:
             self.logger.error(f"Error opening {target}: {e}")
             return False

    def set_clipboard(self, text: str) -> bool:
        """ Set clipboard content """
        try:
            self.device.clipboard = text
            return True
        except Exception as e:
            self.logger.error(f"Error setting clipboard: {e}")
            return False

    def get_clipboard(self) -> str | bool:
        """ Get clipboard content """
        try:
            return self.device.clipboard
        except Exception as e:
            self.logger.error(f"Error getting clipboard: {e}")
            return False

    def rotate_screen(self, orientation: Literal["n", "l", "r", "u"] = "n") -> bool:
        """ 
        Rotate screen: n(natural), l(left), r(right), u(upside down) 
        """
        try:
            self.device.set_orientation(orientation)
            return True
        except Exception as e:
            self.logger.error(f"Error rotating screen: {e}")
            return False

    # --- Debug & Toast ---
    def get_hierarchy(self) -> str | bool:
        """ Dump UI hierarchy as XML string """
        try:
             return self.device.dump_hierarchy()
        except Exception as e:
             self.logger.error(f"Error dumping hierarchy: {e}")
             return False

    def get_toast(self, wait_timeout: float = 10.0) -> str | None:
        """ Get the latest toast message """
        try:
            # wait for toast and return its message
            # message = self.device.toast.get_message(wait_timeout, 5.0, "default") 
            # Note: uiautomator2 toast handling might vary by version
            return self.device.toast.get_message(wait_timeout, 5.0, "default")
        except Exception as e:
            self.logger.error(f"Error getting toast: {e}")
            return None

    # --- Watcher ---
    def register_watcher(self, name: str, condition_text: str, action_text: str = None, click_action: bool = True):
        """
        Register a watcher to auto-handle UI interruptions (like popups).
        - condition_text: Text to look for (e.g., "Allow")
        - action_text: Text to look for next (if separate) or same as condition
        - click_action: Click the found text?
        """
        try:
             if click_action:
                 if action_text:
                     self.device.watcher(name).when(condition_text).click(action_text)
                 else:
                     self.device.watcher(name).when(condition_text).click()
             else:
                 # Just register existence check or press key
                 self.device.watcher(name).when(condition_text).press("back")
             
             self.device.watcher.start()
             self.logger.info(f"Watcher {name} registered for '{condition_text}'")
        except Exception as e:
             self.logger.error(f"Error registering watcher: {e}")

    def remove_watcher(self, name: str):
        """ Remove a registered watcher """
        try:
            self.device.watcher.remove(name)
        except Exception:
            pass
    
    def remove_all_watchers(self):
        """ Remove all watchers """
        self.device.watcher.remove()
    

