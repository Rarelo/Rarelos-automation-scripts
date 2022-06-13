import subprocess
import os

#root level program code
def get_and_check_user_input(input_message,valid_inputs):
#   input string to prompt the user: input_message
#   valid_inputs is list of inputs which should be checked
#   an empty valid_inputs list will except all inputs (except "" = exit)
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

##linux specific code
def linux_get_application_directory():
    return (os.getcwd())

## firefox profiles
def get_profile_name():
    '''get desired profile name from user'''
    profile_name = get_and_check_user_input(
    "Enter Profile Name:",[])
    if profile_name == None:
        #print("Exiting2")
        return None
    return profile_name
def fix_dot_desktop_file(profile_name,shortcut_name):
    '''fills in profile_name with the user's profile name and outputs to new file'''
    replacements = {'profile_name':str(profile_name)}

    with open('firefox.desktop') as infile, open(str(shortcut_name), 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

def main():
    '''top level function code'''
    print("")
    ###operating system check + exit code
    operating_system = get_operating_system()
    if operating_system == None:
        print("Exiting...")
        return None
    ###profile name input + exit code
    profile_name = get_profile_name()
    if profile_name == None:
        print("Exiting...")
        return None

    print(profile_name)

    if operating_system == 'linux':
        directory = linux_get_application_directory()
        #string 1: command, other strings arguments for string 1
#        subprocess.run(["firefox", "-CreateProfile", str(profile_name)])
#        #run create-profile.sh w/ argument of profile-name
#        subprocess.run([directory+'/create-profile.sh',profile_name])
#        #copy and fix the .desktop shortcut temprarily in the program folder
#        shortcut_name = str(profile_name)+".desktop"
#        fix_dot_desktop_file(profile_name,shortcut_name)
#        #copy the .desktop to the /usr/share/applications/
#        subprocess.run(["sudo","cp",str(shortcut_name),
#        "/usr/share/applications/"+str(shortcut_name)])
#        #remove the old .desktop file from the program directory
#        subprocess.run(["rm",str(shortcut_name)])

## runs the code
main()
