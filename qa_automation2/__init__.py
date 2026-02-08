from .qautomationcore import *
import sys
class qa_connect(qa_automation, adbcore):
    def __init__(self,device_id=None, log_dir:str="logs"):
        if device_id:
            self.device =u2.connect(device_id)
        else:
            try:
                device_id = self.devices_list()[0]
                self.device = u2.connect(device_id)
                self.device.wait_timeout
            except:
                print("No device connected, please plug the cable into the phone")
                sys.exit()
        self.device_information = self.device.device_info
        super().__init__(device=self.device, device_infor=self.device_information, log_dir=log_dir)
        self.logger.info(msg=f"Connected model {self.device_information}")
