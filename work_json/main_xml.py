import xml.etree.ElementTree as ET
from collections import Counter


def read_xml(file_path, word_min_len=6, top_words_amt=10):
    """
    Функция для чтения файла с новостями и возврата самых частых слов.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    all_words = []

    for description in root.findall('./channel/item/description'):
        if description.text:
            words = description.text.split()

            # ИЗМЕНЕНИЕ ЗДЕСЬ: используем строго больше (>),
            # чтобы при word_min_len=6 брались слова от 7 символов.
            filtered_words = [word for word in words if len(word) > word_min_len]
            all_words.extend(filtered_words)

    word_counts = Counter(all_words)

    top_words = [word for word, count in word_counts.most_common(top_words_amt)]

    return top_words


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))