import os

class WordFileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

        if not os.path.exists(filepath):
            f = open(filepath, 'w', encoding='utf-8')
            f.write('') 
            f.close()

        f = open(filepath, 'r', encoding='utf-8')
        text = f.read()
        f.close()

        self.words = text.split()

    def delete_word(self, word):
        self.words = [w for w in self.words if w != word]

    def update_source(self):
        f = open(self.filepath, 'w', encoding='utf-8')
        f.write(' '.join(self.words))
        f.close()


if __name__ == "__main__":
    handler = WordFileHandler("example.txt")
    print("Изначальные слова:", handler.words)

    handler.delete_word("example")
    print("После удаления:", handler.words)

    handler.update_source()
