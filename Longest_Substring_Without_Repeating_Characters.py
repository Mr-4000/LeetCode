s="pwwwkew"
arr = []
for i in range(0,26):
    arr.append(0)
max = 0
temp = 0
for i in range(0,len(s)):
    temp = temp + 1
    if (arr[ord(s[i])-97]!=0):
        a = arr[ord(s[i])-97]
        temp = temp - a
        for j in range(0,26):
            arr[j] = arr[j] - a
            if (arr[j] < 0):
                arr[j] = 0
    if (max<temp):
        max = temp
    arr[ord(s[i])-97] = temp
print(max)