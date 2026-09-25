#Grade Calculator

#Defining the required function - getting a percentage
def percentage(ice, midterm, final, orientation, quizes, labs, homework):
    ice_p = float((ice/500))
    midterm_p = float((midterm/120))
    final_p = float((final/100))
    orientation_p = float((orientation/40))
    quizes_p = float((quizes/60))
    labs_p = float((labs/900))
    homework_p = float((homework/400))

    total_percentage = (0.14 * ice_p) + (0.20 * midterm_p) + (0.2 * final_p) + (0.01 *  orientation_p) + (0.1 * quizes_p) + (0.25 * labs_p) + (0.1 * homework_p)
    return total_percentage

def lettergrade(total_percentage):
    if total_percentage >= 0.85:
        l = 'A'
        return l
    elif total_percentage >= 0.70: 
        l = 'B'
        return l
    elif total_percentage >= 0.60: 
        l = 'C'
        return l
    elif total_percentage >= 0.50: 
        l = 'D'
        return l   
    else:
        l = 'F'
        return l

print('Welcome to the Grade Calculator')

ice = int(input('Out of 500, How many points did you get for the ICES: '))
midterm_1 = int(input('How many points did you get on the first midterm: '))
midterm_2 = int(input('How many points did you get on the second midterm: '))
midterm_t = midterm_1 + midterm_2
final = int(input('How many points did you get on the final: '))
orientation = int(input('How many points did you get on the Orientation Quiz: '))
Quizes = int(input('What was your total score, out of 60 for all 4 quizzes?: '))
Labs = int(input('How many points did you get from lab (Out of 900): '))
Homework = int(input('How many points did you get from all your homeworks?: '))

total_percentage = percentage(ice, midterm_t, final, orientation, Quizes, Labs, Homework)
letter_grade = lettergrade(total_percentage)

percent_n = 100 * total_percentage

print('Your final grade was a',percent_n ,'%, You got a', letter_grade, 'in the class!')
