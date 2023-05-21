'''
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.


'''

values = [3, 9, 12, 15]

# def same_by(characteristic, objects):
#     for i in range (len(objects)-1):
#         if characteristic(objects[i]) != characteristic(objects[i+1]): 
#             return False
#     return True    

def same_by(characteristic, objects):
    funObject = set(map(characteristic, objects)) 
    if len(funObject)>1:  return False
    return True    


if same_by(lambda x: x%3, values):
    print('same')
else: 
    print ('different')  