import os


async def show_size(file_name):
    size = os.path.getsize(file_name)
    q = 0
    while q < 2:
        if size > 1024:
            size = size / 1024
        else:
            break
        q += 1

    if q == 1:
        value = 'kb'
    elif q == 2:
        value = 'mb'
    elif q == 0:
        value = "byte"
    else:
        value = 'mb'

    return f'{round(size, 1)} {value}'
