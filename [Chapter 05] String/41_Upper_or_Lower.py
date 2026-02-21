text = input()

if text.upper() == text and text.lower() != text:
    print('Upper')
elif text.upper() != text and text.lower() == text:
    print('Lower')
else:
    print('Mixed')