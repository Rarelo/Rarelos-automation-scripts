
def determine_website_and_replace(link):
    '''top level function to find the website and replace the link'''
    for i in url_database:
        #print(i)
        website = is_the_website_right(link,i)
        if website != -1:
            return link.replace(i[0],i[1])

def is_the_website_right(link,website_to_check):
    findnum = link.find(website_to_check[0])
    return findnum

def remove_www(new_link):
    '''prevent firefox issues with https://wwww... links'''
    return new_link.replace('www.','')

###update this list with a new list containing website url and what
###to replace with
url_database = [['fxtwitter.com','nitter.net'],
['youtube.com','vid.puffyan.us'],
['twitter.com','nitter.net'],['youtu.be','vid.puffyan.us']]

link = input("Enter Link: ")
new_link = determine_website_and_replace(link)
new_link = remove_www(new_link)
print(new_link)
link = input("Process Done. Press Any Key to Exit")
