import re

from BestPracticesWorkshop import REV_COM_TRANSLATION

def search(pattern, text):
    return [str(m.start()) for m in re.finditer('(?=' + pattern + ')' , text)]


def r_c(d, as_string=False):
    reverse = [REV_COM_TRANSLATION.get(c) for c in d[::-1]]
    if as_string:
        reverse = ''.join(reverse)
    return reverse


def ext_k(k, DNA):
    kmers = set()
    [kmers.add(DNA[i:i+int(k)]) for i in range(len(DNA) - k)]
    return kmers


def mfk(s, k, r=False):
    res = {}
    k = ext_k(k, s)
    for elem in k:
        n = len(search(elem, s))
        if r:
            n += len(search(''.join(r_c(elem)), s))
        if res.has_key(n):
            res[n].append(elem)
        else:
            res[n] = [elem]
    return res[max(res.keys())]
