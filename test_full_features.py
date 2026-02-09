from qa_automation2 import qa_connect
import time

# --- CẤU HÌNH TEST (Sửa lại cho khớp với màn hình hiện tại của bạn) ---
TARGET_TEXT = "Settings"        # Một text đang hiển thị trên màn hình
TARGET_TEXT_CONTAINS = "Sett"   # Một đoạn text con
TARGET_CLASS = "android.widget.TextView" # Class phổ biến
TARGET_PACKAGE = "com.android.settings" # Package app settings (hoặc app bạn đang mở)
LOG_DIR = "logs/test_full"

def main():
    print(">>> KHOI TAO KET NOI...")
    # 1. Khởi tạo
    automation = qa_connect(log_dir=LOG_DIR)
    print(f"Device Info: {automation.device_information}\n")

    # 2. Test ADB Shell
    print(">>> [TEST] abd_shell")
    res = automation.abd_shell("input keyevent 3") # Thử bấm Home
    print(f"ADB Command Result (Go Home): {res}")
    time.sleep(1)
    
    # 3. Test Wait Activity
    print(f"\n>>> [TEST] wait_activity: {TARGET_PACKAGE}")
    # Lưu ý: Hàm này đợi activity load
    is_loaded = automation.wait_activity(TARGET_PACKAGE, timeout=3)
    print(f"Result: {is_loaded}")

    # 4. Test Find_element & Selector Types
    print("\n>>> [TEST] Find_element with Advanced Selectors")
    
    # Text Exact
    el = automation.Find_element(TARGET_TEXT, type_="text")
    print(f" - Text Exact '{TARGET_TEXT}': {'FOUND' if el else 'NOT FOUND'}")

    # Text Contains
    el = automation.Find_element(TARGET_TEXT_CONTAINS, type_="text_contains")
    print(f" - Text Contains '{TARGET_TEXT_CONTAINS}': {'FOUND' if el else 'NOT FOUND'}")
    
    # Regex
    el = automation.Find_element("^[S|C].*", type_="text_matches") # Bắt đầu bằng S hoặc C
    print(f" - Text Matches Regex '^[S|C].*': {'FOUND' if el else 'NOT FOUND'}")

    # Class Name
    el = automation.Find_element(TARGET_CLASS, type_="class_name")
    print(f" - Class Name '{TARGET_CLASS}': {'FOUND' if el else 'NOT FOUND'}")

    # 5. Test get_info_element
    print("\n>>> [TEST] get_info_element")
    if el:
        info_text = automation.get_info_element(el, type_get="text")
        info_bounds = automation.get_info_element(el, type_get="bounds")
        print(f" - Info Text: {info_text}")
        print(f" - Info Bounds: {info_bounds}")

    # 6. Test Touch
    print("\n>>> [TEST] Touch")
    # Touch vào cái tìm thấy (Cẩn thận kịch bản click lung tung)
    # print(f"Touch '{TARGET_TEXT}': {automation.Touch(TARGET_TEXT, type_='text')}") 
    print(" (Skipped Touch to avoid unintended clicks - Uncomment in code to test)")

    # 7. Test get_all_text_element (New Feature)
    print("\n>>> [TEST] get_all_text_element")
    
    all_texts = automation.get_all_text_element(action="text_all")
    print(f" - found {len(all_texts) if all_texts else 0} texts on screen.")
    
    all_desc = automation.get_all_text_element(action="talkback_all")
    print(f" - found {len(all_desc) if all_desc else 0} content-descs on screen.")

    # Test child text
    child_texts = automation.get_all_text_element(name="android.widget.FrameLayout", type_="class_name", action="text_child")
    print(f" - Child texts of FrameLayout: {child_texts}")

    # 8. Test Scroll Functions
    print("\n>>> [TEST] Scroll Functions")
    # Scroll basic
    print(" - Scrolling Down...")
    automation.scroll(type_="down", duration=0.1)
    time.sleep(1)
    print(" - Scrolling Up...")
    automation.scroll(type_="up", duration=0.1)

    # Scroll to find
    print(f" - Scroll to find '{TARGET_TEXT}'...")
    found_el = automation.scroll_to_find_element(TARGET_TEXT, max_scrolls=2)
    print(f"Result: {'FOUND' if found_el else 'NOT FOUND'}")
    
    # Scroll Up Down Find
    print(f" - Scroll Up/Down to find '{TARGET_TEXT}'...")
    found_el_ud = automation.scroll_up_down_find_element(TARGET_TEXT, max_scrolls=2)
    print(f"Result: {'FOUND' if found_el_ud else 'NOT FOUND'}")

    print("\n>>> TEST COMPLETED.")

if __name__ == "__main__":
    main()
