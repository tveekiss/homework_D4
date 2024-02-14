from django import template

register = template.Library()

file_path =r'E:\Python\Projects\django-projects\homework D2.9\NewsPortal\news\templatetags\filter_profanity_russian_cached.txt'

@register.filter()
def censor(text):
    with open(file_path, 'r', encoding='utf-8') as file:
        bad_words = file.read().splitlines()
    words = text.split()
    for i, word in enumerate(words):
        check_word = word.lower()
        if check_word in bad_words:
            words[i] = word[0] + '*' * (len(word) - 1)
    return ' '.join(words)
