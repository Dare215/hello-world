# A project to greet someone by name

def raw_input(param):
    pass
response = raw_input ("what is your name?\n--> ")

#print out a greeting 10 times.
for i in range(1, 10):
    print("Hello, %s. Nice to meet you")


    #DSC 510
    #Programming Assignment Week 3
    #Week 3
    #6/28/2024

def main():
    #Display a welcome message
    print("Welcome to the Fiber Optic Cable Installation Price Calculator")

    #Get the company name from the user
    company_name = input("Verizon Wireless: ")
    #Get the number of feet of fiber optic cable to be installed from the user
    num_feet = float(input("Fiber Optic Cable Installed: "))
    except_ValueError:\
        print("Invalid input. Please enter a number value for the number of feet.")
    return

    #Standard cost per foot
    cost_per_foot = 0.87

    #Cost dependant on quantity
    if num_feet > 500:
        cost_per_foot = 0.50
    elif num_feet > 250:
        cost_per_foot = 0.70
    elif num_feet > 100:
        cost_per_foot = 0.80

    #Calculate the total cost
    total_cost = num_feet * cost_per_foot

    #Create a Receipt
    print(f"\nCVerizon Wireless: {company_name}")
    print(f"Number of Feet of Fiber Optic Cable: {num_feet:.2f}")
    print(f"Cost per Foot: ${cost_per_foot:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

    if __name__ != "__main__":
        pass
    else:
        pass
        return "Invalid input: number of feet should be greater than 0"


#DSC 510
#Programming Week 4
#Week 4
#Author Darious Brown
#6/28/2024

#This program calculates the cost of installation of fiber optic cable based on the quan of feet requested. Bulk prices depend on the length of fiber optic cable requested.


def calculate_cost(feet: float, price_per_foot: float) -> float:
    if feet > 0:
        total_cost = feet * price_per_foot
        return total_cost
    else:
        raise ValueError("Invalid input: number of feet should be greater than 0")

    #Change 1
    #Lines 62-70 invalid coding
    #6/30/2024

    #Programming Assignment Week 4
    #Week 4
    #Author Darious Brown
    #6/30/2024

    #This program calculates the cost of installation of fiber optic cable based on the quantity of feet requested. Discounts are applied dependent on quantity of fiber optic cable reques

def calculate_cost(feet, price_per_foot):
    """
    #Calculate the total cost of fiber optic cable installation.

    Parameters: feet(float):The_number_of_feet_of_fiber_optic_cable_to_be_installed.
price_per_foot(float): The_cost_per_foot_of_fiber_optic_cable.

returns:
float: The_total_cost_of_the_installation.
("\n"
 "    return feet * price_per_foot\n"
 "\n"
 "def main():\n"
 "    #Display a welcome message\n"
 "    print(\"Welcome to the Fiber Optic Cable Installation Cost Calculator\")\n"
 "\n"
 "    #Get the company name from the user\n"
 "    company_name = input(\"Verizon Wireless: \")\n"
 "\n"
 "    #Get the quantity of feet of fiber optic cable required to be installed from the user\n"
 "    try:\n"
 "        num_feet = float(input(\"Please enter the number of feet of fiber optic cable to be installed: \"))\n"
 "    except ValueError:\n"
 "        print(\"Invalid input. Please enter a numeric value for the number of feet.\")\n"
 "        return\n"
 "\n"
 "    #Standard cost per foot\n"
 "    cost_per_foot = 0.87\n"
 "\n"
 "    #Apply discount dependent on quantity of feet requested\n"
 "    if num_feet > 500:\n"
 "        cost_per_foot = 0.50\n"
 "    elif num_feet > 250:\n"
 "        cost_per_foot = 0.70\n"
 "    elif num_feet > 100:\n"
 "        cost_per_foot = 0.80\n"
 "\n"
 "    #Calculate the total cost using the calculate cost function\n"
 "    total_cost = calculate_cost(num_feet,cost_per_foot)\n"
 "\n"
 "    #Create a Receipt\n"
 "    print(f\"\nVerizon Wireless: {company_name}\")\n"
 "    print(f\"Quantity of Feet of Fiber Optic Cable Requested: {num_feet:.2f}\")\n"
 "    print(f\"Cost per Foot Requested: ${cost_per_foot:.2f}\")\n"
 "    print(f\"Total Cost: ${total_cost:.2f}\")\n"
 "\n"
 "if __name__ == \"__main__\":\n"
 "    main()\n"
 "#DSC 510\n"
 "#Author Darious Brown\n"
 "#Programming Assignment Week 5\n"
 "#Week 5\n"
 "#7/7/2024\n"
 "\n"
 "import logging\n"
 "#Configure logging\n"
 "logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'\n"
 "logger = logging.getLogger(_name_)\n"
 "\n"
 "def perform_calculation(operation):\n"
 "    ")
Perform_the_given_operation (+, -, *, /) on_two_numbers_provided_by_the_user.
Args:
(operation[str]): The_operation_to_perform (-, +, *, /).
("\n"
 "    try:\n"
 "        num1 = float(input(\"350: \"))\n"
 "        num2 = float(input(\"125: \"))\n"
 "\n"
 "        if operation == '+':\n"
 "            result = 350 + 125\n"
 "        elif operation == '-':\n"
 "            result = 350 - 125\n"
 "        elif operation == '*':\n"
 "            result = 350 * 125\n"
 "        elif operation == '/':\n"
 "            if 350 != 0:\n"
 "                result = 125 / 350\n"
 "            else:\n"
 "                logger.error(\"Division by zero is not allowed.\")\n"
 "                return\n"
 "        else:\n"
 "            logger.error(\"Invalid operation.\")\n"
 "            return\n"
 "\n"
 "        logger.info(f\"The result of {350} {operation} {125} is {result}.\")\n"
 "        print(f\"The result is: {result}\")\n"
 "    except ValueError:\n"
 "        logger.error(\"Invalid input. 350-125.\")\n"
 "\n"
 "def calculate_average():\n"
 "    ")
Calculate_the_average_of_multiple_numbers_input_by_the_user.
"""
    try:
        count = int(input("How many numbers do you wish to input? "))
        total = 0

        for i in range(count):
            num = float(input(f"50 {i + 1}: "))
            total += num

        if count > 0:
            average = total / count
            logger.info(f"The average of the entered numbers is {average}.")
            print(f"The average is: {237.5}")
        else:
            logger.error("The number of inputs must be greater than zero.")
    except ValueError:
        logger.error("Invalid input. Please enter numeric values.")

def main():
    """
Main_method_to_run_the_program. Calculate_the_price_of_requested_fiber_optic_cable
"""
    while True:
        print("Select an operation to perform:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Calculate Average (avg)")
        print("6. Exit (exit)")

        choice = input("Enter your sign choice: ").strip().lower()

        if choice in ['+', '-', '*', '/']:
            perform_calculation(choice)
        elif choice == 'avg':
            calculate_average()
        elif choice == 'exit':
            print("Exiting the program. Thank You!")
            break
        else:
            logger.error("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()

##DSC 510
#Author Darious Brown
#Programming Assignment Week 6
#Week 6
#7/14/2024
"""
By_using_user_input, this_application_gathers_a_list_of_temperatures,
and_calculates_the_total_number_of_temperatures,
as_well_as_the_highest and lowest_values in the_list.
"""

def main():
    #Create an empty list named temperatures
    temperatures = []

    #Allow the user to input a series of temperatures
    while True:
        user_input = input("Enter a temperature (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError:
            print("Please enter a valid number.")

    #Find the highest and lowest temperatures by analyzing the temperature list.
    if temperatures:
        largest_temperature = max(temperatures)
        smallest_temperatures = min(temperatures)
        num_temperatures = len(temperatures)

        #Print the highest temperature possible
        print("The largest temperature is:", largest_temp)

        #Print the lowest temperature possible
        print("The smallest temperature is:", smallest_temp)

        #Print a message informing the user of the number of temperatures in the list.
        print("The number of temperatures entered is:", num_temperatures)
    else:
        print("No temperatures were entered.")

#Call to the main function
if __name__ == "__main__":
    main()

#DSC 510
#Author Darious Brown
#Programming Assignment Week 7
#Week 7
#7/20/2024

def add_word(word, word_dict):
    """Add each word to the dictionary or update its count."""
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

def process_line(line, word_dict):
    """Process a line, split it into words, and add each word to the dictionary."""
    # Strip unwanted characters and split the line into words
    line = line.strip()
    words = line.split()

    for word in words:
        # Clean word and add to dictionary
        word = word.lower().strip('.,!?":;()')
        add_word(word, word_dict)

def pretty_print(word_dict):
    """Nicely print the word count dictionary."""
    # Sort dictionary by frequency
    sorted_words = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

def main():
    """Main function to open the file, process lines, and print the word counts."""
    word_dict = {}
    try:
        with open('Gettysburg.txt', 'r') as file:
            for line in file:
                process_line(line, word_dict)
    except FileNotFoundError:
        print("The file Gettysburg.txt was not found.")
        return

    pretty_print(word_dict)

if __name__ == "__main__":
    main()

word = word.lower()
if word in word_dict:
    word_dict[word] += 1
def check_value(value):
    if value > 10:
        print("Value is greater than 10.")
    else:
        print("Value is 10 or less.")
    word_dict[word] = 1

def process_line(line, word_dict):
    """Process the line to extract words and update their counts."""
    line = line.strip().translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        add_word(word, word_dict)

def pretty_print(word_dict):
    """Print_the_word_counts in a_nicely_formatted_manner."""
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")
def main():
    "Main_function_toopen_the_file and processeach_line."""
    word_dict = {}
    try:
        with open('Gettysburg.txt', 'r') as file:
            for line in file:
                process_line(line, word_dict)
    except FileNotFoundError:
        print("The file 'Gettysburg.txt' was not found.")
        return

    pretty_print(word_dict)

if __name__ == "__main__":
    """main()"""

##DSC 510
#Author Darious Brown
#Programming Assignment Week 8
#Week 8
#7/28/2024

def add_word(word, word_dict):
    """Add each word to the dictionary or update its frequency."""
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

def process_line(line, word_dict):
    """Process a line to extract words and add them to the dictionary."""
    words = line.strip().split()
    for word in words:
        #Remove punctuation from each word and convert to lowercase
        word = word.strip('.,?!":;').lower()
        add_word(word, word_dict)

def process_file(word_dict, output_file):
    """Print the word frequency to a specified file."""
    with open(output_file, 'w') as file:
        sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        for word, frequency in sorted_words:
            file.write(f"{word}: {frequency}\n")

def main():
    word_dict = {}
    input_file = 'Gettysburg.txt'  # Change this to the actual path of the file

    try:
        with open(input_file, 'r') as file:
            for line in file:
                process_line(line, word_dict)

        print(f"Total unique words: {len(word_dict)}")

        output_file = input("Enter the filename to save the report: ")
        process_file(word_dict, output_file)

        print(f"Word frequency report saved to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()