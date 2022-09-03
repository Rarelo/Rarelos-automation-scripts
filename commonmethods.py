### To contain common methods between both windows and linux code

def get_and_check_user_input(input_message,valid_inputs):
    '''Prompt the user with 'input_message' and check their
    input via the list 'valid_inputs' An empty 'valid_inputs' will accept all inputs (except blank which is exit)'''
    user_input = input(input_message)
    input_check_couner = 0
    if user_input == "":
        return None
    if len(valid_inputs) == 0:
        input_check_couner += 1
    for i in valid_inputs:
        if user_input == i:
            input_check_couner += 1
    if input_check_couner == 1:
        return user_input
    else:
        print("Error: Please enter a valid input")
        get_and_check_user_input(input_message,valid_inputs)

def get_user_confirmation(input_message):
    '''get user confiramation and output either a proceed (true) or kill signal'''
    user_response = get_and_check_user_input(input_message,['y','n'])
    if user_response == 'y':
        return True
    elif user_response == 'n':
        return None
    else: print('something has gone wrong with the get_user_confirmation method in commonmethods')

def choose_script(operating_system):
    if operating_system == 'linux':
        chosen_script = get_and_check_user_input( 
            "Choose Script: \n 1) Create Firefox Profile \n 2) Create Application Shortcut \n" 
        ,['1','2'])
        return chosen_script
    else:
        print("Windows support coming soon")

def get_operating_system(): 
    '''get user input for operating system they are on''' 
    os_input = get_and_check_user_input( 
    "Linux (L) or Windows (W): ",['L','l','W','w']) 
    #print(os_input) 
    if os_input == None: 
        #print("Exiting2") 
        return None 
    if os_input == 'L' or os_input == 'l': 
        return "linux" 
    elif os_input == 'W' or os_input == 'w': 
        print("Windows currently unimplemented") 
        return "windows" 
    else: 
        print('Error: Program error')

