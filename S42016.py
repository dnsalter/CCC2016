def main():
    N = eval(input())
    balls = input().split(" ")
    keepgoing = True
    while keepgoing == True:
        trueCount = 0
        for i in range(len(balls)):
            try:
                if balls[i] == balls[i+1]:
                    trueCount+=1
                    break
                elif balls[i] == balls[i+2]:
                    trueCount+=1
                    break
            except IndexError:
                if trueCount == 0:
                    keepgoing = False
                    break
        if keepgoing == False:
            break
        for i in range(len(balls)):
            if balls[i] == balls[i+1]:
                x = balls.pop(i)
                y = balls.pop(i)
                balls.insert(i,str(int(x) + int(y)))
                break
            elif balls[i] == balls[i+2]:
                x = balls.pop(i)
                y = balls.pop(i)
                z = balls.pop(i)
                balls.insert(i,str(int(x)+int(y)+int(z)))
                break
    large = 0
    for item in balls:
        if int(item) >= large:
            large = int(item)
    print(large)
main()
