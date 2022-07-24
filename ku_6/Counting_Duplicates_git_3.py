# Подсчитайте количество дубликатов
# Напишите функцию, которая будет возвращать количество различных
# буквенных символов и цифр, не зависящих от регистра, которые встречаются
# во входной строке более одного раза. Можно предположить, что входная строка
# содержит только буквы (как прописные, так и строчные) и числовые цифры.
#
# Пример
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "неделимость" -> 1 # 'i' occurs six times
# "неделимость" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


def duplicate_count(text):
    alf = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = 0 # количество дубликатов
    for a in alf: # перебор по алфовиту
        y = 0 # количество одной буквы
        for t in text: # перебор по вводу
            if t.title() == a:
                y += 1
        if y > 1:
            x += 1
    return x


print(duplicate_count("")) # 0
print(duplicate_count("abcde")) # 0
print(duplicate_count("abcdeaa")) # 1
print(duplicate_count("abcdeaB")) # 2
print(duplicate_count("Indivisibilities")) # 2
print(duplicate_count("qMZubBpDprsIw9DE4MVBqBeRXXFSj3I3BWVG0Wri3pdYbCQUpEGq")) # 15

print(len('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


def duplicate_count(text):
    seen = set() # set уникальные элементы
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

