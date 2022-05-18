import os
import instaloader

def picture_download(username):
    parser = instaloader.Instaloader()
    """ Change directory to download folder """
    os.chdir(os.path.join(os.path.expanduser('~'), 'Downloads'))

    """ create costum folder dor ig Dwonloads """
    if os.path.isdir("Instagram Downloads"):
        os.chdir("Instagram Dwonloads")
        """ Download the data """
        return parser.download_profile(username, profile_pic_only=True)
    else:
        """ make instagram downloads folder is not exists """
        os.mkdir("Instagram Downloads")
        os.chdir("Instagram Dwonloads")
        """ Dwonload the data """
        return parser.download_profile(username, profile_pic_only=True)

if __name__=="__main__":
    user = input("enter Instagram account: ")
    picture_download(user)
