def make_car(maker,typer,**information):
    car = {}
    car["maker"] = maker
    car["typer"] = typer
    for key,value in information.items():
        car[key] = value
    return car

car = make_car('sabaru','outback',color = 'blue',tow_package = True)

for key,value in car.items():
    print(str(key)+"  "+str(value))
