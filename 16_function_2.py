#transfer any amount of arguments
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping.title()}")

make_pizza('pepperoni')
make_pizza('pepperoni','green pepper','extra cheese')

#combine position argument & any amount of arguments
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping.title()}")

make_pizza(16,'pepperoni')
make_pizza(12,'pepperoni','green pepper','extra cheese')

#accept any number of key-value pair in function
def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile=build_profile('albert','einstein',
                          location='princeton',
                          field='physics')
print(user_profile)

#pratice 8-12
def order_sandwich(number,size,*ingredients):
    if number>1:
        print(f"I would like to order {number} {size} sandwiches with:")
    elif number==1: 
        print(f"I would like to order {number} {size} sandwich with:")
    for ingredient in ingredients:
        print(ingredient.title())

order_sandwich(2,'large','hum','cheese','tomato')

#pratice 8-13
def build_profile(first,last,gender,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    user_info['gender']=gender
    return user_info
user_profile=build_profile('xiaowen','sun','male',
                          location='seattle',
                          field='computer science')
print(user_profile)

#pratice 8-14
def make_car(brand,type,**info):
    info['brand']=brand
    info['type']=type
    print(info)

make_car('Tesla','4-seat',color='white',country='China')

#save function in module and import module
import pizza
pizza.make_another_pizza('pepperoni')
pizza.make_another_pizza('pepperoni','green pepper','extra cheese')

#import specific function in module
from pizza import make_another_pizza,make_final_pizza
make_final_pizza('pepperoni')
make_final_pizza('pepperoni','green pepper','extra cheese')

#set another name for import module or function
from pizza import make_final_pizza as mfp
mfp('pepperoni','green pepper','extra cheese')

import pizza as p
p.make_another_pizza('pepperoni')
p.make_another_pizza('pepperoni','green pepper','extra cheese')

#import all functions from module
from pizza import *
make_another_pizza('pepperoni','green pepper','extra cheese')
make_final_pizza('pepperoni')

#pratice 8-15
import printing_function as pf
unprinted_designs=['phone case','robot pendant','dodercahedron']
completed_models=[]
pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)
print(completed_models)
print(unprinted_designs)

from printing_function import print_models as pm
from printing_function import show_completed_models as scm
unprinted_designs=['phone case','robot pendant','dodercahedron']
completed_models=[]
pm(unprinted_designs,completed_models)
scm(completed_models)
print(completed_models)
print(unprinted_designs)