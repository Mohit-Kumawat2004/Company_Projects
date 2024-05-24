def calculate_bmi(weight, height):
    
    #Calculating the Body Mass Index (BMI) from weight (kg) and height (m).
    
    try:
        weight = float(weight)  # Convert weight to a float
        height = float(height)  # Convert height to a float
    except ValueError:
        # If conversion fails, print The error message and returns
        print("Invalid input. Weight and height must be numeric.")
        return None

    if weight <= 0 or height <= 0:
        # Check if weight or height is less than or equal to 0, which is invalid
        print("Weight and height must be positive values.")
        return None

    # Convert height from feet to meters (since 1 foot = 0.3048 meters)
    height_meters = height * 0.3048

    # Calculate BMI using the formula: BMI = weight / (height in meters)^2
    bmi = weight / (height_meters ** 2)
    return bmi  # Return the calculated BMI

def get_bmi_category(bmi):
   
   #Classify the BMI value into various categories.
   
    # Determine the BMI category based on the value of BMI
    if bmi < 16.0:
        category = "Severely Underweight"
    elif bmi < 17.0:
        category = "Moderately Underweight"
    elif bmi < 18.5:
        category = "Mildly Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal"
    elif bmi < 30.0:
        category = "Overweight"
    elif bmi < 35.0:
        category = "Obese Class I"
    elif bmi < 40.0:
        category = "Obese Class II"
    else:
        category = "Obese Class III"
    return category  # Return the BMI category

def main():
    while True:
        # User will input their weight in kilograms
        weight = input("Enter your weight in kilograms: ")
        # User will input their height in feet
        height_feet = input("Enter your height in feet: ")

        # Calculate BMI using the calculate_bmi function
        bmi = calculate_bmi(weight, height_feet)
        if bmi is None:
            # If BMI calculation failed (None), continue the loop and ask for input again
            continue

        # Calling Function and storing in variable
        category = get_bmi_category(bmi)

        # Print the calculated BMI and the corresponding category
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")

        # Ask the user if they want to continue
        choice = input("Do you want to continue? (YES[y]/NO[n]): ")
        if choice.lower() != 'y':
            # If the user does not choose 'y', break the loop and exit
            break

# COde will work main function calling
if __name__ == "__main__":
    main()
