def delete_nth(order,max_e):
    
    for i in order:
        if order.count(i) > max_e:
            print(i)
     
print(delete_nth([20,37,20,21,21], 1))