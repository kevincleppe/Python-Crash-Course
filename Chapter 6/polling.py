#what people registered as
poll={
    'kevin':'repub',
    'brandon':'dem',
    'charlie':'liber',
    'carlos':'green',
}
#this will loop through above dict and print who registered and as what
for key,value in poll.items():
    print(f"{key} is registered as a {value}")
#people that we are not sure if they are voted or not
others=['kevin','hideo', 'steve', 'carlos']

#this will loop through others array, comapre i in it to the poll array. 
#If it matches, it will say you have already taken the poll
#if it doesn't it will same you have not taken it yet
for i in others:
    if i in poll.keys():
        print(f"{i.title()} you have already taken the poll!")
    else:
        print(f"{i.title()} you have not taken  ")
        

