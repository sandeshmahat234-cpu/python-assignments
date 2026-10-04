text = input("Enter a string: ")

seen = []
found = False

for ch in text:
    if ch in seen:
        print("First repeated character:", ch)
        found = True
        break
    seen.append(ch)

if not found:
    print("No repeated character found")