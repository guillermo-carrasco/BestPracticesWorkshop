import re

from BestPracticesWorkshop import REV_COM_TRANSLATION

def search(text, pattern):
    return [str(m.start()) for m in re.finditer('(?=' + pattern + ')' , text)]


def reverse_complement(DNA, as_string=False):
    reverse = [REV_COM_TRANSLATION.get(c) for c in DNA[::-1]]
    if as_string:
        reverse = ''.join(reverse)
    return reverse


def extract_kmers(k, DNA):
    kmers = set()
    [kmers.add(DNA[i:i+int(k)]) for i in range(len(DNA) - k + 1)]
    return kmers


def most_frequent_kmer(DNA, k, reverse=False):
    results = {}
    kmers = extract_kmers(k, DNA)
    for kmer in kmers:
        n = len(search(kmer, DNA))
        if reverse:
            n += len(search(''.join(reverse_complement(kmer)), DNA))
        if results.has_key(n):
            results[n].append(kmer)
        else:
            results[n] = [kmer]
    return results[max(results.keys())]
