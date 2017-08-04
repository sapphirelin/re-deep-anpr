#!/usr/bin/env python
#
# Copyright (c) 2017 Sapphire Lin
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
#     NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#     OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#     USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
製作測試資料的背景圖片

"""

__all__ = (
    'extract_backgrounds',
)

import os
import tarfile

import cv2
import numpy


def im_from_file(f):
    print("This is im_from_file(f):",f)    
    a = numpy.asarray(bytearray(f.read()), dtype=numpy.uint8)
    return cv2.imdecode(a, cv2.IMREAD_GRAYSCALE )

def extract_backgrounds(archive_name):
    """
    解壓縮背景圖片 (from a tar archive)
    將圖片們 (JPEGs) 轉換成灰階 (grayscale)
    再裁切 (cropped/resized) 成一定大小 (256x256)
    存至指定資料夾 (./bgs/)
    
    """
    try:
        os.mkdir("bgs")
    except:
        pass
    
    t = tarfile.open(name=archive_name)

    def members():
        m = t.next()
        while m:
            yield m
            m = t.next()
    index = 0
    for m in members():
        if not m.name.endswith(".jpg"):
            continue
        f =  t.extractfile(m)
        try:
            im = im_from_file(f)
        finally:
            f.close()
        if im is None:
            continue
            
        if im.shape[0] > im.shape[1]:
            im = im[:im.shape[1], :]
        else:
            im = im[:, :im.shape[0]]
        if im.shape[0] > 256:
            im = cv2.resize(im, (256, 256))
        fname = "bgs/{:08}.jpg".format(index)
        ## print the filename of images
        print (fname)                         
        rc = cv2.imwrite(fname, im)
        if not rc:
            raise Exception("Failed to write file {}".format(fname))
        index += 1

"""
archive_name = 背景圖片壓縮檔

"""
if __name__ == "__main__":
    archive_name = "SUN397.tar.gz"
    if archive_name in os.listdir(os.getcwd()):
        extract_backgrounds(os.getcwd()+"\\"+archive_name)
    else:
        print("找不到壓縮檔 (archive_name error)")
