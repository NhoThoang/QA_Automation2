from qa_automation2 import qa_connect
import time

# --- CẤU HÌNH TEST THÀNH CÔNG (Dựa trên log màn hình Home của bạn) ---
TARGET_TEXT = "Play Store"        # Text chính xác có trên màn hình
TARGET_TEXT_CONTAINS = "Store"    # Text chứa
TARGET_REGEX = "^[P|C].*"         # Regex: Bắt đầu bằng P (Play Store, Phone) hoặc C (Camera)
TARGET_CLASS = "android.widget.TextView" 
# Launcher Samsung thường là com.sec.android.app.launcher hoặc com.android.launcher3 (Pixel)
# Mình sẽ dùng wait_activity cho text tìm thấy để đảm bảo đúng app đang mở (Launcher)
LOG_DIR = "logs/test_success"

def main():
    print(">>> KHOI TAO KET NOI (TEST SUCCESS CASE)...")
    # 1. Khởi tạo
    automation = qa_connect(log_dir=LOG_DIR)
    print(f"Device Info: {automation.device_information.get('model')}")

    # 2. Test ADB Shell
    print(">>> [TEST] abd_shell")
    res = automation.abd_shell("input keyevent 3") # Về Home
    print(f"ADB Home Result: {res}")
    time.sleep(2) # Chờ về Home xong
    
    # 3. Test Wait Activity (Mình sẽ check gói Launcher hiện tại)
    current_app = automation.device.app_current()
    current_pkg = current_app.get('package')
    print(f"\n>>> [TEST] wait_activity: Current App is {current_pkg}")
    
    if current_pkg:
        is_loaded = automation.wait_activity(current_pkg, timeout=3)
        print(f"Result (Should be True): {is_loaded}")
    else:
        print("Result: Could not detect current package.")

    # 4. Test Find_element & Selector Types
    print("\n>>> [TEST] Find_element with Advanced Selectors")
    
    # Text Exact ("Play Store")
    el = automation.Find_element(TARGET_TEXT, type_="text")
    print(f" - Text Exact '{TARGET_TEXT}': {'FOUND' if el else 'NOT FOUND'}")

    # Text Contains ("Store")
    el_cont = automation.Find_element(TARGET_TEXT_CONTAINS, type_="text_contains")
    print(f" - Text Contains '{TARGET_TEXT_CONTAINS}': {'FOUND' if el_cont else 'NOT FOUND'}")
    
    # Regex ("^[P|C].*")
    el_reg = automation.Find_element(TARGET_REGEX, type_="text_matches")
    print(f" - Text Matches Regex '{TARGET_REGEX}': {'FOUND' if el_reg else 'NOT FOUND'}")
    # Nếu tìm thấy, in ra text thực tế để kiểm chứng
    if el_reg:
        print(f"   -> Found element text: {el_reg.info.get('text')}")

    # Class Name
    el_cls = automation.Find_element(TARGET_CLASS, type_="class_name")
    print(f" - Class Name '{TARGET_CLASS}': {'FOUND' if el_cls else 'NOT FOUND'}")

    # 5. Test get_info_element
    print("\n>>> [TEST] get_info_element")
    if el:
        info_text = automation.get_info_element(el, type_get="text")
        info_bounds = automation.get_info_element(el, type_get="bounds")
        print(f" - Info Text of Found Element: {info_text}")
        print(f" - Info Bounds: {info_bounds}")

    # 6. Test Get All Text (Action Text All)
    print("\n>>> [TEST] get_all_text_element (Action: text_all)")
    all_texts = automation.get_all_text_element(action="text_all")
    print(f" - Found {len(all_texts)} texts on screen.")
    if TARGET_TEXT in all_texts:
        print(f" - Success: '{TARGET_TEXT}' is present in the list.")
    else:
        print(f" - Warning: '{TARGET_TEXT}' not found in full text list??")

    # 7. Test Scroll
    # Vì màn hình Home đôi khi không scroll được (nếu ít icon), ta test nhẹ
    print("\n>>> [TEST] Scroll Functions (Test lightly)")
    automation.scroll(type_="right", duration=0.1) # Vuốt màn hình sang phải
    time.sleep(1)
    automation.scroll(type_="left", duration=0.1)  # Vuốt lại sang trái
    print(" - Scroll Left/Right executed.")

    print("\n>>> TEST COMPLETED SUCCESS.")

if __name__ == "__main__":
    main()
