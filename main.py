import subprocess

#firefox -CreateProfile {profileName}

##needs to do linux and maybe one day windows
#enter profile name X
#create profile X
#copy profile settings into new profile from default X
#create shortcut

def get_operating_system():
    '''get user input for operating system they are on'''
    os_input = input("Linux (L) or Windows (W): ")
    if os_input == 'L' or os_input == 'l':
        return "linux"
    elif os_input == 'W' or os_input == 'w':
        print("Windows currently unimplemented")
        return "windows"
    else:
        print("Error: Please enter a valid input")
        get_operating_system()

def get_profile_name():
    '''get desired profile name from user'''
    profile_name = input("Enter Profile Name: ")
    return profile_name

def fix_dot_desktop_file(profile_name,shortcut_name):
    replacements = {'profile_name':str(profile_name)}

    with open('firefox.desktop') as infile, open(str(shortcut_name), 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

print("")
os = get_operating_system()
profile_name = get_profile_name()

if os == 'linux':
    #string 1: command, other strings arguments for string 1
    subprocess.run(["firefox", "-CreateProfile", str(profile_name)])
    #run create-profile.sh w/ argument of profile-name
    subprocess.run(['./create-profile.sh',profile_name])
    #copy and fix the .desktop shortcut temprarily in the program folder
    shortcut_name = str(profile_name)+".desktop"
    fix_dot_desktop_file(profile_name,shortcut_name)
    #copy the .desktop to the /usr/share/applications/
    subprocess.run(["sudo","cp",str(shortcut_name),
    "/usr/share/applications/"+str(shortcut_name)])
    #remove the old .desktop file from the program directory
    subprocess.run(["rm",str(shortcut_name)])
