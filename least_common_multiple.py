def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    LCMarr = arr[0]
    
    for i in range(len(arr)):
        GCDarr = GCD(LCMarr, arr[i])
        LCMarr = LCMarr * arr[i] // GCDarr
    
    return LCMarr
        