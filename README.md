# QA Automation 2 🚀

Dự án **QA Automation2** là một hệ thống tự động hóa kiểm thử cho ứng dụng di động mạnh mẽ, được phát triển dựa trên thư viện [uiautomator2](https://github.com/openatx/uiautomator2). Phiên bản này hỗ trợ tìm kiếm phần tử linh hoạt với nhiều chiến lược (Startswith, Contains, Regex...) và quản lý Log chuyên nghiệp.

## 📦 Yêu cầu & Cài đặt

*   **Python:** >= 3.8
*   **Android SDK Platform-Tools** (adb)

Cài đặt thư viện:

```bash
pip install qa_automation2
```


## 🚀 Tính năng nổi bật

*   **Tìm kiếm phần tử nâng cao:** Hỗ trợ Regex ($), Contains (*), StartsWith (^) cho cả Text, Description và Resource ID.
*   **Log Rotation:** Hệ thống log tự động xoay vòng file (Max 5MB/file, giữ lại 3 file backup).
*   **Auto Scroll:** Tự động cuộn thông minh để tìm kiếm phần tử theo nhiều hướng (Up, Down, Left, Right).
*   **Quản lý thiết bị:** Tự động kết nối và lấy thông tin thiết bị.

## 📖 Hướng dẫn sử dụng

### 1. Khởi tạo kết nối

```python
from qa_automation2 import qa_connect

# Kết nối thiết bị đầu tiên tìm thấy và lưu log vào thư mục "logs"
automation = qa_connect(log_dir="logs")

# Hoặc kết nối thiết bị cụ thể qua Serial ID
# automation = qa_connect(device_id="RFcn0w...", log_dir="custom_logs")
```

### 2. Chiến lược Tìm kiếm (Selector Strategies)

Hàm `Find_element` và các hàm tương tác hỗ trợ các loại `type_` sau để định vị phần tử chính xác hơn:

| Loại (`type_`) | Ý nghĩa | Ví dụ Code |
| :--- | :--- | :--- |
| `text` | Chính xác tuyệt đối | `text="Login"` |
| `text_contains` | Chứa chuỗi con | `textContains="Log"` |
| `text_startswith` | Bắt đầu bằng chuỗi | `textStartsWith="Welcome"` |
| `text_matches` | Biểu thức chính quy (Regex) | `textMatches="^Log.*"` |
| `resource_id` | ID chính xác | `resourceId="com.app:id/btn"` |
| `resource_id_matches` | ID theo Regex | `resourceIdMatches=".*btn_login$"` |
| `talkback` | Content Description chính xác | `description="Home"` |
| `talkback_contains` | Description chứa chuỗi | `descriptionContains="ome"` |
| `talkback_startswith`| Description bắt đầu bằng | `descriptionStartsWith="Hom"` |
| `talkback_matches` | Description theo Regex | `descriptionMatches="^Hom.*"` |

### 3. Ví dụ Code

**Click vào một phần tử có chứa chữ "Settings":**
```python
automation.Touch(name="Settings", type_="text_contains")
```

**Cuộn xuống tìm phần tử bắt đầu bằng "Chapter 1":**
```python
automation.scroll_to_find_element(
    name="Chapter 1", 
    type_="text_startswith", 
    type_scroll="down",
    max_scrolls=10
)
```

**Lấy text của tất cả phần tử con khớp với Regex:**
```python
texts = automation.get_all_text_element(name="^[0-9]+$", type_="text_matches")
```

## ⚠️ Deprecation Warning

Các hàm sau đây đã lỗi thời và sẽ bị xóa trong phiên bản tới:

*   `qa_infor.get_info_element`: Đã chuyển sang `qautomationcore.qa_automation.get_info_element`.
    *   *Hành động:* Vui lòng cập nhật code để sử dụng hàm mới và tránh cảnh báo `DeprecationWarning`.

## 📂 Cấu trúc dự án

*   `qa_automation2/`:
    *   `qautomationcore.py`: Core xử lý chính (Find, Touch, Scroll...).
    *   `loginfor.py`: Quản lý Logging (RotatingFileHandler).
    *   `adbcore.py`: Tương tác ADB.
    *   `qa_infor.py`: (Deprecated) Các tiện ích cũ.
*   `logs/`: Thư mục lưu trữ log kiểm thử.

## 🤝 Liên hệ
Mọi thắc mắc hoặc đóng góp vui lòng liên hệ qua email hoặc tạo issue trên repository.
