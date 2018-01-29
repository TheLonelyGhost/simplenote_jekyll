import json  # noqa
import os
import re
import unicodedata
from datetime import datetime

import simplenote


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters, and
    converts spaces to hyphens.
    """
    out = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    out = re.sub(r'[^\w\s-]', '', out).strip().lower()
    return re.sub(r'[-\s]+', '-', out)


def process_note(note):
    created = datetime.fromtimestamp(int(note['createdate'].split('.')[0]))
    updated = datetime.fromtimestamp(int(note['modifydate'].split('.')[0]))
    tags = [slugify(tag) for tag in note['tags'] if tag != 'blog']
    title = note['content'].splitlines()[0]
    content = '\n'.join(note['content'].splitlines()[1:])

    filename = '{}-{}.md'.format(
        created.isoformat(sep='T').split('T')[0],
        slugify(title),
    )

    return {
        'filename': filename,
        'created': created.isoformat(),
        'updated': updated.isoformat(),
        'tags': tags,
        'title': title,
        'content': content,
    }


def compile_frontmatter(data):
    out = []
    out.append('---')
    out.append('{}: {}'.format('layout', 'post'))
    out.append('{}: \'{}\''.format('title', data['title']))
    out.append('{}: {}'.format('date', data['created']))
    out.append('{}: {}'.format('created', data['created']))
    out.append('{}: {}'.format('updated', data['updated']))
    out.append('{}: {}'.format('categories', ' '.join(data['tags'])))
    out.append('---')
    return '\n'.join(out)


def main():
    username = os.getenv('SIMPLENOTE_USER')
    password = os.getenv('SIMPLENOTE_PASSWD')
    directory = os.path.expanduser(os.getenv(
        'JEKYLL_POSTS_DIR',
        os.path.join(os.getcwd(), '_posts')
    ))

    if not os.path.exists(directory):
        os.makedirs(directory)

    sn = simplenote.Simplenote(username, password)
    note_list, status = sn.get_note_list(tags=['blog'])
    for meta in note_list:
        note, status = sn.get_note(meta['key'])
        data = process_note(note)
        full_path = os.path.join(directory, data['filename'])
        front_matter = compile_frontmatter(data)
        with open(full_path, 'w') as f:
            f.write('\n\n'.join([front_matter, data['content']]))


if __name__ == '__main__':
    main()
