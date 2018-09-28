#!/usr/bin/env python

import Image
import ImageFilter


if __name__ == '__main__':
    in_im = Image.open('westbrook.jpg')
    out_im = Image.eval(in_im, lambda x: x*0.5)
    out_im.save('Q2,jpg')
