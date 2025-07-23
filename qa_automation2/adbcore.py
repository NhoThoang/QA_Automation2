from adbutils import adb
# """['_ScreenrecordExtension__get_screenrecord_impl', '_ScreenshotExtesion__get_real_display_id', '_ScreenshotExtesion__screencap', 
# '__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__',
# '_abc_impl', '_client', '_features', '_get_with_command', '_install', '_prepare', '_properties', '_push_apk', '_record_client', 
# '_serial', '_shell_v1', '_shell_v2', '_transport_id', '_wm_size', 'adb_output', 'app_clear', 'app_current', 'app_info', 'app_start',
# 'app_stop', 'battery', 'brightness_mode', 'brightness_value', 'click', 'create_connection', 'download_apk', 'dump_hierarchy', 'forward',
# 'forward_list', 'forward_port', 'framebuffer', 'get_devpath', 'get_features', 'get_serialno', 'get_state', 'getprop', 'info', 'install', 
# 'install_remote', 'is_recording', 'is_screen_on', 'keyevent', 'list_packages', 'logcat', 'open_browser', 'open_shell', 'open_transport',
# 'package_info', 'prop', 'push', 'reboot', 'remove', 'reverse', 'reverse_list', 'rmtree', 'root', 'rotation', 'screenshot', 'send_keys',
# 'serial', 'shell', 'shell2', 'start_recording', 'stop_recording', 'swipe', 'switch_airplane', 'switch_screen', 'switch_wifi', 'sync', 
# 'tcpip', 'uninstall', 'volume_down', 'volume_mute', 'volume_up', 'window_size', 'wlan_ip']"""
# devices = adb.device_list()
# device = devices[0]
# print(dir(device))
# device = adb.connect("192.168.1.100:5555")
# device = adb.device(serial="emulator-5554")
class adbcore:
    def __init__(self):
        pass
    def devices_list(self):
        devices = adb.device_list()
        return [device.serial for device in devices]
