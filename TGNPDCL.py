# write a python program for electricity bill program using functions that reads Previous Units, Current Units, and Customer Type, calculates units consumed(Domestic,Commercial,Industrial)dont calculate final bill. 
def calculate_units_consumed(previous_units, current_units): #task1
    if current_units < previous_units:
        raise ValueError("Current Units cannot be less than Previous Units.")
    return current_units - previous_units
# Main function to get user input and calculate units consumed
def main():
    try:
        previous_units = float(input("Enter Previous Units: "))
        current_units = float(input("Enter Current Units: "))
        customer_type = input("Enter Customer Type (Domestic/Commercial/Industrial): ")

        units_consumed = calculate_units_consumed(previous_units, current_units)
        print(f"\nUnits Consumed for {customer_type} customer: {units_consumed} units\n")

    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
# Function to calculate energy charges
def calculate_energy_charges(units_consumed, customer_type):#task2
    if customer_type == 'Domestic':
        if units_consumed <= 100:
            return units_consumed * 1.5
        elif units_consumed <= 300:
            return (100 * 1.5) + ((units_consumed - 100) * 2.5)
        else:
            return (100 * 1.5) + (200 * 2.5) + ((units_consumed - 300) * 4.0)
    elif customer_type == 'Commercial':
        if units_consumed <= 100:
            return units_consumed * 2.0
        elif units_consumed <= 300:
            return (100 * 2.0) + ((units_consumed - 100) * 3.5)
        else:
            return (100 * 2.0) + (200 * 3.5) + ((units_consumed - 300) * 5.0)
    elif customer_type == 'Industrial':
        if units_consumed <= 100:
            return units_consumed * 3.0
        elif units_consumed <= 300:
            return (100 * 3.0) + ((units_consumed - 100) * 4.5)
        else:
            return (100 * 3.0) + (200 * 4.5) + ((units_consumed - 300) * 6.0)
    else:
        raise ValueError("Invalid customer type. Please enter 'Domestic', 'Commercial', or 'Industrial'.")
        # Function to calculate fixed charges
def calculate_fixed_charges(customer_type):#task3
    if customer_type == 'Domestic':
        return 50.0
    elif customer_type == 'Commercial':
        return 100.0
    elif customer_type == 'Industrial':
        return 150.0
    else:
        raise ValueError("Invalid customer type. Please enter 'Domestic', 'Commercial', or 'Industrial'.")
        # Electricity Duty(percentage of energy charges)
def calculate_electricity_duty(energy_charges, customer_type):#task4
    if customer_type == 'Domestic':
        return energy_charges * 0.05  # 5% duty
    elif customer_type == 'Commercial':
        return energy_charges * 0.10  # 10% duty
    elif customer_type == 'Industrial':
        return energy_charges * 0.15  # 15% duty
    else:
        raise ValueError("Invalid customer type. Please enter 'Domestic', 'Commercial', or 'Industrial'.")
# Function to print the bill
def print_bill(previous_units, current_units, customer_type):#task5
    units_consumed = current_units - previous_units
    energy_charges = calculate_energy_charges(units_consumed, customer_type)
    fixed_charges = calculate_fixed_charges(customer_type)
    electricity_duty = calculate_electricity_duty(energy_charges, customer_type)
    total_amount = energy_charges + fixed_charges + electricity_duty

    print("\nElectricity Bill")
    print("----------------------------")
    print(f"Customer Type      : {customer_type}")
    print(f"Previous Units     : {previous_units}")
    print(f"Current Units      : {current_units}")
    print(f"Units Consumed     : {units_consumed}")
    print(f"Energy Charges     : ${energy_charges:.2f}")
    print(f"Fixed Charges      : ${fixed_charges:.2f}")
    print(f"Electricity Duty   : ${electricity_duty:.2f}")
    print("----------------------------")
    print(f"Total Amount       : ${total_amount:.2f}")
    print("----------------------------\n")
# Main function to get user input and generate the bill
def main():
    try:
        previous_units = float(input("Enter Previous Units: "))
        current_units = float(input("Enter Current Units: "))
        customer_type = input("Enter Customer Type (Domestic/Commercial/Industrial): ")

        if current_units < previous_units:
            raise ValueError("Current Units cannot be less than Previous Units.")

        print_bill(previous_units, current_units, customer_type)

    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
    #print total bill
    print_bill(previous_units, current_units, customer_type)
