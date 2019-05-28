def make_car(manufacturar, model, **extra_info):
    """Write function that stores information about a car in a dictionary."""
    car_dict = {}
    car_dict['manufacturar_name'] = manufacturar.title()
    car_dict['model_name'] = model.title()
    for key, value in extra_info.items():
        car_dict[key] = value
    return car_dict


car = make_car('subaru', 'wrc', color='blue', tow_package=True)

print(car)
