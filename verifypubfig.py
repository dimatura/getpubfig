#!/usr/bin/env python

import hashlib
import os
import sys

def get_md5(file_path):
    img_handle = open(file_path, 'rb')
    img_str = img_handle.read()
    img_handle.close()
    h = hashlib.md5()
    h.update(img_str)
    return h.hexdigest()

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('dev', 'eval'):
        usage()
        return
    path = sys.argv[1]

    if not os.path.exists(path+'_bad'):
        os.mkdir(path+'_bad')
    for f in os.listdir(path):
        fullpath = os.path.join(path, f)
        correct_md5,ext = os.path.splitext(f)
        md5 = get_md5(fullpath)
        print md5, correct_md5
        if md5==correct_md5:
            pass
        else:
            print '%s md5 not OK'%(f)
            os.rename(fullpath, os.path.join(path+'_bad', f))
            #os.remove(fullpath)

if __name__ == '__main__':
    main()
