# CS114.L21-L22.KHCL 
# Danh sách thành viên:
| Họ và tên      | MSSV | Lớp     |
| :---        |    :----:   |          ---: |
| [Nguyễn Lê Anh Quân](https://github.com/anhquan075 "Quân's github")      | 19522081       | CS114.L22.KHCL  |
| [Lý Hoàng Thuận](https://github.com/20-8-21-1-14 "Thuận's github")   | 19522315        | CS114.L22.KHCL      |
| [Phan Thành Nhân](https://github.com/pthanhnhan "Nhân's github") | 19521944 | CS114.L21.KHCL|
# Bài tập tuần 6: 
*Câu hỏi quá trình:
Mỗi nhóm tìm dăm ba ví dụ về bài toán regression ***TRONG THỰC TẾ***
Ghi rõ input, output và cách thu thập + xử lý data, commit vào github repository và dẫn link lên đây.
Có thể ghi ra giấy rồi chụp hình hoặc viết ở dạng Markdown.*
## **Ví dụ 1**:  Dự báo thời gian sinh viên tốt nghiệp của sinh viên Trường Đại Học Công Nghệ Thông Tin:
**INPUT**: 
Đầu vào bao gồm các thuộc tính như sau: Điểm trung bình tích lũy, số lần rớt môn, số môn còn nợ phải trả, điểm rèn luyện trung bình, số tín chỉ tích lũy, số buổi vắng trung bình trong các kỳ.

**OUTPUT**:
Thời gian tốt nghiệp của sinh viên

**Thu thập data**:  
Thông thường nhà trường sẽ post danh sách các sinh viên đạt chuẩn tốt nghiệp mỗi đợt trên trang chủ của trường ở định dạng xlsx (File excel), với title chung là "Danh sách sinh viên dự kiến tốt nghiệp khóa X". Ta có thể crawl tự động bằng thư viện Selenium theo từ khóa kể trên và gom các file xlsx lại thành một khối định dữ liệu chung có thể ở định dạng CSV hoặc JSON.

**Xử lý data**:
- Loại bỏ các điểm dữ liệu bị trống ( null ) hoặc thay thế chúng bằng độ lệch chuẩn của đặc tính đó để tránh việc mô hình học những điểm dữ liệu lỗi kiến cho sai lệch trong việc dự đoán.

## **Ví dụ 2**: 
## **Ví dụ 2**: Dự đoán doanh thu của 1 bộ phim mới ra mắt cho bài đăng tạp chí:
**INPUT**: 
Các chỉ số về bộ phim đó như:
    +Chi phí sản xuất
    +Nhà sản xuất

**OUTPUT**:
Doanh thu của bộ phim chính là mục tiêu cần tìm ra

**Thu thập data**:  
Rất nhiều các chỉ số về những bộ phim trước như:
    +Doanh thu đạt được
    +Chi phí sản xuất
    +Nhà sản xuất
    +Ngày công chiếu
    +...
Data dạng bảng thu được tại web: https://www.the-numbers.com/weekend-box-office-chart#box_office_weekend_table=od3. Chuyển data dạng bảng về file .csv.

**Xử lý data**:
Loại bỏ các bộ phim có các chỉ số bất hợp lý như doanh thu bằng 0 do có ngày công chiếu lớn hơn hiện tại, lọc bớt những bộ phim chỉ vừa công chiếu được 2 hoặc 3 tuần.
Sau đó loại các cột thứ hạng phim, ngày phát hành, doanh thu trong nước. Do ta chỉ cần doanh thu, chi phí sản xuất và nhà sản xuất là 3 thuộc tính có vẻ quan trọng nhất trong việc dự đoán này.

## **Ví dụ 3**: 

**INPUT**: 

**OUTPUT**:

**Thu thập data**:  

**Xử lý data**:
