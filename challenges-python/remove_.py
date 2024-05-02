class List:
    def remove_(self, integer_list, values_list):
        
        for x in set(values_list):
            for i in integer_list:
                if x in integer_list:
                    integer_list.remove(i)
                
        return integer_list
    
l = List()
integer_list = [4, 4, 2 , 3]
values_list  = [2, 2, 4, 3]
print(l.remove_(integer_list, values_list))