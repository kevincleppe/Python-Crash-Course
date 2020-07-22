def cars(make,model, **car_info):
    car_info['make']=make
    car_info['model']=model 
    return car_info


my_car=cars('toyota', 'prius',year='2004',color='black')

print(my_car)