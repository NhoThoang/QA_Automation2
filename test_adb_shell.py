from qa_automation2 import qa_connect

def test_adb_shell():
    print("Connecting to device...")
    try:
        automation = qa_connect(log_dir="logs_adb")
        print(f"Connected: {automation.device.serial}\n")
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    # --- CASE 1: Lệnh OK có output ---
    print(">>> Test 1: ls /sdcard (Expected: List of files)")
    res1 = automation.abd_shell("ls /sdcard | head -n 3") # Lấy 3 dòng đầu cho gọn
    print(f"Result Value: {repr(res1)}") # repr() để hiển thị rõ chuỗi, ký tự đặc biệt
    
    # Kiểm tra kĩ kiểu dữ liệu trả về
    if res1 is not False: 
        print("-> STATUS: SUCCESS (OK)\n")
    else:
        print("-> STATUS: FAILED (Error)\n")

    # --- CASE 2: Lệnh OK không output (Ví dụ lệnh input, settings...) ---
    print(">>> Test 2: input keyevent 3 (Expected: Empty string '')")
    res2 = automation.abd_shell("input keyevent 3")
    print(f"Result Value: {repr(res2)}") 
    
    if res2 is not False:
        print("-> STATUS: SUCCESS (OK - Empty string is valid for no-output commands)\n")
    else:
        print("-> STATUS: FAILED (Error)\n")

    # --- CASE 3: Lệnh Lỗi (File/Folder không tồn tại) ---
    print(">>> Test 3: ls /folder_khong_ton_tai (Expected: False)")
    res3 = automation.abd_shell("ls /folder_khong_ton_tai")
    print(f"Result Value: {res3}")
    
    if res3 is False:
        print("-> STATUS: SUCCESS (Correctly identified error)\n")
    else:
        print(f"-> STATUS: FAILED (Should be False but got: {res3})\n")

    # --- CASE 4: Lệnh Lỗi (Command not found) ---
    print(">>> Test 4: lenh_nay_khong_co (Expected: False)")
    res4 = automation.abd_shell("lenh_nay_khong_co")
    print(f"Result Value: {res4}")
    
    if res4 is False:
        print("-> STATUS: SUCCESS (Correctly identified error)\n")
    else:
        print(f"-> STATUS: FAILED (Should be False but got: {res4})\n")

if __name__ == "__main__":
    test_adb_shell()
