import os
import time
__author__ = 'robbie'


start_time = time.time()


def get_bible_words():
    bible = open('bible.txt', 'r').read().lower().split()
    return bible


def get_freq_dictionary_from_file(file_name):
    file = open(file_name, 'r')
    words = {}

    for word in file.read().split():

        word = ''.join(filter(str.isalpha, word)).lower()

        if word == '':
            continue

        if word not in words:
            words[word] = 1
        else:
            words[word] = words[word] + 1

    file.close()

    return words


def write_frequential_dic_to_file(dic):
    f = open('frequential_table_from_dic.txt', 'w')

    for key, value in dic.items():
        f.write(str(key) + "=" + str(value) + "\n")

    f.close()


file_name = "bible.txt"
counted_words = get_freq_dictionary_from_file(file_name)
write_frequential_dic_to_file(counted_words)


class TrieNode:
    def __init__(self):
        self.n = 0
        self.d = {}

    def __repr__(self, res=""):

        for k in self.d:
            res += k + "=" + str(self.d[k].n) + "\n"
            res += self.d[k].__repr__()

        return res

    def scission(self, oldKey, prefix, word):

        self.d[prefix] = TrieNode()
        prenode = self.d[prefix]
        prenode.d[oldKey] = self.d[oldKey]
        prenode.d[word] = TrieNode()
        prenode.d[word].n = 1
        del self.d[oldKey]

    def insert(self, word, pre=""):

        if word in self.d.keys():
            self.d[word].n += 1
        else:
            is_prefix_found = False
            for k in self.d:
                prefix = os.path.commonprefix([k, word])

                if len(prefix) > 0:
                    is_prefix_found = True

                    if prefix == pre:
                        self.d[word] = TrieNode()
                        self.d[word].n = 1
                        break

                    if prefix == k:
                        self.d[k].insert(word, prefix)
                        break

                    if prefix != pre and prefix != k:
                        self.scission(k, prefix, word)
                        break

            if not is_prefix_found:
                self.d[word] = TrieNode()
                self.d[word].n = 1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self.root.insert(word)

    def __repr__(self):
        return self.root.__repr__()


def words_to_trie(words):
    trie = Trie()
    for word in words:

        if len(words):
            word = ''.join(filter(str.isalpha, word)).lower()
            trie.insert(word)
    return trie

def trie_to_frequential_file(t):

    f = open("frequential_table_from_trie.txt", 'w')
    f.write(t.__repr__())
    f.close()

# method 2
trie_to_frequential_file(words_to_trie(get_bible_words()))

print("--- %s seconds ---" % (time.time() - start_time))
