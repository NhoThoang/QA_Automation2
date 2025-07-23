# QA Automation2

Dự án **QA Automation2** là một hệ thống tự động hóa kiểm thử cho ứng dụng di động, được phát triển dựa trên thư viện [u2](https://github.com/openatx/uiautomator2).

## Tính năng chính
- Tự động hóa kiểm thử ứng dụng Android thông qua giao diện điều khiển và script Python.
- Quản lý thiết bị, đăng nhập, kiểm tra thông tin và thực hiện các thao tác tự động.
- Lưu trữ log kiểm thử và hỗ trợ cấu hình qua file YAML.

## Cấu trúc dự án
- `qa_automation2/`: Chứa các module chính như quản lý thiết bị (`adbcore.py`), đăng nhập (`loginfor.py`), kiểm tra thông tin (`qa_infor.py`), và core tự động hóa (`qautomationcore.py`).
- `recbin/`: Chứa các script hỗ trợ, file cấu hình YAML và các module bổ sung.
- `logs/`: Thư mục lưu trữ log kiểm thử.
- `test2.py`: Script kiểm thử mẫu.

## Yêu cầu
- Python >= 3.8
- Thư viện [uiautomator2](https://github.com/openatx/uiautomator2)

## Cài đặt
```bash
pip install -r requirements.txt
```
Hoặc cài đặt trực tiếp uiautomator2:
```bash
pip install uiautomator2
```

## Sử dụng
Ví dụ khởi động kiểm thử:
```bash
python test2.py
```
Hoặc sử dụng các module trong `qa_automation2` để xây dựng kịch bản kiểm thử tùy chỉnh.

## Tài liệu tham khảo
- [uiautomator2 Documentation](https://github.com/openatx/uiautomator2)

## Liên hệ
Mọi thắc mắc hoặc đóng góp vui lòng liên hệ qua email hoặc tạo issue trên repository.
