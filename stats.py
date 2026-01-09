import string
from collections import Counter
from pathlib import Path
import os
import pypdf
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def extract_text(path: Path) -> str:
    """
    Extracts text from a file based on its extension.
    
    Args:
        path (Path): The path to the file.
        
    Returns:
        str: The extracted text.
        
    Raises:
        NotImplementedError: If the file extension is not supported.
    """
    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")
    elif path.suffix.lower() == ".pdf":
        try:
            reader = pypdf.PdfReader(path)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
            return "\n".join(text)
        except Exception as e:
            # Wrap pypdf errors in a consistent way if needed, or let bubble up
            raise RuntimeError(f"Error reading PDF: {e}")
    else:
        raise NotImplementedError(f"Extension {path.suffix} not supported yet.")

def get_ai_summary(text: str, target_language: str = "Italiano") -> str:
    """
    Generates a summary of the text using Google Gemini API in the specified language.
    
    Args:
        text (str): The text to summarize.
        target_language (str): The language for the summary.
        
    Returns:
        str: The generated summary or an error message.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ API Key mancante. Crea un file .env con GEMINI_API_KEY=..."

    try:
        client = genai.Client(api_key=api_key)
        
        # Truncate text if too long
        MAX_CHAR_PREVIEW = 25000 
        text_preview = text[:MAX_CHAR_PREVIEW]
        
        if target_language.lower() == "inglese":
            prompt = (
                "Act as an expert document analyst. "
                "Provide a detailed yet concise summary of the following text in ENGLISH. "
                "Organize the summary with bullet points if necessary and highlight key concepts.\n\n"
                f"Text to analyze:\n{text_preview}"
            )
        else:
            prompt = (
                "Agisci come un analista di documenti esperto. "
                "Fai un riassunto dettagliato ma conciso del seguente testo in lingua ITALIANA. "
                "Organizza il riassunto con punti elenco. "
                "IMPORTANTE: Lascia sempre una riga vuota tra ogni paragrafo e tra i punti elenco per massimizzare la leggibilità.\n\n"
                f"Testo da analizzare:\n{text_preview}"
            )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash", # Il modello più stabile e con più quota per il piano gratuito
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Errore API: {e}"

def process_text(file_path: Path, target_word: str | None = None) -> tuple[str, dict]:
    """
    Processes the text file and calculates statistics.
    
    Args:
        file_path (Path): Path to the file.
        target_word (str, optional): A specific word to count.
        
    Returns:
        tuple[str, dict]: A tuple containing the cleaned text and a dictionary of statistics.
    """
    # 1. Extraction
    raw_text = extract_text(file_path)
    
    # 2. Cleaning
    # Convert to lowercase
    text_lower = raw_text.lower()
    
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text_lower.translate(translator)
    
    # 3. Stats
    words = clean_text.split()
    total_words = len(words)
    
    word_counts = Counter(words)
    top_5 = word_counts.most_common(5)
    
    stats = {
        "total_words": total_words,
        "top_5": top_5,
        "word_counts": word_counts  # Added for > 5 filtering
    }
    
    if target_word:
        target_clean = target_word.lower()
        stats["target_word_count"] = word_counts[target_clean]
        
    return clean_text, stats
