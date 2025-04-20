temperature = float(input("Введите температуру: "))
is_rainy = input("Есть осадки? (y/n): ")
if is_rainy == "y":
    rain = True
else:
    rain = False
if rain:
    is_raining_heavily = input("Осадки сильные? (y/n): ")
    if is_raining_heavily == "y":
        heavy_rain = True
    else:
        heavy_rain = False
else:
    heavy_rain = False
if temperature <= 0:
    print("Пуховик")
else:
    if temperature <= 20:
        if is_rainy:
            if is_raining_heavily:
                print("Пальто, резиновые сапоги и зонт")
            else:
                print("Пальто и дождевик")
        else:
            print("Пальто")
    else:
        if temperature < 30:
            if is_rainy:
                print("Футболку, шорты и дождевик")
            else:
                print("Футболку и шорты")
        else:
            if is_rainy:
                if is_raining_heavily:
                    print("Пальто, резиновые сапоги и зонт")
                else:
                    print("Футболку, шорты и дождевик")
            else:
                print("Футболку и шорты")