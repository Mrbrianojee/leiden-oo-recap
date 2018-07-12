class Employee(object):
    
    BASE_SALARY =  5000
    
    fname = ''
    sname = ''
    no_of_years = 0
    
    def __init__(self, fname, sname, no_of_years):
        self.fname  = fname
        self.sname  = sname
        self.no_of_years  = no_of_years
    
    def calculate_salary(self):
        bonus = 0
        salary =  self.BASE_SALARY
        
        if self.no_of_years < 3:
            return salary + salary * .05
        elif self.no_of_years <= 5:
            return salary + salary * .1
        elif self.no_of_years > 5:
            return salary + salary * .25
        
    def get_details(self):
         return " First Name: {0}\n Surname: {1}\n Number of Years: {2}\n Salary: {3}\n".format(
         self.fname, 
         self.sname, 
         self.no_of_years, 
         self.calculate_salary()
         )
         
         
class Developer(Employee):
    def __init__(self, fname, sname, no_of_years, prog_lang):
        super(Developer, self).__init__(fname, sname, no_of_years)
        self.prog_lang = prog_lang

    def calculate_salary(self):
        basic_salary = super(Developer, self).calculate_salary()
        
        if self.prog_lang.lower() == "python":
            return basic_salary + basic_salary * .05
        elif self.prog_lang.lower() == "java":
            return basic_salary + basic_salary * .01
            
    
    def get_details(self):
        return super(Developer, self).get_details()+" Programming language: {0}".format(self.prog_lang)