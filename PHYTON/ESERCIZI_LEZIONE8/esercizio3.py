
#Context Managers for File Handling: Use the with statement and context managers to open and close a file. 
#Handle potential IOError within the with block for clean resource management.


def read_file(filepath: str) -> str:
    """Legge il contenuto di un file in modo sicuro usando un context manager.

    Parameters:
    filepath (str): Percorso del file da leggere.

    Returns:
    str: Contenuto del file o messaggio di errore.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        return f"Errore nella lettura del file: {e}"

# Esempio (modificare il percorso se necessario)
print(read_file("esempio.txt"))
