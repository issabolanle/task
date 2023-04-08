# Python function that takes 10list


colors = ['blue', 'hisense', 'white', 'champagne', 'orange']
fruit = ['cherry', 'tangerine', 'orange', 'apple', 'hisense']
phone = ['hisense', 'infinx','orange', 'samsung', 'tecno']
drinks = ['vodca', 'orange', 'champagne', 'hisense', 'liquor']
laptop = ['samsung', 'apple', 'hisense', 'orange', 'hp']
Makeup = ['mascara', 'orange', 'eyeliner', 'hisense', 'blush']
coffee = ['black', 'nescafe', 'orange','tetley', 'hisense']
software = ['python', 'orange', 'html', 'hisense', 'javascript']
Tablet = ['hisense', 'andriod', 'xiaomi', 'orange', 'infinix']
conditioner = ['thermocool', 'orange', 'scanfrost', 'hisense']

common_elements = set(colors).intersection(fruit,phone,drinks,laptop,Makeup,coffee,software,Tablet,conditioner)

def cohort_four():
    if common_elements:
        print('true', 'The common_elements are', common_elements)
    else:
        print('false', 'There are no common element')

cohort_four()

