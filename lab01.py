while True:
    name = input("Enter Your Name: ")
    if name.lower() == "exit":
        break

    unit = int(input("Enter unit :"))

    electricity_usage = float()
    mont = float()

    if unit <= 150:
        if unit > 0 and unit < 16:
            electricity_usage = 2.3488
        elif unit > 15 and unit <= 25:
            electricity_usage = 2.9882
        elif unit > 25 and unit <= 35:
            electricity_usage = 3.2405
        elif unit > 35 and unit <= 100:
            electricity_usage = 3.6237
        elif unit > 100 and unit <= 150:
            electricity_usage = 3.7171
        elif unit > 150 and unit <= 400:
            electricity_usage = 4.2218
        elif unit > 400:
            electricity_usage = 4.4217
        mont = 8.19
    else:
        if unit > 0 and unit <= 150:
            electricity_usage = 3.2484
        elif unit > 150 and unit <= 400:
            electricity_usage = 4.2218
        elif unit > 400:
            electricity_usage = 4.4217
        mont = 38.22
    electricity_usage = electricity_usage * unit + mont
    ft_fee = unit * 0.2048
    vat = (ft_fee + electricity_usage) * 7 / 100
    payment = ft_fee + electricity_usage + vat

    print(f"Name = {name}")
    print(f"Payment = {payment:.2f}")
    print(f"vat = {vat:.2f}")
