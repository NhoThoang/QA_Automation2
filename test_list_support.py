from qa_automation2 import qa_connect
import time

def main():
    try:
        print("Connecting to device...")
        # Assuming generic connection works as per test_guide.py
        automation = qa_connect(log_dir="logs/test_list")
        if not automation:
            print("Failed to connect")
            return

        print("Connected.")
        
        # Test 1: List with non-existent and existent element names
        # We need a name that likely exists. 
        # Let's get all text first to see what's there, then pick one.
        texts = automation.get_all_text_element(action="text_all")
        if not texts:
            print("No text found on screen to test with.")
            existing_text = "Settings" # Fallback
        else:
            existing_text = texts[0]
            print(f"Found existing text on screen: '{existing_text}'")

        non_existent_text = "NON_EXISTENT_ELEMENT_XYZ_123"
        
        print(f"\n--- Testing Find_element with list: ['{non_existent_text}', '{existing_text}'] ---")
        found_element = automation.Find_element(name=[non_existent_text, existing_text], type_="text")
        
        if found_element:
            print(f"Success! Found element: {found_element.info.get('text')}")
        else:
            print("Failed to find element with list.")

        # Test 2: List with only non-existent
        print(f"\n--- Testing Find_element with list: ['{non_existent_text}'] ---")
        not_found = automation.Find_element(name=[non_existent_text], type_="text")
        if not not_found:
             print("Success! Did not find non-existent element.")
        else:
             print(f"Fail? Found: {not_found}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
