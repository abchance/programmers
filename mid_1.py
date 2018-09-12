def solution(s):
    if len(s)%2 == 1: print(s[int(len(s)/2)])
    else: print(s[int(len(s)/2-1)],s[int(len(s)/2)])

s=str(input())
solution(s)

    


