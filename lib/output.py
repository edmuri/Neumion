

def start():
    print("*"*39)
    print("*{0}{1}{0}*".format(
                            " "*10,
                            "Beginning Neumion"))
    print("*"*39)

def spotify():
    print("[-] Fetching songs from Spotify")
    print("[-] Please hold..this may take a minute..")

def spotify_complete():
    print("[-] Fetching songs from Spotify finished")

def youtube():
    print("[-] Fetching songs from Youtube")
    print("[-] Please hold..this may take a minute..")

def youtube_complete():
    print("[-] Fetching songs from Youtube completed")

def analysis():
    print("[-] Beginning song analysis..")
    print("[-] This may take a while to be thorough...")
    print("[-] Please hold")

def error(e):
    print("[!] Error Caught: " + str(e))
    print("[!] Exiting Neumion...")