with open('new_file.text', mode='w') as file:
    file.write("New text.")


with open('text.text') as file:
    contents = file.read()
    print(contents)
