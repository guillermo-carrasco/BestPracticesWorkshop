import re

from BestPracticesWorkshop import REV_COM_TRANSLATION

def search(pattern, text):
    """Searches for exact matchings of pattern in text.

    :param text: String where to perform the search
    :param pattern: Pattern to search within text
    :return: A list containing all positions where an occurrence of pattern starts in text.
    :rtype: list
    """
    return [str(m.start()) for m in re.finditer('(?=' + pattern + ')' , text)]


def reverse_complement(DNA, as_string=False):
    """Calculates the reverse complement of DNA.

    :param DNA: String representing a DNA sequence.
    :param as_string: If true, return the reverse complement as a string
    :return: The reverse complement of DNA
    :rtype: list
    """
    reverse = [REV_COM_TRANSLATION.get(c) for c in DNA[::-1]]
    if as_string:
        reverse = ''.join(reverse)
    return reverse


def extract_kmers(k, DNA):
    """Returns a set of all k-mers in DNA.

    :param k: Length of the k-mer
    :param DNA: String representing a DNA sequence.
    :return: Set of all k-mers on DNA
    :rtype: set
    """
    kmers = set()
    [kmers.add(DNA[i:i+int(k)]) for i in range(len(DNA) - k + 1)]
    return kmers


def most_frequent_kmer(DNA, k, reverse=False):
    """Find mosf frequent k-mers in DNA.

    :param DNA: String representing a DNA sequence
    :param k: Length of the k-mer
    :param reverse: If true, search also the k-mers' reverse complements
    :return: A set of most common k-mers in DNA
    :rtype: set
    """
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
