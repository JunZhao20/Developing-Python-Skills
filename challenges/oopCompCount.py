class Composer:
    lst = []
    def __init__(self, name, dob, country) -> None:
        
        self.name = name
        self.dob = dob
        self.country = country
        Composer.lst.append(self)
        Composer.count = len(Composer.lst)
        
c1 = Composer('jun', '02.10.2001', 'china')
c2 = Composer('jim', '123', '123')
print(Composer.count)