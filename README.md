# 📊 Text Analyzer CLI & AI Summary 🚀

**Text Analyzer CLI** è uno strumento avanzato da riga di comando progettato per professionisti e studenti che desiderano analizzare rapidamente documenti di testo (`.txt`) e file PDF (`.pdf`). Sfruttando la potenza di **Google Gemini 2.5 Flash**, l'applicazione trasforma lunghi documenti in riassunti intelligenti e fornisce statistiche testuali dettagliate in pochi secondi.

---

## ✨ Caratteristiche Principali

- 📂 **Supporto Multi-formato**: Analisi nativa di file `.txt` e documenti `.pdf`.
- 📊 **Analisi Statistica Profonda**:
  - Conteggio totale delle parole.
  - Classifica delle **Top 5 parole più frequenti**.
  - Ricerca mirata di termini specifici nel testo.
  - Avvisi automatici per termini ricorrenti (più di 5 occorrenze).
- 🧠 **Riassunti Intelligenti con AI**:
  - Integrazione con **Google Gemini 2.5 Flash**.
  - **Supporto Multilingua**: Generazione di riassunti in **Italiano**, **Inglese** e **Tedesco**.
  - Formattazione elegante in Markdown con pannelli visivi.
- 🎨 **Interfaccia Premium**:
  - Menu interattivo basato su **Typer** e **Rich**.
  - Supporto al **Drag-and-Drop** per il percorso delle cartelle.
  - Tabelle e pannelli colorati per una leggibilità superiore.

---

## 🛠️ Tech Stack

- **Linguaggio**: Python 3.10+
- **CLI Framework**: [Typer](https://typer.tiangolo.com/)
- **UI & Styling**: [Rich](https://rich.readthedocs.io/)
- **AI Engine**: [Google Generative AI (Gemini 2.5 Flash)](https://ai.google.dev/)
- **PDF Processing**: [pypdf](https://pypdf.readthedocs.io/)
- **Environment Management**: [python-dotenv](https://saurabh-kumar.com/python-dotenv/)

---

## 🚀 Installazione Rapida

### 1. Clona il progetto
```bash
git clone <url-repo>
cd text_analyzer_project
```

### 2. Configura l'ambiente virtuale
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Configurazione API Gemini
Crea un file `.env` nella root del progetto e inserisci la tua API Key di Google AI Studio:
```env
GEMINI_API_KEY=LaTuaChiaveQui
```
*Puoi ottenere una chiave gratuita su [Google AI Studio](https://aistudio.google.com/).*

---

## 📖 Guida all'Utilizzo

1. **Avvio**: Esegui `python main.py`.
2. **Selezione Cartella**: Trascina la cartella contenente i tuoi documenti direttamente nel terminale o inserisci il percorso manuale.
3. **Selezione File**: Scegli il file da analizzare dall'elenco numerato.
4. **Analisi Interattiva**:
   - Digita `1` per cercare quante volte compare una parola.
   - Digita `2` per visualizzare la tabella delle statistiche generali.
   - Digita `3` per generare un riassunto AI (selezionando la lingua preferita).

---

## 📂 Struttura del Progetto

```text
text_analyzer_project/
├── main.py           # Gestione dell'interfaccia CLI e della logica di navigazione
├── stats.py          # Logica di analisi del testo e integrazione API Gemini
├── io_utils.py       # Utilità per la gestione dei file (opzionale/future espansioni)
├── requirements.txt  # Elenco delle dipendenze necessarie
├── .env              # Variabili d'ambiente (non incluso nel commit)
└── text/             # Cartella di esempio per i documenti
```

---

## 📄 Licenza

Distribuito sotto Licenza MIT. Consulta il file `LICENSE` per ulteriori informazioni.

---

<p align="center">Creato con ❤️ per semplificare l'analisi dei tuoi dati.</p>
