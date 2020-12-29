import os


def diskdir():
    dirlist = []
    for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if os.path.exists(f'{drive_letter}:'):
                # print(f'{drive_letter}:')
                dirlist.append([f'{drive_letter}'])
            else:
                pass
    return dirlist
