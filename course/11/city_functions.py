def city_combine(city,nation,population = 0):
    if population == 0:
        infor = city.title() +","+nation.title()
    else:
        infor = city.title() +","+nation.title()+" - population "+str(population)
    return infor
