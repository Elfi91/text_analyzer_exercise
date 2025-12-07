from typing import Optional # Importiamo Optional per indicare che la funzione può restituire None

def leggi_file(percorso: str) -> Optional[str]:
    '''Accetta il percorso di un file, ne restituisce il contenuto come stringa.
    Gestisce FileNotFoundError in caso di file inesistente.'''
    try:
        # Tenta di aprire il file e leggere tutto il contenuto
        with open(percorso, "r") as file:
            content = file.read()
            return content
            
    except FileNotFoundError:
        # Se il file non è stato trovato, stampiamo un messaggio di errore all'utente
        print(f"\nERRORE: File non trovato al percorso specificato: '{percorso}'")
        # Restituiamo None per segnalare al programma principale che l'operazione è fallita
        return None
    except Exception as e:
        # Catturiamo altri possibili errori (es. permessi)
        print(f"\nERRORE in lettura file: {e}")
        return None