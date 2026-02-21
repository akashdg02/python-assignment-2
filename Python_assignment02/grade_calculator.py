def q6_grade_calculator():
    marks = []
    for i in range(1, 6):
        # Gather marks and handle errors [cite: 122]
        m = float(input(f"Enter marks for subject {i}: "))
        marks.append(m)
        
    total = sum(marks) # [cite: 123]
    percentage = (total / 500) * 100 # [cite: 124]
    
    # Determine result based on pass criteria (>=40) [cite: 126]
    result = "Pass" if all(m >= 40 for m in marks) else "Fail"
    
    # Grade logic [cite: 127, 128, 129, 130, 131, 132, 133]
    if percentage >= 90: grade = "A+"
    elif percentage >= 80: grade = "A"
    elif percentage >= 70: grade = "B"
    elif percentage >= 60: grade = "C"
    elif percentage >= 50: grade = "D"
    else: grade = "F"
    
    print(f"Total Marks: {total}/500 | Percentage: {percentage}%")
    print(f"Grade: {grade} | Result: {result}")