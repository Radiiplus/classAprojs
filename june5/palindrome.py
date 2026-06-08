thoughts = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon, no melon',
    'some men interpret nine memos',
    'madam'
]

for item in thoughts:
    cleaned = item.replace(" ", "").replace(",", "")
    
    if cleaned == cleaned[::-1]:
        print(f"{item} is Palindrome")
    else:
        print(f"{item} is not a palindrome")