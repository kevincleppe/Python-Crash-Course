def music(artist, album):
    project=f"{artist} {album}"
    return project.title()
diskography=[]
while True:
    

    art=input("\nName an artist, or enter q to exit: ")
    if art =='q':
        break
    mus=input("\nName one of their albums, or enter q to exit: ")
    if mus == 'q':
        break
    get_music = music(art, mus)
    diskography.append(get_music)
    print(f"{get_music}")
    print(f"\n{diskography}")
