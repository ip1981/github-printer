"""
Written by Igor Pashev <pashev.igor@gmail.com>

The author has placed this work in the Public Domain,
thereby relinquishing all copyrights. Everyone is free
to use, modify, republish, sell or give away this work
without prior consent from anybody.
"""

""" Seven lines in height """
GLYPHS = {
    'H' : [
            '#  #',
            '#  #',
            '#  #',
            '####',
            '#  #',
            '#  #',
            '#  #',
            ],
    'e' : [
            '    ',
            '    ',
            ' ## ',
            '#  #',
            '### ',
            '#   ',
            ' ###',
            ],
    'l' : [
            ' #  ',
            ' #  ',
            ' #  ',
            ' #  ',
            ' #  ',
            ' #  ',
            '  ##',
            ],
    'o' : [
            '    ',
            '    ',
            ' ## ',
            '#  #',
            '#  #',
            '#  #',
            ' ## ',
            ],
    ':' : [
            '  ',
            '##',
            '##',
            '  ',
            '##',
            '##',
            '  ',
            ],
    ';' : [
            '  ',
            '##',
            '##',
            '  ',
            '##',
            '##',
            ' #',
            ],
    ')' : [
            '#  ',
            ' # ',
            '  #',
            '  #',
            '  #',
            ' # ',
            '#  ',
            ],
    ' ' : [
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ],
    }

MISSING = [
            ' ## ',
            '#  #',
            '   #',
            '  # ',
            ' #  ',
            '    ',
            ' #  ',
            ]

def text2glyphs(text):
    for c in text:
        try:
            yield GLYPHS[c]
        except KeyError:
            yield MISSING

def glyphs(text):
    ret = ['' for n in range(7)]
    for glyph in text2glyphs(text):
        for n in range(7):
            ret[n] += glyph[n] + ' '
    return ret

