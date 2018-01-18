def main():
    N1 = list(input().lower())
    N2 = input().lower()
    N1list = list(N1)
    output = "N"
    trues=[]
    for ch in N2:
        if ch in N1list or ch =="*":
            trues.append(ch)
            if ch != "*":
                N1list.remove(ch)
        else:
            break
    if len(trues) == len(N1):
        output = "A"
    print(str(output))
main()