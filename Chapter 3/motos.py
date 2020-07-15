motos= ['honda', 'yamaha', 'suzuki']
print(motos)

motos[0]='ducati'
print(motos)
motos.append('toyota')
print(motos)
print(motos[0].title())
print(motos)
print("The full list is ", motos)
pop_motos=motos.pop()
print("The last item in the list is ", motos.pop())
print("The popped item is ", pop_motos)
print("Hey this is a test", pop_motos)
pricey='ducati'
print(motos)
motos.remove(pricey)
print(motos)