import re

def calcola_carattere_controllo(codice_fiscale):
    """Calcola il carattere di controllo atteso per i primi 15 caratteri."""
    
    # Valori per posizioni dispari (1, 3, 5, ... in base 1)
    valori_dispari = {
        '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
        'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
        'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
        'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
    }
    
    # Valori per posizioni pari (2, 4, 6, ... in base 1)
    valori_pari = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    
    # Lettere di controllo corrispondenti al resto (0-25)
    lettere_controllo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    somma = 0
    for i, char in enumerate(codice_fiscale[:15]):
        posizione = i + 1  # posizione in base 1
        if posizione % 2 != 0:  # posizione dispari
            somma += valori_dispari[char]
        else:  # posizione pari
            somma += valori_pari[char]
    
    resto = somma % 26
    return lettere_controllo[resto]


def verifica_codice_fiscale(cf):
    """Verifica formato e carattere di controllo di un codice fiscale."""
    
    if not cf:
        return False, "Il codice fiscale non può essere vuoto."
    
    cf = cf.strip().upper()
    
    # 1. Verifica lunghezza
    if len(cf) != 16:
        return False, f"Lunghezza non valida: {len(cf)} caratteri (attesi 16)."
    
    # 2. Verifica formato generale con regex
    pattern = r'^[A-Z]{6}[0-9]{2}[A-EHLMPRST][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
    if not re.match(pattern, cf):
        return False, "Formato non valido (struttura non conforme allo schema del codice fiscale)."
    
    # 3. Verifica carattere di controllo
    carattere_atteso = calcola_carattere_controllo(cf)
    carattere_effettivo = cf[15]
    
    if carattere_atteso != carattere_effettivo:
        return False, f"Carattere di controllo errato: atteso '{carattere_atteso}', trovato '{carattere_effettivo}'."
    
    return True, "Codice fiscale valido."


# --- Programma principale ---
if __name__ == "__main__":
    dato_input = input("Inserisci il codice fiscale da verificare: ")
    
    valido, messaggio = verifica_codice_fiscale(dato_input)
    
    if valido:
        print(f"✅ {messaggio}")
    else:
        print(f"❌ {messaggio}")