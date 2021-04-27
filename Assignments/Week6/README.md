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
Dự đoán doanh thu của bộ phim chính là mục tiêu cần tìm ra

**Thu thập data**:  
Rất nhiều các chỉ số về những bộ phim trước như:
    +Doanh thu đạt được
    +Chi phí sản xuất
    +Nhà sản xuất
    +Ngày công chiếu
    +...
Data dạng bảng thu được tại web: https://www.the-numbers.com/weekend-box-office-chart#box_office_weekend_table=od3. Chuyển data dạng bảng về file .csv.

**Xử lý data**:
Loại bỏ các bộ phim có các chỉ số bất hợp lý như: doanh thu bằng 0 do có ngày công chiếu lớn hơn hiện tại, lọc bớt những bộ phim chỉ vừa công chiếu trong khoảng 2 hoặc 3 tuần.
Sau đó loại các cột thứ hạng phim, ngày phát hành, doanh thu trong nước. Do ta chỉ cần doanh thu, chi phí sản xuất và nhà sản xuất là 3 thuộc tính có vẻ quan trọng nhất trong việc dự đoán này.

## **Ví dụ 3**: 
## **Ví dụ 3**: Dự đoán chất lượng của bánh trong một dây chuyền sản xuất:

**INPUT**:
	+ nhiệt độ của lò nướng 
	+ thời gian ở trong lò 
	+ thành phần của bột 
	+ thời gian ủ bột 
	+ nhiệt độ của môi trường trong nhà máy 
	+ độ ẩm của môi trường 
	+...
**OUTPUT**:
 chất lượng của mẻ bánh ( độ ngon , độ gòn của bánh vv)

**Thu thập data**:  
 tất cả các thông tin trên chúng ta đều có thể thu thập thủ công tại các nhà máy bánh , các nhà máy công nghiệp 
luôn luôn đầu tư các hệ thống tracking để thu thập nhưng thông tin này và cũng như đội ngũ giám sát chất lượng sẽ 
vô cùng chính xác theo dõi từng bước của quá trình . bước cuối là chất lượng , đây là một điểm mang tính chất khách quan , vậy tên ta sẽ cần 1 lượng người thử đủ rộng để không bị bias ,tuy nhiên ta ko thể đến 1 mẻ bánh làm ra lại đem đi ăn thử hết . Vậy ta phải đi tham khảo khách hàng mua bánh để cải thiện sản phẩm (feedback từ khách hàng).
tổng quát các thông tin thành 1 file csv/json hoàn thiện .

**Xử lý data**:
 làm sạch dữ liệu bằng cách đồng bộ các dữ liệu về cùng 1 loại đơn vị do và làm tròn các thông số , loại bỏ các null 
và các thông tin thừa không đáng giá và không ảnh hưởng nhiều tới output .

