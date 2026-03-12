from qa_automation2 import qa_connect
import time

def test_new_features():
    print(">>> KHOI TAO KET NOI TEST NEW FEATURES...")
    # 1. Khởi tạo
    automation = qa_connect(log_dir="logs/test_new_features")
    print(f"Device connected: {automation.device_information.get('model')}")

    # ---------------------------------------------------------
    # TEST 1: Tinh nang manage_webview_support (ADB commands)
    # ---------------------------------------------------------
    print("\n>>> [TEST 1] manage_webview_support (Bật/Tắt Debug Layout)")
    
    print(" - Dang BAT che do ho tro (Ban se thay khung do/xanh tren dien thoai)...")
    automation.manage_webview_support(action="on")
    time.sleep(3) # Cho ban quan sat man hinh dien thoai
    
    print(" - Dang TAT che do ho tro (Man hinh se tro lai binh thuong)...")
    automation.manage_webview_support(action="off")
    time.sleep(2)

    # ---------------------------------------------------------
    # TEST 2: Tinh nang scroll trong BOUNDS (Box)
    # ---------------------------------------------------------
    print("\n>>> [TEST 2] Scroll trong Bounds (Box)")
    
    # Huong dan: De test tinh nang nay, ban nen mo mot app co danh sach cuon (nhu Settings/Cài dặt)
    # Hoac minh se tu mo Settings
    print(" - Dang mo Settings de test scroll...")
    automation.start_app("com.android.settings")
    time.sleep(3)

    # Chung ta se lay bounds cua toan bo man hinh hoac mot vung cu the
    # Gia su chung ta muon cuon trong mot vung Box duoc dinh nghia (vi du vung giua man hinh)
    # Box format: [left, top, right, bottom]
    # Lay thong tin man hinh
    info = automation.device.info
    display_width = info.get('displayWidth')
    display_height = info.get('displayHeight')
    
    # SỬ DỤNG SỐ CỐ ĐỊNH ([left, top, right, bottom])
    # Ví dụ: Vùng từ Y=800 đến Y=1600 (Vùng hẹp ở giữa màn hình)
    test_box = [100, 800, 500, 1600] 
    
    print(f" - Thuc hien scroll 'down' ben trong BOX CO DINH: {test_box}")
    # Thêm steps=100 để vuốt chậm lại cho dễ nhìn
    automation.scroll(type_="down", box=test_box, steps=100)
    time.sleep(1)
    
    print(" - Thuc hien scroll 'up' ben trong BOX CO DINH...")
    automation.scroll(type_="up", box=test_box, steps=100)
    time.sleep(1)

    print("\n>>> [TEST 2.1] Scroll to END/TOP trong Box")
    # Tinh nang moi ban yeu cau: cuon xuong day/len dinh ben trong mot vung
    print(" - Dang cuon xuon DAY (bottom) ben trong Box...")
    automation.scroll(type_="bottom", box=test_box)
    time.sleep(1)
    
    print(" - Dang cuon len DINH (top) ben trong Box...")
    automation.scroll(type_="top", box=test_box)
    time.sleep(1)

    # ---------------------------------------------------------
    # TEST 3: Tinh nang cuon tim phan tu (Scroll to find) với Box
    # ---------------------------------------------------------
    print("\n>>> [TEST 3] scroll_to_find_element voi Box")
    # Tim mot muc trong Settings (vi du 'Display' hoac 'Hien thi')
    target_item = ["Display", "Display & brightness", "Màn hình", "Màn hình và độ sáng"]
    print(f" - Dang tim muc '{target_item}' trong Box...")
    
    element = automation.scroll_to_find_element(
        name=target_item, 
        type_="text", 
        type_scroll="down", 
        max_scrolls=10, 
        box=test_box
    )
    
    if element:
        print(f" - THANH CONG: Tim thay element tai bounds: {element.info.get('bounds')}")
        # Click thu luon
        element.click()
        print(" - Da click vao phan tu tim thay.")
        time.sleep(2)
        automation.press_key("back") # Quay lai
    else:
        print(" - KHONG TIM THAY phan tu trong so lan cuon cho phep.")

    print("\n>>> TAT CA TEST HOAN THANH.")

if __name__ == "__main__":
    main_start = time.time()
    try:
        test_new_features()
    except Exception as e:
        print(f"!!! CO LOI XAY RA: {e}")
    print(f"\nTong thoi gian test: {round(time.time() - main_start, 2)} giay")
