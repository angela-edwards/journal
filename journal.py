import os

def main():
    while True:
        print_menu()
        choice = input('please enter your choice: ')

        if choice == '1':
            if not os.path.exists('passcode.txt'):
                create_passcode()
            new_entry()

        elif choice == '2':
            mental_health()

        elif choice == '3':
            motivation()

        elif choice == '4':
            previous_entries()
        
        elif choice == '5':
            forgot_passcode()
        
        elif choice == '6':
            print('have a great day <3')
            break

        else:
            print('invalid choice. please try again.')

def print_menu():
    print('------------------------')
    print('welcome to your journal!\nwhat would you like to do?')
    print('   1. Journal entry')
    print('   2. Mental health log')
    print('   3. Motivation')
    print('   4. See previous entries')
    print('   5. Forgot passcode')
    print('   6. Exit')

def create_passcode():
    passcode = input('please create a passcode: ')
    with open('passcode.txt', 'w') as file:
        file.write(passcode)
    print('\nwrite it down somewhere!')
    yes_no = input('\ndid you write it down (y/n)? ')
    if yes_no == 'y':
        print("yay!! don't lose it!")
    else:
        print(":( please write it down...")

def get_passcode():
    if os.path.exists('passcode.txt'):
        with open('passcode.txt', 'r') as file:
            return file.read().strip()
    return None

def verify_passcode():
    saved_passcode = get_passcode()
    if not saved_passcode:
        print('no passcode found. please create one!')
        create_passcode()
        return True
    entered_passcode = input('\nplease enter your passcode: ')
    if entered_passcode == saved_passcode:
        print('thank you!')
        return True
    else:
        print("incorrect passcode! if you've forgotten it, please return to the start menu.")
        return False

def new_entry():
    create_passcode()
    print('---------------------------------------')
    print("feel free to write anything you'd like.\nthis journal is top secret!\n")
    date = input('please provide the date (dd/mm/yyyy): ')
    entry = input('write away!\n')

    with open('journal.txt', 'a') as file:
        file.write(date + '\n')
        file.write(entry + '\n')
    
    print('\nyour entry has been added!')

def create_file():
    with open('journal.txt', 'w') as file:
        new_entry()

def mental_health():
    print('-----------------------------------------')
    print('would you like to log an emotion or mood?')
    print("**emotion: how you feel right now\n**mood: how you've felt overall today")
    choice = input('\nplease enter here: ')

    if choice == 'emotion':
        date = input('\nplease provide the date (dd/mm/yyyy): ')
        scale = input('1. on a scale from 1-10, how are you feeling in this moment? ')
        description = input('2. what words best describe this feeling? ')
        cause = input("3. why do you feel this way? what's on you're mind? ")
        concerns = input("4. any other specific concerns or feelings? ")

        with open('mental_logs.txt', 'a') as file:
            file.write(date + "\n")
            file.write("how i'm feeling right now: " + scale)
            file.write("\nwords describing this feeling:\n" + description)
            file.write("\n" + cause)
            if concerns == 'no' or concerns == 'nothing':
                file.write('\n' + 'end of entry')
            else:
                file.write( "\n" + concerns)

    elif choice == 'mood':
        date = input('\nplease provide the date (dd/mm/yyyy): ')
        scale = input('1. on a scale from 1-10, how have you felt today? ')
        description = input('2. what words best describe this feeling? ')
        cause = input('3. what occurrences happened today to provoke this feeling? ')
        concerns = input("4. anything else on your mind? ")

    with open('mental_logs.txt', 'a') as file:
        file.write(date + "\n")
        file.write("how i've felt today: " + scale)
        file.write("\nwords describing this feeling:\n" + description)
        file.write("\n" + cause)
        if concerns == 'no' or concerns == 'nothing':
            file.write('\n' + 'end of entry')
        else:
            file.write( "\n" + concerns)
    
    print("\nyour mental health has been logged! you can access the logs at the start menu.")
    print("\nif you've had a bad day today, i promise that things will get better.\njust keep on going and don't give up! <3")

def motivation():
    print('coming soon!')

def previous_entries():
    if not verify_passcode():
        return
    choice = input('\nwould you like to see past journal entries(1) or mental health logs(2)? ') 
    if choice == '1':
        try: 
            print('\nprevious journal entries: ')
            with open('journal.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("\nyou have no previous entries. come back once you've written one!")

    elif choice == '2':
        try: 
            print('\nprevious mental health logs: ')
            with open('mental_logs.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("\nyou have no mental health logs. come back once you've done one!")

def forgot_passcode():
    print("-------------------------------------------")
    print("looks like you forgot you're passcode, huh.")
    print("you should've written it down like i told you to, silly!")
    print("well, i guess i'll help you out. if you answer this question i'll tell you the passcode.")
    answer = input("\ndo you like pineapple on pizza (yes/no)? ")
    if answer == 'yes':
        print("disgusting. you don't get your passcode back.")
    elif answer == 'no':
        print('correct! here is your passcode: ')
        with open('passcode.txt', 'r') as file:
            print(file.read())
    else:
        print("trynna be funny? try again!\n")

main()