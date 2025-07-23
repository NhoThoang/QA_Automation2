import uiautomator2 as u2
d = u2.connect() 
print(d.info)
d.swipe_ext("up", scale=0.8, box=(0, 0, 1080, 1920))  # Adjust the box size as needed
d.swipe_ext("down", scale=0.8, box=(0, 0, 1080, 1920))  # Adjust the box size as needed
d.clear_text()  # Clear the text input field
d.app_start("com.android.settings")  
d(text="Search").click()  
d(text="Apps").click()  
d(text="com.github.uiautomator").click()  
d(text="Uninstall").click()  
d(text="OK").click()
d.wait_activity("com.android.settings.Settings", timeout=10)  # Wait for the activity to load
text = d.xpath('//android.widget.TextView[@text="Uninstall"]')
if text.exists:
    print("Uninstall button found")
else:
    print("Uninstall button not found")
text = d.xpath('//android.widget.TextView[@text="Uninstall"]').get_text() 
# text = d.xpath('//android.widget.TextView[@text="Uninstall"]').get("resou rce-id") 
# fans_count = d.xpath('//*[@resource-id="tv.danmaku.bili:id/fans_count"]').text
# print(f"Fan count: {fans_count}")
d.xpath('//android.widget.TextView[@text="Uninstall"]').click()
print(d.info)
import adbutils # Requires version >=2.9.1
import uiautomator2 as u2
dev = adbutils.device(transport_id=6)
d = u2.connect(dev)


# Basic Syntax:

# / - Select from the root node
# // - Select from any position starting from the current node
# . - Select the current node
# .. - Select the parent of the current node
# @ - Select attributes
# [] - Predicate expression, used for filtering conditions
# You can quickly generate XPath using UIAutoDev.

d.xpath('//*[@text="私人FM"]').click() # Click element with text "私人FM"

# Syntactic sugar
d.xpath('@personal-fm') # Equivalent to d.xpath('//*[@resource-id="personal-fm"]')

sl = d.xpath("@com.example:id/home_searchedit") # sl is an XPathSelector object
sl.click()
sl.click(timeout=10) # Specify timeout, throws XPathElementNotFoundError if not found
sl.click_exists() # Click if exists, returns whether click was successful
sl.click_exists(timeout=10) # Wait up to 10s

# Wait for the corresponding element to appear, returns XMLElement
# Default wait time is 10s
el = sl.wait()
el = sl.wait(timeout=15) # Wait 15s, returns None if not found

# Wait for element to disappear
sl.wait_gone()
sl.wait_gone(timeout=15)

# Similar to wait, but throws XPathElementNotFoundError if not found
el = sl.get()
el = sl.get(timeout=15)

sl.get_text() # Get component text
sl.set_text("") # Clear input field
sl.set_text("hello world") # Input "hello world" into input field

# Element Wait Timeout
d.implicitly_wait(10.0) # Can also be modified via d.settings['wait_timeout'] = 10.0
print("wait timeout", d.implicitly_wait()) # get default implicit wait

# Throws UiObjectNotFoundError if "Settings" does not appear in 10s
d(text="Settings").click()
d.clear_text() # Clear text input field
d.long_click(100, 100) # Long press at coordinates (100, 100)
d.swipe(100, 100, 200, 200) # Swipe from (
d.drag(100, 100, 200, 200) # Drag from (100, 100) to (200, 200)
d.press("home") # Press home button
print(d.window_size())
print(d.app_current())

d.wait_activity(".ApiDemos", timeout=10) # default timeout 10.0 seconds
# Output: true or false

print(d.serial)
# output example: 74aAEDR428Z9

print(d.wlan_ip)
# output example: 10.0.0.1 or None

# Set clipboard
d.clipboard = 'hello-world'
# or
d.set_clipboard('hello-world', 'label')

# Get clipboard
# Depends on input method (com.github.uiautomator/.AdbKeyboard)
d.set_input_ime("com.github.uiautomator/.AdbKeyboard") # Set input method to AdbKeyboard
print(d.clipboard)

d.screen_on() # turn on the screen
d.screen_off() # turn off the screen

d.info.get('screenOn') # check if the screen is on
# Output: True or False
d.press("home") # press the home key, with key name
d.press("back") # press the back key, with key name
d.press(0x07, 0x02) # press keycode 0x07('0') with META ALT(0x02)
d.press("enter") # press enter key
# home
# back
# left
# right
# up
# down
# center
# menu
# search
# enter
# delete ( or del)
# recent (recent apps)
# volume_up
# volume_down
# volume_mute
# camera
# power

d.unlock()
# This is equivalent to
# 1. press("power")
# 2. swipe from left-bottom to right-top
d.click(x, y)
d.double_click(x, y)
d.double_click(x, y, 0.1) # default duration between two clicks is 0.1s
d.long_click(x, y)
d.long_click(x, y, 0.5) # long click 0.5s (default)

d.swipe(sx, sy, ex, ey)
d.swipe(sx, sy, ex, ey, 0.5) # swipe for 0.5s (default)


d.swipe_ext(direction="right") # Swipe right, 4 options: "left", "right", "up", "down"
d.swipe_ext("right", scale=0.9) # Default 0.9, swipe distance is 90% of screen width
d.swipe_ext("right", box=(0, 0, 100, 100)) # Swipe within the area (0,0) -> (100, 100)

# In practice, starting swipe from the midpoint for up/down swipes has a higher success rate
d.swipe_ext("up", scale=0.8)

# Can also use Direction as a parameter
from uiautomator2 import Direction
d.
d.swipe_ext(direction="down") # Scroll down page, equivalent to d.swipe_ext("up"), but easier to understand
d.swipe_ext(Direction.BACKWARD) # Scroll up page
d.swipe_ext(Direction.HORIZ_FORWARD) # Scroll page horizontally right
d.swipe_ext(Direction.HORIZ_BACKWARD) # Scroll page horizontally left
d.get_text() # Get text from the current focused element
activity = d.current_app() # Get current app package name
print(activity) # Output: com.example.app
curent_screen = d.screenshot() # Take a screenshot, returns PIL Image object
curent_screen.save("screenshot.png") # Save screenshot to file
curent_activity = d.current_app() # Get current app package name
print(curent_activity) # Output: com.example.app
# scroll up and down
d.scroll(steps=10) # Scroll down 10 steps
d.scroll(steps=-10) # Scroll up 10 steps