def smallest(K):
    small = 100000000
    for item in K:
        if int(item) < small:
            small = int(item)
    return small

def largest(K):
    large = 0
    for item in K:
        if int(item) > large:
            large = int(item)
    return large

def main():
    qType = input()
    N = eval(input())
    D = input().split(" ")
    P = input().split(" ")
    speed = 0
    for i in range(N):
        highD = largest(D)
        highP = largest(P)
        smallD = smallest(D)
        smallP = smallest(P)
        if qType == "1":
            D.remove(str(highD))
            P.remove(str(highP))
            highspeed = highD
            if highP > highspeed:
                highspeed = highP
        else:
            highspeed = highP
            lowspeed = smallD
            if highD >= highP:
                highspeed = highD
                lowspeed = smallP
                D.remove(str(highspeed))
                P.remove(str(lowspeed))
            else:
                D.remove(str(lowspeed))
                P.remove(str(highspeed))
        speed+=(highspeed)
    print(str(speed))
main()