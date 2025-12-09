import math
# Can you get an A in this course?

def pre_final_grade_calculator():
    assignment_weight = 0.56
    midterm_weight = 0.06
    final_weight = 0.3
    scholatic_conduct_weight = 0.08

    current_assignment_grade = ( float(input("Enter your current assignment % (0-100): ")) ) / 100
    midterm_grade = ( float(input("Enter your midterm exam % (0-100): ")) ) / 100
    assumed_final_grade = ( float(input("Guess your final exam % (0-100) or enter '0' to see lowest you need: ")) ) / 100
    scholatic_conduct_grade = input("Did you breach scholastic conduct? (Y/N): ").upper()

    if scholatic_conduct_grade.upper() == 'Y':
        scholatic_conduct_grade = 0
    else:
        scholatic_conduct_grade = scholatic_conduct_weight

    scaled_assg_grade = calc_scaled_assg_grade(current_assignment_grade, assumed_final_grade)
    # print(f"Scaled Assignment Grade: {scaled_assg_grade * 100:.2f}%")

    final_grade = (scaled_assg_grade * assignment_weight) + (midterm_grade * midterm_weight) + (assumed_final_grade * final_weight) + scholatic_conduct_grade
    # print(f"Final grade = ({scaled_assg_grade} * {assignment_weight}) + ({midterm_grade} * {midterm_weight}) + ({assumed_final_grade} * {final_weight}) + {scholatic_conduct_grade}")

    if final_grade >= .95:
        print(f"You can get an A in this course! Your projected grade is: {final_grade  * 100:.2f}%")
    else:
        if assumed_final_grade != 0:
            print(f"You cannot get an A in this course. Your projected grade is: {final_grade  * 100:.2f}%")
        while final_grade < .95:
            assumed_final_grade += .001
            scaled_assg_grade = calc_scaled_assg_grade(current_assignment_grade, assumed_final_grade)
            final_grade = (scaled_assg_grade * assignment_weight) + (midterm_grade * midterm_weight) + (assumed_final_grade * final_weight) + scholatic_conduct_grade
            # print(f"Final grade = ({scaled_assg_grade} * {assignment_weight}) + ({midterm_grade} * {midterm_weight}) + ({assumed_final_grade} * {final_weight}) + {scholatic_conduct_grade}")
        print(f"You need at least a {assumed_final_grade * 100:.2f}% on the final exam to get an A in this course.")
        


def calc_scaled_assg_grade(assg_grade, final_grade):
    if final_grade <= 1 and final_grade >= .95:
        return 1 * assg_grade
    elif final_grade < .95 and final_grade >= .9:
        return .95 * assg_grade
    elif final_grade < .9 and final_grade >= .85:
        return .9 * assg_grade
    elif final_grade < .85 and final_grade >= .8:
        return .85 * assg_grade
    elif final_grade < .8 and final_grade >= .75:
        return .8 * assg_grade
    elif final_grade < .75 and final_grade >= .7:
        return .75 * assg_grade
    elif final_grade < .7 and final_grade >= .65:
        return .7 * assg_grade
    elif final_grade < .65 and final_grade >= .6:
        return .65 * assg_grade
    elif final_grade < .6 and final_grade >= .55:
        return .6 * assg_grade
    elif final_grade < .55 and final_grade >= .5:
        return .55 * assg_grade    
    else:
        return 0
    


pre_final_grade_calculator()