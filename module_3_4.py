#Задача "Однокоренные":
#
#Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.



#Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.



#Пункты задачи:

#Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
#Создайте внутри функции пустой список same_words, который пополнится нужными словами.
#При помощи цикла for переберите предполагаемо подходящие слова.
#Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
#После цикла верните образованный функцией список same_words.
#Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
#Пример результата выполнения программы:




def single_root_words(root_world, *other_words):
    same_words = []
    for i in other_words:
        if root_world.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_world.lower():
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

