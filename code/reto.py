def run():
    numbers=[]
    for i in range (101):
        if i % 3 != 0:
            numbers.append(i**2)
    print (numbers)

if __name__=="__main__":
    run()