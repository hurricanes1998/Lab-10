from PIL import Image

holidays={"1":"День хрустящего огурчика","2":"День печеной картошечки","3":"День ухотрепальщиков"}
for key in holidays:
    print(key, " - ", holidays[key])

n = input("выберите праздник и напишите номер: ")

if n in holidays:
    filename = "C://Users/Vlad/PycharmProjects/PythonProject2/lab10/postcards/"+n+".jpg"
    card = Image.open(filename)
    card.show()
else:
    print("повод для развлечения не найден")