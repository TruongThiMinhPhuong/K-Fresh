import csv
import json

def loc_email_xin_nghi(file_csv, file_ket_qua):
    """
    Hàm đọc file CSV và lọc ra các email xin nghỉ phép
    """
    danh_sach_xin_nghi = []
    
    try:
        with open(file_csv, 'r', encoding='utf-8') as file:
            doc_gia = csv.DictReader(file)
            
            for dong in doc_gia:
                chuoi_kiem_tra = f"{dong['subject']} {dong['body']}".lower()
                
                if 'leave' in chuoi_kiem_tra:
                    danh_sach_xin_nghi.append({
                        "id": int(dong['id']),
                        "sender": dong['sender'],
                        "type": "leave_request"
                    })
        
    
        with open(file_ket_qua, 'w', encoding='utf-8') as file_json:
            json.dump(danh_sach_xin_nghi, file_json, indent=2, ensure_ascii=False)
            
        print(f" Đã tìm thấy {len(danh_sach_xin_nghi)} email xin nghỉ phép")
        print(f" Kết quả đã được lưu vào: {file_ket_qua}")
        
    except FileNotFoundError:
        print(" Lỗi: Không tìm thấy file emails.csv")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    loc_email_xin_nghi("emails.csv", "leave_requests.json")