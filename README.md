# Text Analyzer CLI Project

Un tool CLI modulare e "production-ready" per l'analisi di file di testo.

## Funzionalità

*   **Selezione Guidata**: Seleziona una cartella e poi un file `.txt` dall'elenco.
*   **Analisi Statistica**: 
    *   Conteggio totale parole.
    *   Top 5 parole più frequenti.
    *   Ricerca obbligatoria di una parola target.
    *   Visualizzazione opzionale delle parole che compaiono più di 5 volte.
*   **AI Ready**: Predisposizione per riassunti automatici (Stub implementato).

## Setup

1.  Crea e attiva il virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Mac/Linux
    ```
2.  Installa le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```

## Utilizzo

Avvia il programma:

```bash
python main.py
```

Segui le istruzioni a video per selezionare la cartella, il file e i parametri di analisi.

## Qualità Codice

Verifica la qualità del codice con:

```bash
ruff check .
```
