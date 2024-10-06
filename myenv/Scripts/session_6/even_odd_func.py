def even_odd_func ():
    even_lst = []
    odd_lst  = []

    for i in range (2,10):
        if i % 2 == 0 :
            even_lst.append(i)
        else :
            odd_lst.append(i)
                           
        i += 1
    print("even numbers",even_lst) 
    print("odd numbers",odd_lst) 

even_odd_func()        