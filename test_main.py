from RegExpClass import *


def test_True_1():
    s = RegExp("ab+c+1+", 'c', 729)
    assert(s.parse() == True)


def test_True_2():
    s = RegExp("ab.aba.*.bac.+.+*", 'a', 2)
    assert(s.parse() == True)


def test_True_3():
    s = RegExp("ac+ba.*.a.*ab1+..", 'b', 34)
    assert(s.parse() == True)


def test_False_1():
    s = RegExp("a*b.b+", 'b', 5)
    assert(s.parse() == False)


def test_False_2():
    s = RegExp("ccc.*.ab.*", 'c', 10)
    assert(s.parse() == False)
