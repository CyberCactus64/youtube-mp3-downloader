
from __future__ import unicode_literals
import youtube_dl # pip install --upgrade youtube_dl
from sys import exit

def main():
    options = {'format': 'bestaudio/best', 
            'postprocessors': [{'key': 'FFmpegExtractAudio', 
                                'preferredcodec': 'm4a',
                                'preferredquality': '192'}]}

    print("\nYOUTUBE MUSIC DOWNLOADER")
    print("\nBased on youtube_dl library --> https://yt-dl.org/")
    print("Code by Edoardo Fornasier")
    print("\n(Press CTRL-C to stop download)")

    count = 0
    errors = 0

    ydl = youtube_dl.YoutubeDL(options)

    with open('songs.txt', 'r') as songs:
        links = songs.readlines() # create a list that contains all the links
        for link in links: # iterate through the file lines
            print("\n-------------------------------------------------------------------------\n")
            print(f"DOWNLOADING LINK N. {count+1}")
            print("")
            try:
                ydl.download([link])
            except KeyboardInterrupt: # if CTRL-C close the script
                break
            except:
                print(f"Error while trying to download link n. {count+1}")
                errors += 1
                pass # go to the next file line

            count += 1 # add 1 to counter

    print("")
    print(f"{count - errors} links successfully downloaded :)")
    print(f"{errors} errors :(")
    exit() # sys.exit(), stop the script

if __name__ == "__main__":
    main()