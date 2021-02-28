def num_translate(ru):

    for key in words:
        print(f'"{a}" переводится как "{words[ru]}" ')
        break
    # if a != key in words: - пока не получилось реализовать None нормально)
    #     return print(words.get('key', f' Слово {a} не содержиться в переводчике'))


a = input('Введите число от 0 до 10 ввиде слова:')

words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
    'zero': 'ноль'
}

num_translate(a)
# num_translate('one') - подумал что вводить число самому будет лучше)
# num_translate('two')
