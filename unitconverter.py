def convert(value, from_unit, to_unit, conversion_dict):
    base = value * conversion_dict[from_unit]
    return base / conversion_dict[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15


def main():
    print("=== Unit Converter ===")
    print("Type 'quit' to exit.\n")

    categories = {
        "1": {
            "name": "Length",
            "units": {
                "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34,
                "nmi": 1852  # nautical mile
            }
        },
        "2": {
            "name": "Weight / Mass",
            "units": {
                "mg": 0.001, "g": 1, "kg": 1000, "t": 1000000,
                "oz": 28.3495, "lb": 453.592, "st": 6350.29  # stone
            }
        },
        "3": {
            "name": "Temperature",
            "units": ["C", "F", "K"]
        },
        "4": {
            "name": "Volume",
            "units": {
                "ml": 0.001, "l": 1, "m3": 1000,
                "tsp": 0.00492892, "tbsp": 0.0147868,
                "fl_oz": 0.0295735, "cup": 0.236588,
                "pt": 0.473176, "qt": 0.946353, "gal": 3.78541
            }
        },
        "5": {
            "name": "Area",
            "units": {
                "mm2": 0.000001, "cm2": 0.0001, "m2": 1, "km2": 1000000,
                "in2": 0.00064516, "ft2": 0.092903, "yd2": 0.836127,
                "acre": 4046.86, "ha": 10000  # hectare
            }
        },
        "6": {
            "name": "Speed",
            "units": {
                "mps": 1, "kph": 0.277778, "mph": 0.44704,
                "fps": 0.3048, "knot": 0.514444
            }
        },
        "7": {
            "name": "Time",
            "units": {
                "ms": 0.001, "s": 1, "min": 60, "hr": 3600,
                "day": 86400, "week": 604800, "year": 31536000
            }
        },
        "8": {
            "name": "Digital Storage",
            "units": {
                "b": 1, "kb": 1000, "mb": 1000000, "gb": 1000000000, "tb": 1000000000000,
                "kib": 1024, "mib": 1048576, "gib": 1073741824, "tib": 1099511627776
            }
        },
        "9": {
            "name": "Pressure",
            "units": {
                "pa": 1, "kpa": 1000, "bar": 100000,
                "psi": 6894.76, "atm": 101325, "torr": 133.322
            }
        },
        "10": {
            "name": "Energy",
            "units": {
                "j": 1, "kj": 1000, "cal": 4.184, "kcal": 4184,
                "wh": 3600, "kwh": 3600000, "btu": 1055.06
            }
        }
    }

    while True:
        print("Categories:")
        for key, cat in categories.items():
            print(f"{key}. {cat['name']}")
        print("11. Quit")

        choice = input("\nChoose a category (1-11): ").strip().lower()

        if choice == "11" or choice == "quit":
            print("Goodbye!")
            break

        if choice not in categories:
            print("Invalid option.\n")
            continue

        category = categories[choice]

        try:
            value = float(input("Enter value: ").strip())
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        # Temperature is special
        if choice == "3":
            print("\nUnits: C, F, K")
            from_unit = input("From unit: ").strip().upper()
            to_unit = input("To unit: ").strip().upper()

            if from_unit not in ["C", "F", "K"] or to_unit not in ["C", "F", "K"]:
                print("Invalid unit.\n")
                continue

            result = convert_temperature(value, from_unit, to_unit)
            print(f"\n{value}°{from_unit} = {result:.4f}°{to_unit}\n")
            continue

        # All other categories
        units = list(category["units"].keys())
        print(f"\nAvailable units: {', '.join(units)}")
        from_unit = input("From unit: ").strip().lower()
        to_unit = input("To unit: ").strip().lower()

        if from_unit not in category["units"] or to_unit not in category["units"]:
            print("Invalid unit.\n")
            continue

        result = convert(value, from_unit, to_unit, category["units"])
        print(f"\n{value} {from_unit} = {result:.6f} {to_unit}\n")


if __name__ == "__main__":
    main()