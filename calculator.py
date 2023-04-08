# Application that can check the age of a person
# input name and age in the application
# 18 years below access will be denied


current_year = 2023
Average_age = 18 #int

def age_calc():
    name_of_student = input("enter student name: ")
    age_calculator = int(input("enter student date of birth: "))
    if age_calculator <= 2005 :
        final_age = current_year - age_calculator
        print("True!",name_of_student, "your age is", final_age, "years,you are qualified")
    else:
        final_age = current_year - age_calculator
        print("false!",name_of_student, "your age is", final_age, "years, you are not qualified yet")
age_calc()
    
