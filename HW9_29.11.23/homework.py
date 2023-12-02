#    number1
# def sstrings(strings):
#     mlen = max(len(s) for s in strings)
#     for s in strings:
#         stars = "*" * (mlen - len(s))
#         print(f"{stars}{s}")
#
# input = ['da', 'net', 'poka']
# sstrings(input)

#   number2
# def balance_array(arr):
#     posSum = sum(x for x in arr if x>0)
#     negSum = sum(x for x in arr if x<0)
#     diff = abs(posSum) - abs(negSum)
#     if diff>0:
#         arr.append(-diff)
#     else:
#         arr.append(abs(diff))
#     return arr
#
# input = [-3, -2, 1, 2, 3, 4]
# print(balance_array(input))

#     number3
# def ddomains(emails):
#     return list({email.split('@')[-1] for email in emails})
#
# input = [
#     'user@something.com'
#     'user1@example.com'
#     'user2@gmail.com'
# ]
# print(ddomains(input))

#         number4
# def vvowel(text):
#     vowels = "aeiouyAEIOUY"
#     words = text.split()
#     vowel_words = [word for word in words if word and word[0] in vowels]
#     return vowel_words
#
# # Пример текста
# input = "Apple car Footbal elephant"
# print(vvowel(input))

#         number5
# def razdeliteli(text, delimiter):
#     return [i for i in text if i not in delimiter]
#
# input_text = "Apple, car@ Footbal - elephant$ horse_"
# input_delimiter = [',', '@', '-', '$', '_']
# print(razdeliteli(input_text, input_delimiter))