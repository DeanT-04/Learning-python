def human_data():
    # Prompt user for their name and capitalize the first letter
    name = input("Enter your name: ").capitalize()
    # Prompt user for their age and convert to integer
    age = int(input("Enter your age: "))
    # Prompt user for their height and convert to float
    height = float(input("Enter your height:"))
    # Prompt user for their gender and capitalize the first letter
    gender = input("Enter your gender: ").capitalize()
    # Prompt user if they are a student and capitalize the first letter of the response
    is_student = input("Are you a student? (True/False): ").capitalize()
    
    # Print out the user's data
    print(f"Name: {name}\nAge: {age}\nHeight: {height}\nGender: {gender}\nIs Student: {is_student}")

# Call the function to collect and display human data
human_data()