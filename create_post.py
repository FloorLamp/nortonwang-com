#!/usr/bin/python

import sys
from datetime import datetime

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: ./create_post.py name'
        exit()
    else:
        name = sys.argv[1]
        now = datetime.now()
        filename = 'content/{}-{}.md'.format(now.strftime('%Y-%m'), name.lower())
        with open(filename, 'w') as file:
            file.write('Title: {}\n'.format(name))
            file.write('Date: {}\n'.format(now.strftime('%Y-%m-%d %H:%M')))
            file.write('Tags:\n\n\n')

        print 'Created {}'.format(filename)
        exit()