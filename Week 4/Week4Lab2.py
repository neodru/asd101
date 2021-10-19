
game = [ 'Duck', 'Duck','Duck','Duck', 'GOOSE!', 'Duck','Duck']

response = ['No','No','No','No','RUN!','No','No']

for x in game:
    for y in response:
        print(x,y)
    if x == 'GOOSE!':
        break

 duck = "Duck"
 goose = "GOOSE!"
 not_it = "No"
 tag = "RUN!"

x =5
while x<= 20:
    print(duck + " " + not_it)
    if x ==15:
        print(goose + " " + tag)
        break
x += 1

