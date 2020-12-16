import main

print('''
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
                                                WELCOME TO YOUTER

[1] Download from links in a text file
[2] Download by searching using youtube API
[3] Download by using a direct link

''')

option = int(input('Select an option: '))
if option == 1:
    print("""
    [1] Download Audio
    [2] Download Video""")
    
    opt = int(input("Select an option: "))
    if opt == 1:
        f_path = input("Enter the path of the file with links: ")
        destination = input("Enter the path where you want to save: ")
        main.line_download_music(f_path, destination)
    elif opt == 2:
      f_path = input("Enter the path of the file with links: ")
      destination = input("Enter the path where you want to save: ")
      main.line_download_videos(f_path, destination)
    else:
        print("Enter a valid number!!")
elif option == 2:
    print("""
    [1] Download Audio
    [2] Download Video""")
    opt = int(input("Select an option: "))
    if opt == 1:
        search = input("Enter the video you want to search for: ")
        print("Copy the video Id of the video you would like to download")
        main.youtquery(search)
        videoid = input("Enter the video id: ")
        destination = input("Enter the path where you want to save: ")
        main.download_musicid(videoid, destination)
    elif opt == 2:
        search = input("Enter the video you want to search for: ")
        print("Copy the video Id of the video you would like to download")
        main.youtquery(search)
        videoid = input("Enter the video id: ")
        destination = input("Enter the path where you want to save: ")
        main.download_videosid(videoid, destination)
    else:
        print("Enter a valid number!!")
elif option == 3:
    print("""
    [1] Download Audio
    [2] Download Video""")
    opt = int(input("Select an option: "))
    if opt == 1:
        video_link = input("Enter the link: ")
        destination = input("Enter the path where you want to save: ")
        main.download_musiclink(video_link, destination)
    elif opt == 2:
        video_link = input("Enter the link: ")
        destination = input("Enter the path where you want to save: ")
        main.download_videolink(video_link, destination)
    else:
        print("Enter a valid number!!")
else:
    print("Enter a valid number!!")



