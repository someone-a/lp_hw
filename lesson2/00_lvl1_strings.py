import requests

url = "https://gist.githubusercontent.com/Melevir/7e347126f978af72c5de108f3909cc85/raw/f198d012e009faeef3dfba1eba9a37a6da0f7617/string_challenges.py"
url_text = requests.get(url)
exec(url_text.text)

list_of_vowels = [i for i in "аеёиоуэюя"]
print(word[-1])
print(word.count("а"))
print(sum([word.lower().count(letter) for letter in list_of_vowels]))
print(len(sentence.split()))
[print(word[0]) for word in sentence.split()]
print(len(''.join(sentence.split())) / (len(sentence.split())))