import os
import simplenote


def main():
    username = os.getenv('SIMPLENOTE_USER')
    password = os.getenv('SIMPLENOTE_PASSWD')

    sn = simplenote.SimpleNote(username, password)
    note_list, status = sn.get_notes_list(tag=['blog'])
    for note in note_list:
        print('Note:')
        print(repr(note))
        print('\n\n')


if __name__ == '__main__':
    main()
