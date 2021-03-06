m = str(input()).lower()
temp = ["A","O","Y","E","U","I","a","o","e","u","i","y"]
'''
Chương trình sẽ yêu cầu nhập một chuỗi, 
sau đó nếu có chữ viết hoa trong chuỗi thì thay thế chúng bằng những chữ viết thường.
Xóa hết tất cả các nguyên âm và chèn dấu "." trước mỗi phụ âm có trong chuỗi đó.
'''
s = ''
for i in m:
    if i in temp:
        m = m.replace(i,'')

for i in m:
    s = s + '.'
    if i != '.':
        s = s + i

print(s)