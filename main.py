import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm, Prompt
from rich.markdown import Markdown
from rich.panel import Panel
import stats

app = typer.Typer()
console = Console()

def get_folder_from_user() -> Path | None:
    """
    Asks user for a folder path until valid or exit.
    Returns Path object or None (exit).
    """
    while True:
        console.print("[dim]Suggerimento: Puoi trascinare la cartella qui dentro o scrivere il percorso completo (es. /Users/nome/Desktop/pdf)[/dim]")
        folder_path_str = Prompt.ask("Inserisci il percorso assoluto della CARTELLA contenente i file (o 'q' per uscire)")
        
        if folder_path_str.lower() in ("q", "quit", "exit"):
            return None
            
        # Clean input
        folder_path_str = folder_path_str.strip().strip("'").strip('"')
        folder_path = Path(folder_path_str).expanduser().resolve()

        if not folder_path.exists():
            console.print(f"[bold red]Errore: La cartella '{folder_path}' non esiste. Riprova.[/bold red]")
            continue
        
        if not folder_path.is_dir():
             console.print(f"[bold red]Errore: '{folder_path}' non è una cartella. Riprova.[/bold red]")
             continue
             
        return folder_path

def select_file_in_folder(folder_path: Path):
    """
    Lists files in the given folder and asks user to pick one.
    Returns:
    - Path object (selected file)
    - "BACK" (change folder)
    - "EXIT" (quit app)
    """
    while True:
        # List .txt and .pdf files
        files = sorted(list(folder_path.glob("*.txt")) + list(folder_path.glob("*.pdf")))
        
        if not files:
            console.print(f"[bold yellow]Nessun file .txt o .pdf trovato in '{folder_path}'.[/bold yellow]")
            if Confirm.ask("Vuoi selezionare un'altra cartella?", default=True):
                return "BACK"
            else:
                return "EXIT"

        console.print(f"\n[green]File trovati in {folder_path.name}:[/green]")
        for i, file in enumerate(files, 1):
            console.print(f"{i}. {file.name}")
        
        choice = Prompt.ask("Seleziona il numero del file (0 per cambiare cartella, 'q' per uscire)")
        
        if choice.lower() in ("q", "quit", "exit"):
            return "EXIT"
        
        if choice == "0":
            return "BACK"

        try:
            file_index = int(choice)
            if 1 <= file_index <= len(files):
                return files[file_index - 1]
            console.print(f"[bold red]Per favore inserisci un numero tra 1 e {len(files)}[/bold red]")
        except ValueError:
            console.print("[bold red]Input non valido.[/bold red]")

def show_file_menu(file_path: Path, clean_text: str, statistics: dict):
    """
    Shows the action menu for a selected and processed file.
    """
    while True:
        console.print("\n[bold cyan]Cosa vuoi fare con questo file?[/bold cyan]")
        console.print("1. Cerca una parola specifica")
        console.print("2. Mostra statistiche (Totale pagine/parole, Top 5)")
        console.print("3. Riassunto con AI Gemini")
        console.print("4. Torna alla lista file")
        console.print("5. Esci")

        choice = Prompt.ask("Seleziona opzione", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            target_word = Prompt.ask("Inserisci la parola da cercare")
            # Re-process to get specific count if simpler, or just search in text logic
            # Since our stats engine does it all at once, we can just look at word_counts if we have them
            # We already have statistics['word_counts'] from previous load
            word_counts = statistics.get("word_counts", {})
            count = word_counts.get(target_word.lower(), 0)
            console.print(f"\nLa parola '[bold green]{target_word}[/bold green]' compare [bold]{count}[/bold] volte.")

        elif choice == "2":
            # Show standard stats
            console.print("\n[bold green]Statistiche Analisi:[/bold green]")
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Metrica", style="dim")
            table.add_column("Valore")
            table.add_row("Totale Parole", str(statistics["total_words"]))
            top_5_str = ", ".join([f"{w} ({c})" for w, c in statistics["top_5"]])
            table.add_row("Top 5 Parole", top_5_str)
            console.print(table)
            
            # > 5 words check
            word_counts = statistics.get("word_counts", {})
            common_words = {word: count for word, count in word_counts.items() if count > 5}
            if common_words:
                 console.print(f"\n[dim]Ci sono {len(common_words)} parole che compaiono più di 5 volte.[/dim]")

        elif choice == "3":
            console.print("\n[bold cyan]In che lingua vuoi il riassunto?[/bold cyan]")
            console.print("1. Italiano")
            console.print("2. Inglese")
            lang_choice = Prompt.ask("Seleziona", choices=["1", "2"], default="1")
            
            target_lang = "Italiano" if lang_choice == "1" else "Inglese"
            
            console.print(f"\n[italic]Generazione riassunto in {target_lang} in corso con Gemini...[/italic] ⏳")
            summary_text = stats.get_ai_summary(clean_text, target_language=target_lang)
            
            # Rendering bellissimo con Markdown e Panel
            md = Markdown(summary_text)
            console.print(Panel(md, title=f"AI Summary ({target_lang})", border_style="cyan", expand=False, padding=(1, 2)))
            console.print("")

        elif choice == "4":
            return "BACK_TO_LIST"
            
        elif choice == "5":
            return "EXIT_APP"

def main():
    console.print("[bold blue]Benvenuto nel Text Analyzer CLI![/bold blue] 🚀")
    
    current_folder = None

    while True:
        # 1. Folder Selection Phase (Sticky)
        if current_folder is None:
            current_folder = get_folder_from_user()
            if current_folder is None: # User quit
                console.print("Arrivederci! 👋")
                break

        # 2. File Selection Phase
        selection = select_file_in_folder(current_folder)
        
        if selection == "EXIT":
            console.print("Arrivederci! 👋")
            break
        
        if selection == "BACK":
            current_folder = None
            continue
            
        file_path = selection
        console.print(f"[dim]Caricamento file: {file_path.name}...[/dim]")

        # 3. Load & Process Once
        try:
            # We process initially without a target word to get base stats
            clean_text, statistics = stats.process_text(file_path)
        except Exception as e:
             console.print(f"[bold red]Errore durante la lettura/analisi:[/bold red] {e}")
             input("Premi invio per continuare...")
             continue

        # 4. Action Menu Loop
        action = show_file_menu(file_path, clean_text, statistics)
        
        if action == "EXIT_APP":
            console.print("Arrivederci! 👋")
            break
        # If BACK_TO_LIST, loop naturally goes back to select_file_in_folder

if __name__ == "__main__":
    typer.run(main)