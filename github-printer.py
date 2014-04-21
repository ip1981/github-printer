#!/usr/bin/python3

"""
Written by Igor Pashev <pashev.igor@gmail.com>

The author has placed this work in the Public Domain,
thereby relinquishing all copyrights. Everyone is free
to use, modify, republish, sell or give away this work
without prior consent from anybody.
"""

import datetime
import os
import shutil
import subprocess

from glyphs import glyphs

git_binary = 'git'
repo_dir = 'repo'
content_file = 'story'

def git(*args):
    subprocess.check_call([git_binary] + list(args))

def init_repo(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    git('init', path)
    os.chdir(path)
    open(content_file, 'a').close()
    git('add', content_file)


def start_date():
    """ Returns next nearest sunday - top line in github graph """
    day = datetime.date.today()
    while day.weekday() != 6:
        day += datetime.timedelta(days=1)
    return day

def dates(text):
    date = start_date() + datetime.timedelta(weeks=-50)
    print ('start date: {}'.format(date))
    row_start_date = date
    for row in glyphs(text):
        commit_date = row_start_date
        for c in row:
            if not c.isspace():
                commit_datetime = datetime.datetime.combine(commit_date, datetime.time(12, 0, 0))
                for n in range(50):
                    yield commit_datetime
                    commit_datetime += datetime.timedelta(minutes=1)
            commit_date += datetime.timedelta(weeks=1)
        row_start_date += datetime.timedelta(days=1)


def imprint(text):
    for date in sorted(dates(text)):
        date_str = date.isoformat()
        with open(content_file, 'a') as cnt:
            cnt.write(date_str)
            cnt.write("\n")
        git('commit', content_file, '--date={}'.format(date_str), '-m', date_str)

if __name__ == '__main__':
    init_repo(repo_dir)
    imprint('Hello :)')

