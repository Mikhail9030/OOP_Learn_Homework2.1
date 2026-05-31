import json
from collections import Counter
import string


def read_json(file_path, word_min_len=7, top_words_amt=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_words = []

    for item in data['rss']['channel']['items']:
        description = item.get('description', '')
        # Разбиваем по пробелам БЕЗ приведения к нижнему регистру
        words = description.split()

        for word in words:
            # Очищаем только от пунктуации, чтобы 'туристов.' превратилось в 'туристов'
            clean_word = word.strip(string.punctuation)

            # Проверяем длину очищенного слова
            if len(clean_word) >= word_min_len:
                all_words.append(clean_word)

    counter = Counter(all_words)
    # Возвращаем список слов в исходном регистре
    return [word for word, count in counter.most_common(top_words_amt)]


if __name__ == '__main__':
    print(read_json('newsafr.json'))