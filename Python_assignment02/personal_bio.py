def q1_personal_bio():
    # Define student details in variables [cite: 37]
    name = "John Doe"
    age = 20
    course = "Python Programming"
    college = "ABC University"
    email = "john@example.com"
    
    # Create a visually appealing box format [cite: 38, 39]
    print("+" + "-"*35 + "+")
    print("|      STUDENT BIO CARD             |")
    print("+" + "-"*35 + "+")
    print(f"| Name    : {name:<23} |")
    print(f"| Age     : {age:<23} |")
    print(f"| Course  : {course:<23} |")
    print(f"| College : {college:<23} |")
    print(f"| Email   : {email:<23} |")
    print("+" + "-"*35 + "+")