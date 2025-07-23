import tkinter as tk
import threading
import win32gui
import win32con
import win32api

class PhoneModelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Theo dõi điện thoại")
        self.label = tk.Label(root, text="Model điện thoại: ", font=("Arial", 16), fg="blue")
        self.label.pack(padx=10, pady=20)

        # Chạy thread lắng nghe sự kiện
        threading.Thread(target=self.listen_device_events, daemon=True).start()

    def update_model(self):
        print("📱 Đang cập nhật model điện thoại...")

    def listen_device_events(self):
        # Tạo lớp cửa sổ để nhận thông điệp hệ thống
        wc = win32gui.WNDCLASS()
        wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "HiddenWindowListener"
        wc.lpfnWndProc = self.win_proc
        win32gui.RegisterClass(wc)

        hwnd = win32gui.CreateWindow(
            wc.lpszClassName, None, 0,
            0, 0, 0, 0,
            0, 0, wc.hInstance, None
        )

        # Bắt đầu lắng nghe sự kiện hệ thống
        win32gui.PumpMessages()

    def win_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DEVICECHANGE:
            if wparam == win32con.DBT_DEVICEARRIVAL:
                print("🔌 Điện thoại được cắm vào.")
                self.root.after(1500, self.update_model)
            elif wparam == win32con.DBT_DEVICEREMOVECOMPLETE:
                print("❌ Điện thoại bị rút ra.")
        return 1  # hoặc return True

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneModelApp(root)
    root.mainloop()
