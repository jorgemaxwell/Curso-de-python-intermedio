def run():
    my_list= [1,2,3,4,5]
    power=list(map(lambda x: x**2, my_list))
    print(power)

if __name__=='__main__':
    run()