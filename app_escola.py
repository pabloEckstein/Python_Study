import os

students = [{'name':'Pablo', 'age':'30', 'email':'pablo@gmail.com', 'status':False},
          {'name':'Eric', 'age':'25', 'email':'eric@gmail.com', 'status':True},
          {'name':'Angel', 'age':'20', 'email':'angel@gmail.com', 'status':False},
          {'name':'Patrick', 'age':'16', 'email':'patrick@gmail.com', 'status':True}
          ]
def show_program_name():
    print('APP__SCHOOL')

def show_options():
    print('1. Include new student.')
    print('2. List all students.')
    print('3. Change status.')
    print('4. Quit')

def quit_app():
    show_current_option('Quit App')

def back_to_main_menu():
    input('\nType any button to back to menu: ')
    main()

def invalid_option():
    print('Invalid Option!\n')
    back_to_main_menu()

def show_current_option(text):
    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def include_new_student():
    show_current_option('Include New Students')
    student_name = input('Students Name: ')
    student_age = input('Students Age: ')
    student_email = input('Students Email: ')
    student_info = {'name': student_name, 'age': student_age, 'email': student_email, 'status': 'default'}
    students.append(student_info)
    back_to_main_menu()

def list_all_students():
    show_current_option('Listing Students')
    print(f'{'Name'.ljust(22)} | {'Age'.ljust(20)} | {'Email'.ljust(20)} | Status')
    for student in students:
        student_name = student['name']
        student_age = student['age']
        student_email = student['email']
        student_status = 'Approved' if student['status'] else 'Repproved'
        print(f'- {student_name.ljust(20)} | {student_age.ljust(20)} | {student_email.ljust(20)} | {student_status}')
    back_to_main_menu()

def change_status():
    show_current_option('Changing Status')
    student_name = input('Type de student name: ')
    student_is_found = False
    for student in students:
        if student_name == student['name']:
            student_is_found = True
            message = f'The student {student_name} has been activated with success' if student['status'] else f'The student {student_name} has been unactivated with success.'
            print (message)
    if not student_is_found:
        print('Student not found.')
    back_to_main_menu()

def choose_options():
    try:
        option = int(input('Choose one option: '))
        if option == 1:
            include_new_student()
        elif option == 2:
            list_all_students()
        elif option == 3:
            change_status()
        elif option == 4:
            quit_app()
        else:
            invalid_option()
    except:
        invalid_option()


def main():
    os.system('cls')
    show_program_name()
    show_options()
    choose_options()

if __name__ == '__main__':
    main()