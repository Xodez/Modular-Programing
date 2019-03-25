# #
# from reading_from_user import read_nonempty_alphabetical_string
# from reading_from_user import read_integer
#
# def get_score(name_team):
#     goals = read_integer("enter goals of " + name_team + " >>>> :")
#     points = read_integer("enter points of " + name_team + " >>>> :")
#     return goals, points
#
# def calculate_total(goals, points):
#     total = points + (goals * 3)
#     return total
#
# def determine_winning_team(name_team1, total1, name_team2, total2):
#     if total1 > total2:
#         winning_team = name_team1
#     elif total1 < total2:
#         winning_team = name_team2
#     else:
#         winning_team = "Draw"
#     return winning_team
#
# def display_result(winning_team):
#     if winning_team == "Draw":
#         print("The teams drew and there is no winner.")
#     else:
#         print("The winner is " + winning_team)
#
# def main():
#     name_team1 = read_nonempty_alphabetical_string("Name Team #1 >>> ")
#     goals1, points1 = get_score(name_team1)
#     total1 = calculate_total(goals1, points1)
#     name_team2 = read_nonempty_alphabetical_string("Name Team #2 >>> ")
#     goals2, points2 = get_score(name_team2)
#     total2 = calculate_total(goals2, points2)
#     winning_team = determine_winning_team(name_team1, total1, name_team2, total2)
#     display_result(winning_team)
#
# main()
# #
#
from reading_from_user import read_nonempty_alphabetical_string
from reading_from_user import read_integer

def read_house():
    print("\t"+"1: Slytherin"+"\n"+"\t"+"2: Hufflepuff"+"\n"+"\t"+"3: Ravenclaw"+"\n"+"\t"+"Gryffindor")
    house = read_integer("Which House >>>> :")
    return house

def get_house_details(house):
    if house == 1:
        house_name = "Slytherin"
        house_ghost = "The Bloody Baron"
    elif house == 2:
        house_name = "Hufflepuff"
        house_ghost = "The Fat Friar"
    elif house == 3:
        house_name = "Ravenclaw"
        house_ghost = "The Grey Lady"
    elif house == 4:
        house_name ="Gryffindor"
        house_ghost = "Nearly Headless Nick"
    return house_name,house_ghost

def print_details(student_name, house_name, house_ghost):
    print(student_name+"belongs to "+house_name+" which is haunted by "+house_ghost)

def main():
    student_name = read_nonempty_alphabetical_string("Student's name >>> ")
    house = read_house()# returns 1, 2, 3 or 4
    house_name, house_ghost = get_house_details(house) # returns the house's name
    print_details(student_name, house_name, house_ghost)

main()
#