from qa_automation2 import qa_connect
import time

def main():
    try:
        # 1. Kết nối
        print("Connecting to device...")
        automation = qa_connect(log_dir="logs/logs_test")
        print(f"Connected to device model: {automation.device_information.get('model')}")

        # 2. Test text_all
        print("\n--- TEST text_all (Lấy toàn bộ text trên màn hình) ---")
        texts = automation.get_all_text_element(action="text_all")
        if texts:
            print(f"Found {len(texts)} texts.")
            # In thử 10 cái đầu tiên để đỡ dài
            print(f"Sample: {texts[:10]}...") 
        else:
            print("No text found.")

        # 3. Test talkback_all
        print("\n--- TEST talkback_all (Lấy toàn bộ description) ---")
        talkbacks = automation.get_all_text_element(action="talkback_all")
        if talkbacks:
            print(f"Found {len(talkbacks)} talkbacks.")
            print(f"Sample: {talkbacks[:10]}...")
        else:
            print("No talkback found.")

        # 4. Test text_child (Ví dụ tìm List/Recycler View)
        # Bạn cần sửa 'name' và 'type_' bên dưới để trỏ đúng vào một container (như ListView, RecyclerView, LinearLayout...) trong app bạn đang mở
        target_class = "android.widget.FrameLayout" # Ví dụ FrameLayout thường chứa nhiều con
        print(f"\n--- TEST text_child (Lấy text con của {target_class}) ---")
        
        children_texts = automation.get_all_text_element(
            name=target_class, 
            type_="class_name", 
            action="text_child"
        )

        if children_texts:
            print(f"Found {len(children_texts)} children texts:")
            print(children_texts)
        else:
            print(f"No element found for {target_class} or it has no text children.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
