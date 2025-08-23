import string

EMOJI_MAP = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "surprised": "😲",
    "love": "❤️"
}

def replace_emoji(text):
    words = text.split()
    new_words = []
    for word in words:
        cleaned_word = word.lower().strip(string.punctuation)
        new_words.append(EMOJI_MAP.get(cleaned_word, word))
        
    return ' '.join(new_words)

text = input("Enter text: ")
print(replace_emoji(text))