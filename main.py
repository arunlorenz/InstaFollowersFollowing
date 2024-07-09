import instaloader
from instaloader.exceptions import TwoFactorAuthRequiredException
import os

def get_followers_following(username, password, target_username):
    L = instaloader.Instaloader()
    session_file = f"{username}.session"
    if os.path.exists(session_file):                        #check for existing sessions
        L.load_session_from_file(username, session_file)
    else:
        try:
            L.login(username, password)
            L.save_session_to_file(session_file)
        except TwoFactorAuthRequiredException:
            print("Two-factor authentication required.")
            two_factor_code = input("Enter the 2FA code: ")
            L.context.two_factor_login(two_factor_code)
            L.save_session_to_file(session_file)
    
    profile = instaloader.Profile.from_username(L.context, target_username)

    followers = set(follower.username for follower in profile.get_followers())      #gather the namelist of users
    following = set(followee.username for followee in profile.get_followees())

    return followers, following

def get_non_followers(followers, following):
    non_followers = following - followers
    return non_followers

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    target_username = input("Enter the target username: ")
    
    followers, following = get_followers_following(username, password, target_username)
    non_followers = get_non_followers(followers, following)
    
    print("Users who don't follow back:")
    for user in non_followers:
        print(user)

if __name__ == "__main__":
    main()
