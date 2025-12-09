# (Logica di analisi)
from typing import Dict

def conta_caratteri(testo: str) -> int:
    '''Restituisce il numero totale di caratteri nella stringa, spazi inclusi.'''
    return len(testo)

def frequenza_caratteri(testo: str) -> Dict[str, int]:
    frequenze: Dict[str, int] = {}

    for carattere in testo:
        if carattere in frequenze:
            frequenze[carattere] += 1
        else:
            frequenze[carattere] = 1
    return frequenze

def conta_parole(testo: str) -> int:
    '''Restituisce il numero totale di parole nella stringa, spazi inclusi.'''
    return len(testo.split())