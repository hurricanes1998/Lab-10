from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

holidays={"1":"День хрустящего огурчика","2":"День печеной картошечки","3":"День ухотрепальщиков"}
for key in holidays:
    print(key, " - ", holidays[key])

n = input("выберите праздник и напишите номер: ")
name = input("кого вы хотите поздравить: ")

if n in holidays:
    filename = "C://Users/Vlad/PycharmProjects/PythonProject2/lab10/postcards/"+n+".jpg"
    card = Image.open(filename)
    card_new = ImageDraw.Draw(card)
    font = ImageFont.truetype("arial.ttf", 50)
    message = name + ", поздравляю!"
    if n == "1":
        position = (300, 250)
        fill_color = (53, 50, 201)
    elif n == "2":
        position = (600, 250)
        fill_color = (200, 47, 103)
    else:
        position = (400, 850)
        fill_color = (0, 0, 0)
    card_new.text(position, message, font=font, stroke_width=2, fill=fill_color)
    card.show()
    card.save('C://Users/Vlad/PycharmProjects/PythonProject2/lab10//named/'+name+".png")
else:
    print("повод для развлечения не найден")