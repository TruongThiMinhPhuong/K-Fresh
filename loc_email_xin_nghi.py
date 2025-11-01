import csv
import json

# Function lọc email xin nghỉ phép từ file CSV chứa dữ liệu email,
def filterEmails(input_file_csv, output_file_json, keywords):
    try:   
        leave_request_list = findLeaveRequestEmails(input_file_csv, keywords)
        
        with open(output_file_json, 'w', encoding='utf-8') as file_json:
            json.dump(leave_request_list, file_json, indent=2, ensure_ascii=False)
            
        print(f" Đã tìm thấy {len(leave_request_list)} email xin nghỉ phép")
        print(f" Kết quả đã được lưu vào: {output_file_json}")
        
    except FileNotFoundError:
        print(" Lỗi: Không tìm thấy file emails.csv")
    except Exception as e:
        print(f"Lỗi: {e}")

# Hàm tìm email xin nghỉ phép
def findLeaveRequestEmails(input_file_csv, keywords):
    """
    Hàm đọc file CSV và trả về danh sách email
    """
    leave_request_list = []
    try:
        with open(input_file_csv, 'r', encoding='utf-8') as file:
            csvEmailRows = csv.DictReader(file)
            for emailRow in csvEmailRows:
                subJectAndBody = f"{emailRow['subject']} {emailRow['body']}".lower()
                if isContainedKeywords(subJectAndBody, keywords):
                    leave_request_list.append({
                        "id": int(emailRow['id']),
                        "sender": emailRow['sender'],
                        "type": "leave_request"
                    })
        return leave_request_list
    
    except FileNotFoundError:
        print(" Lỗi: Không tìm thấy file emails.csv")
        return []
    except Exception as e:
        print(f"Lỗi: {e}")
        return []


# Hàm kiểm tra từ khóa trong subject và body có chứa keywords (leave, day off, ...)
def isContainedKeywords(subJectAndBody, keywords):
    for keyword in keywords:
        if keyword in subJectAndBody:
            return True
    return False


if __name__ == "__main__":
    # Gọi hàm lọc email xin nghỉ phép
    
    keywords = ['leave', 'day off', 'time off', 'vacation', 'sick leave']
    filterEmails("emails.csv", "leave_requests.json", keywords)