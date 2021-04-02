import bisect

def SoGan_X(lst,x):
    i=bisect.bisect_left(lst,x)
    return i

def K_SoGan_X(k,x,lst):
    lst_result=[]
    pos=SoGan_X(lst,x)

    #nhỏ hơn hoặc bằng giá trị đầu tiên
    if pos==0:
        return lst[0:k]
    #lớn hơn giá trị cuối cùng
    elif pos>=len(lst)-1:
        return lst[len(lst)-k:len(lst)]
    else:
        l=pos
        r=pos+1
        #gán giá trị đầu tiên gần =x hoặc gần x nhất
        if lst[pos]==x or x-lst[l] <= lst[r]-x:
            lst_result.append(lst[pos])
            l-=1
        else:
            lst_result.append(lst[pos+1])
            r+=1
        count=1

        while(count!=k):
            if l<0 and r<len(lst)-1 : # append từ bên trái qua
                lst_result.append(lst[r])
                r+=1
            elif r>len(lst)-1 and l>=0: # append từ bên phải qua
                lst_result.append(lst[l])
                l-=1
            else: # so sánh bên nào nhỏ thì append
                if x-lst[l] <= lst[r]-x:
                    lst_result.append(lst[l])
                    l-=1
                else:
                    lst_result.append(lst[r])
                    r+=1
            count+=1
    return lst_result

a=input()
lst=list(map(int,input().split()))

 
while(1):
    b=list(map(int,input().split()))
    if len(b)==0:
        break
    else:
        result=sorted(K_SoGan_X(b[0],b[1],lst))
        print(result[0],result[-1])