#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib


def calcsha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        return sha1obj.hexdigest()


def calcmd5(filepath):
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        return md5obj.hexdigest()


class VFile:
    sha1 = None
    md5 = None
    
    def __init__(self, sourcefilepath):
        self.sourcefilepath = sourcefilepath
        self.sha1 = calcsha1(sourcefilepath)
        self.md5 = calcmd5(sourcefilepath)

    def compare_verify_strings(self, targetverifystring, algorithm='sha1'):
        if algorithm == 'sha1':
            return self.sha1 == targetverifystring.lower()
        elif algorithm == 'md5':
            return self.md5 == targetverifystring.lower()

    def compare_files(self, targetfilepath, algorithm='sha1'):
        targetfile = VFile(targetfilepath)
        if algorithm == 'sha1':
            return targetfile.sha1 == self.sha1
        elif algorithm == 'md5':
            return targetfile.md5 == self.md5


def smart_comparison(source, target):
    if os.path.isfile(source):
        sf = VFile(source)
        print('FilePath: ', source)
        print('\tSH1: ', sf.sha1)
        print('\tMD5: ', sf.md5)
        if os.path.isfile(target):
            tf = VFile(target)
            print('FilePath: ', target)
            print('\tSH1: ', tf.sha1)
            print('\tMD5: ', tf.md5)
        else:
            target = target.lower()
            print('Verify String: ', target)
            if len(target) == 40:
                print('Identical: ', str(sf.sha1 == target))
            else:
                print('Identical: ', str(sf.md5 == target))
    else:
        source = source.lower()
        print('Verify String: ', source)
        if os.path.isfile(target):
            tf = VFile(target)
            print('FilePath: ', target)
            print('\tSH1: ', tf.sha1)
            print('\tMD5: ', tf.md5)
            if len(source) == 40:
                print('Identical: ', str(tf.sha1 == source))
            else:
                print('Identical: ', str(tf.md5 == source))
        else:
            target = target.lower()
            print('Verify Sring: ', target)
            print('Identical: ', str(source == target))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        print()
        print('Computing...')
        smart_comparison(sys.argv[1], sys.argv[2])
    elif len(sys.argv)==2 and os.path.isfile(sys.argv[1]):
        print()
