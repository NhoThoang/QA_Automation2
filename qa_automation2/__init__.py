from qa_automation2.qautomationcore import *
import sys
class qa_connect(qa_automation):
    def __init__(self,device_id=None, log_dir:str="logs"):
        if device_id:
            self.device =u2.connect(device_id)
        else:
            try:
                device_id = adbcore().devices_list()[0]
                self.device = u2.connect(device_id)
                self.device.wait_timeout
            except Exception as e:
                print(f"Not found device {e}")
                sys.exit()
        self.device_information = self.device.device_info
        super().__init__(device=self.device, device_infor=self.device_information, log_dir=log_dir)
        self.logger.info(msg=f"Connected model {self.device_information}")
