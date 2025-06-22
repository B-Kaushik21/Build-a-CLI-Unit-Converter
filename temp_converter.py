import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def check_health_status(value, unit):
    if unit == "F":
        if value <= 99:
            return "Normal"
        else:
            return "Fever"
    elif unit == "C":
        if value <= 37.2:
            return "Normal"
        else:
            return "Fever"
    else:
        return "Unknown unit"

def main():
    parser = argparse.ArgumentParser(description="Convert temperature between Celsius and Fahrenheit and check health status.")

    parser.add_argument("temperature", type=float, help="The temperature value to convert.")
    parser.add_argument("--from_unit", choices=["C", "F"], required=True, help="The unit to convert from: C or F.")
    parser.add_argument("--to_unit", choices=["C", "F"], required=True, help="The unit to convert to: C or F.")

    args = parser.parse_args()

    original = args.temperature
    if args.from_unit == args.to_unit:
        print(f"No conversion needed. Temperature is {original}°{args.to_unit}.")
        status = check_health_status(original, args.to_unit)
    elif args.from_unit == "C" and args.to_unit == "F":
        converted = celsius_to_fahrenheit(original)
        print(f"{original}°C = {converted:.2f}°F")
        status = check_health_status(converted, "F")
    elif args.from_unit == "F" and args.to_unit == "C":
        converted = fahrenheit_to_celsius(original)
        print(f"{original}°F = {converted:.2f}°C")
        status = check_health_status(converted, "C")
    else:
        print("Invalid conversion.")
        return

    print(f"Health Status: {status}")

if __name__ == "__main__":
    main()
