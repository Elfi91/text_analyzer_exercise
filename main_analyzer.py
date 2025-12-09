# Importazioni dai moduli creati:
from text_analyzer import conta_caratteri, frequenza_caratteri, conta_parole
from io_utils import leggi_file
from typing import Dict, Any

def main():
    '''Funzione principale che orchestra il flusso di analisi del testo.'''
    
    # 1. Chiedi all'utente il percorso del file
    percorso_file = input("Inserisci il percorso del file di testo da analizzare: ")
    
    # 2. Leggi il file utilizzando il modulo I/O
    contenuto_testo = leggi_file(percorso_file)
    
    # 3. Controlla il Contenuto (gestione dell'errore)

    # Se leggi_file restituisce None (a causa di FileNotFoundError), usciamo.
    if contenuto_testo is None:
        print("\nAnalisi interrotta.")
        return # Termina l'esecuzione della funzione main()
        
    # --- IL FILE È STATO LETTO CON SUCCESSO ---
    totale_parole = conta_parole(contenuto_testo)


    # 4. Analisi: Numero totale di caratteri
    totale_caratteri = conta_caratteri(contenuto_testo)
    print("\n" + "="*40)
    print(f"Risultato Analisi per il file: {percorso_file}")
    print("="*40)
    print(f"A) Numero totale di parole: {totale_parole}")
    print(f"B) Numero totale di caratteri (spazi inclusi): {totale_caratteri}")
    
    # 5. Analisi: Calcolo della frequenza
    frequenze = frequenza_caratteri(contenuto_testo)


    # 6. Output Filtrato: Solo i caratteri che compaiono più di 5 volte
    
    SOGLIA = 5
    caratteri_filtrati_trovati = False
    
    print(f"C) Caratteri che compaiono più di {SOGLIA} volte:")


    # Iteriamo sul dizionario delle frequenze
    
    for carattere, conteggio in frequenze.items():
        if conteggio > SOGLIA:
            # Stampiamo solo se il conteggio supera la soglia
            print(f"  - '{carattere}': {conteggio} volte")
            caratteri_filtrati_trovati = True
            
    if not caratteri_filtrati_trovati:
        print(f"  Nessun carattere compare più di {SOGLIA} volte.")

    print("="*40)

    # 7. Output Filtrato: Solo le parole che compaiono più di 2 volte

    Soglia_parole = 2
    parole_filtrate_trovate = False

    print(f"D) Parole che compaiono più di {Soglia_parole} volte:")

    for parola, conteggio in frequenze.items():
        if conteggio > Soglia_parole:
            # Stampiamo solo se il conteggio supera la soglia
            print(f"  - '{carattere}': {conteggio} volte")
            parole_filtrate_trovate = True
            
    if not parole_filtrate_trovate:
        print(f"  Nessun carattere compare più di {Soglia_parole} volte.")

    print("="*40)



# Punto di ingresso del programma
if __name__ == "__main__":
    main()