# QA Automation Core Documentation

This document provides a comprehensive guide to using the `qa_automation` class within `qautomationcore.py`. This class is a wrapper around `uiautomator2` designed to simplify Android UI automation tasks.

## Initialization

```python
from qa_automation2.qautomationcore import qa_automation

# Initialize with a connected device
# device: uiautomator2 device object
# device_infor: dictionary containing device information (e.g., model)
# log_dir: directory to save logs
qa = qa_automation(device=d, device_infor={"model": "Pixel_4"}, log_dir="logs")
```

## Core Functions

### 1. Element Interaction

#### `Find_element`
Finds a UI element based on various criteria.

*   **Parameters:**
    *   `name`: The identifier string (text, resource-id, xpath, etc.) or a list of strings.
    *   `type_`: The type of identifier. Options: `text`, `text_contains`, `resource_id`, `xpath`, `class_name`, `talkback`, etc.
    *   `index`: Index of the element if multiple match (default 0).
*   **Returns:** The UI object if found, otherwise `False`.

#### `wait_for_element`
Waits for an element to appear within a timeout period.

*   **Parameters:** Same as `Find_element`, plus `timeout` (seconds).
*   **Returns:** The UI object if found, otherwise `False`.

#### `Touch`
Finds an element and performs a click (or long click).

*   **Parameters:** Same as `Find_element`, plus `long_` (bool) for long press.
*   **Returns:** `True` if successful.

#### `send_text`
Inputs text into an element or the currently focused field.

*   **Parameters:**
    *   `text`: The string to input.
    *   `name`, `type_`, `index`: To find the target element (optional).
    *   `clear`: Clears existing text before inputting.
    *   `press_enter`: Presses the Enter key after inputting.
    *   `click_before`: Clicks the element before inputting (default `True`).

#### `click_element_relative`
Clicks an element located relative to an anchor text (e.g., click a specific Radio Button next to a label).

*   **Parameters:**
    *   `anchor_text`: The text to use as a reference point.
    *   `target_type`: The type of element to click (`radio`, `checkbox`, `switch`, `button`, `edit`).
    *   `direction`: Direction to look for the target (`left`, `right`, `up`, `down`, `sibling`).
*   **Example:** `qa.click_element_relative("Gender", "radio", "right")`

#### `click_child_element`
Clicks a specific child element within a parent container.

*   **Parameters:**
    *   `parent_name`, `parent_type`: Identifiers for the parent container.
    *   `child_name`, `child_type`: Identifiers for the child element inside the parent.
    *   `child_index`: Index of the child if multiple match (default 0).

### 2. Scroll & Search

#### `scroll`
Performs a simple scroll gesture.

*   **Parameters:**
    *   `type_`: Direction (`up`, `down`, `left`, `right`, `top`, `bottom`).
    *   `scale`, `box`, `duration`, `steps`: Fine-tuning scroll behavior.

#### `scroll_to_find_element`
Scrolls in a specified direction until the element is found.

*   **Parameters:** Element identifiers plus `type_scroll`, `max_scrolls`.

#### `scroll_up_down_find_element` / `scroll_up_down_find_element_click`
Scrolls one way (e.g., UP) then the other (e.g., DOWN) to find an element (and optionally click it).

### 3. Device Control

#### `press_key`
Simulates a physical key press.

*   **Keys:** `home`, `back`, `recent`, `enter`, `delete`, `volume_up`, `power`, etc.
*   **Example:** `qa.press_key("home")`

#### `manage_screen`
Controls the device screen state.

*   **Actions:** `check` (returns status), `on` (turn screen on), `off` (turn screen off).

#### `zoom_screen`
Performs a pinch-to-zoom gesture.

*   **Parameters:**
    *   `action`: `in` (zoom in/shrink), `out` (zoom out/expand).
    *   `percent`: Size of the pinch gesture.
    *   `element_name`: Optional, to perform zoom on a specific element.

### 4. App & System

#### `start_app` / `stop_app`
Starts or stops an application by package name.

#### `wait_activity`
Waits for a specific app activity (screen) to load.

#### `abd_shell`
Executes an ADB shell command on the device.

### 5. Information Retrieval

#### `get_all_text_element`
Retrieves text or content descriptions from all matching elements or children of an element.

#### `get_info_element`
Extracts specific properties (bounds, text, checked, enabled, etc.) from an element object.

### 6. Advanced Gestures & Interactions

#### `drag_element`
Drags an element to another element or specific coordinates.
*   **Parameters:** `source_name`, `dest_name` (or `dest_x`, `dest_y`), `duration`.

#### `double_click`
Double clicks on an element.
*   **Parameters:** `name`, `type_`.

### 7. System Operations

#### `capture_screenshot`
Captures a screenshot and saves it to a file.
*   **Parameters:** `filename` (path to save).

#### `open_system_ui`
Opens system panels.
*   **Parameters:** `target` (`notification`, `quick_settings`).

#### `set_clipboard` / `get_clipboard`
Sets or retrieves text from the device clipboard.

#### `rotate_screen`
Forces screen orientation.
*   **Parameters:** `orientation` (`n`=natural, `l`=left, `r`=right, `u`=upside down).

### 8. Debug & Watchers

#### `get_hierarchy`
Returns the current UI hierarchy as an XML string. Useful for debugging layout.

#### `get_toast`
Retrieves the message from a toast notification (transient popup).
*   **Parameters:** `wait_timeout`.

#### `register_watcher`
Registers a watcher to automatically handle popups or specific text.
*   **Parameters:** `name`, `condition_text`, `action_text` (what to click), `click_action` (bool).
*   **Example:** `qa.register_watcher("ANR", "Application not responding", "OK")`

#### `remove_watcher` / `remove_all_watchers`
Removes specific or all registered watchers.
