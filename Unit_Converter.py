import argparse
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    parser = argparse.ArgumentParser(description="Temperature conversion between Celsius and Fahrenheit:")
    parser.add_argument(
        "temperature",
        type=float,
        help="The temperature value to convert:"
    )
    parser.add_argument(
        "--from_unit",
        choices=["C", "F"],
        required=True,
        help="The unit to convert from: C (Celsius) or F (Fahrenheit)."
    )
    parser.add_argument(
        "--to_unit",
        choices=["C", "F"],
        required=True,
        help="The unit to convert to: C (Celsius) or F (Fahrenheit)."
    )

    args = parser.parse_args()

    if args.from_unit == args.to_unit:
        print(f"No conversion needed. Temperature is {args.temperature}°{args.to_unit}.")
    elif args.from_unit == "C" and args.to_unit == "F":
        converted = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}°C = {converted:.2f}°F")
    elif args.from_unit == "F" and args.to_unit == "C":
        converted = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}°F = {converted:.2f}°C")
    else:
        print("Invalid conversion!!Please check your inputs.")

if __name__ == "__main__":
    main()
