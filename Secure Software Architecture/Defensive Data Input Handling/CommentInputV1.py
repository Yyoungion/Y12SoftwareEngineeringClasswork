comment = input("Write your comment: ")

comment = comment.replace('<script>', '')


comment = comment.replace('&', '').replace('<', '').replace('>', '')

if len(comment) > 200:
    print('Error. Comment cannot be over 200 characters')

else:
    print(f"User comment: {comment}")   