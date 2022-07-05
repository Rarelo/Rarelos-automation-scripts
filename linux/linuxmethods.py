import os
import subprocess
import commonmethods
import directories

### To contain linux methods to be run my main.py

## script level functions
def create_firefox_profile():
    '''top firefox profile script that handles the entire create firefox profile process'''
    directory = linux_get_application_folder_directory() 
    linux_folder_directory = directory+"/linux"
    profile_name = get_name()
    if profile_name == None:
        print("Exiting...")
        return None
    mozilla_create_firefox_profile(profile_name)
    create_shortcut(profile_name)

def create_linux_shortcut():
    app_name = get_name()
    app_directory = get_other_app_directory()
    create_shortcut(app_name,app_directory)

## firefox profiles 
def mozilla_create_firefox_profile(profile_name):
    '''take input for a profile name and create new customized (same as default profile) profile'''
    directory = linux_get_application_folder_directory()
    #for subprocess: string is command, other strings arguments for string 1
    subprocess.run(["firefox", "-CreateProfile", str(profile_name)])
    #run create-profile.sh w/ argument of profile-name to
    #settings from default profile to new profile
    subprocess.run([directory+'/create-profile.sh',profile_name])    

def get_name(): 
    '''get desired profile name from user''' 
    profile_name = commonmethods.get_and_check_user_input( 
    "Enter Profile Name:",[]) 
    if profile_name == None: 
        #print("Exiting2") 
        return None 
    return profile_name 

## shortcut creation
def create_shortcut(name_without_file_extension):
    '''takes a name and creates a shortcut. NOTE: will need to add functionality to change desired app shortcut directory'''
    #copy and fix the .desktop shortcut temprarily in the program folder
    shortcut_name = str(name_without_file_extension)+".desktop"
    create_dot_desktop_file(name_without_file_extension,shortcut_name)
    #copy the .desktop to the /usr/share/applications/
    subprocess.run(["sudo","cp",str(shortcut_name),
    "/usr/share/applications/"+str(shortcut_name)])
    #remove the old .desktop file from the program directory
    subprocess.run(["rm",str(shortcut_name)])

def get_other_app_directory():
    app_directory = commonmethods.get_and_check_user_input(
    "Enter the exact file path to the desrired application:",[])
    return app_directory

def create_dot_desktop_file(profile_name,shortcut_name): 
    '''fills in profile_name with the user's profile name and outputs to a new .desktop file''' 
    replacements = {'profile_name':str(profile_name)} 
 
    with open(directories.LINUX+'/firefox.desktop') as infile, open(str(shortcut_name), 'w') as outfile: 
        for line in infile: 
            for src, target in replacements.items(): 
                line = line.replace(src, target) 
            outfile.write(line)

## base functions
def linux_get_application_folder_directory():
    return (os.getcwd()+"/linux")

