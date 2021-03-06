#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Windows illegal characters
# https://en.wikipedia.org/wiki/Filename
# TODO: Collisions possible
# TODO: May be slow
def make_windows_compatible(path):
    windows_illegal = [
        '/',
        '\\',
        '?',
        '%',
        '*',
        ':',
        '|',
        '"',
        '<',
        '>'
    ]
    for char in windows_illegal:
        path = path.replace(char, '_')

    return path


try:
    import os
    import sys
    import shutil

    import mutagen

    # Source
    src_file = sys.argv[1]
    file_info = mutagen.File(src_file, easy=True)
    try:
        albumartist = file_info['albumartist']
    except KeyError:
        albumartist = file_info['artist']

    try:
        discnumber = file_info['discnumber'][0].split("/")[0]
    except KeyError:
        discnumber = 1

    # Destination
    dst_root_dir = sys.argv[2]
    dst_dir = os.path.join(
        dst_root_dir,
        make_windows_compatible(albumartist[0]),
        make_windows_compatible(file_info['album'][0]))
    dst_filename = ""
    dst_filename += str(discnumber) + "-"
    dst_filename += str(file_info['tracknumber'][0]).split("/")[0].zfill(2)\
        + " "
    dst_filename += str(file_info['title'][0]).replace("/", "_")\
        + os.path.splitext(src_file)[1]
    dst_file = os.path.join(dst_dir, make_windows_compatible(dst_filename))

    # Same as `mkdir -p dst_dir`
    os.makedirs(dst_dir, exist_ok=True)

    # Same as `cp src_file dst_file`
    try:
        shutil.copyfile(src_file, dst_file)
    except shutil.SameFileError:
        pass
except KeyboardInterrupt:
    exit(1)
