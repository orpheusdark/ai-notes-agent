# 📚 Key Takeaways from Chapter 2: Symmetric & Asymmetric Encryption

> This document summarizes Chapter 2 on symmetric and asymmetric encryption, detailing core concepts, various encryption algorithms (Caesar, Playfair, Vigenere, Vernam, Hill ciphers), and transposition techniques like Rail-Fence, along with an introduction to steganography.  The notes highlight key definitions, algorithms, and examples for each technique.

## 🧠 Core Concepts 🔑

### 🔒 Symmetric vs. Asymmetric Encryption

*   **Symmetric Encryption:**  Uses the *same* key for both encryption and decryption.  Sender and receiver must share this *private key*.
    *   *Example*:  Playfair cipher.
    *   **Advantages:** Fast and efficient.
    *   **Disadvantages:** Key distribution can be challenging.
*   **Asymmetric Encryption:** Uses *two* different keys: a *public key* for encryption and a *private key* for decryption.
    *   **Advantages:** Secure key distribution.
    *   **Disadvantages:** Slower than symmetric encryption.


## 🧮 Encryption Algorithms/Ciphers ⚙️

### 🔤 Basic Terms

*   **Plaintext:** Readable message.
*   **Ciphertext:** Unreadable, encrypted message.
*   **Encryption:** Process of converting plaintext to ciphertext.
*   **Decryption:** Process of converting ciphertext back to plaintext.
*   **Substitution Cipher:** Replaces characters with other characters.
*   **Transposition Cipher:** Changes the position of characters.

### 📜 Caesar Cipher 📜

*   A type of *substitution cipher*.
*   Shifts each letter a fixed number of positions down the alphabet.
*   Example:  `COLLEGE` becomes `FROOHJH` (shift of 3).
*   Algorithm:
    1.  Assign numbers (0-25) to A-Z.
    2.  Add the key (e.g., 3) to each number.
    3.  Convert the resulting numbers back to letters.

### 🎲 Playfair Cipher 🎲

*   *Symmetric key cryptography*.
*   Uses a 5x5 matrix with a keyword.
*   Encryption Steps:
    1.  Create and populate the 5x5 matrix (I/J share a cell).
    2.  Divide plaintext into pairs. Add 'X' if needed to make pairs.
    3.  Apply rules based on character positions in the matrix (same row, same column, or different row & column).
*Example Matrix (Keyword: PLAYFAIR):
```
P L A Y F
I/J R C H E
B D G K M
N O Q S T
U V W X Z
```

### 🔑 Vigenere Cipher 🔑

*   *Symmetric encryption*.
*   Uses a Vigenere square (table) and a keyword.
*   Keyword is repeated to match the length of the plaintext.
*   Encryption involves finding the intersection of the plaintext letter (column) and the keyword letter (row) in the Vigenere square.

### 🔒 Vernam Cipher (One-Time Pad) 🔒

*   Uses a *non-repeating* random key (ciphertext) as long as the plaintext.
*   The key is *never reused*.
*   Algorithm:
    1.  Assign numbers (0-25) to A-Z for both plaintext and key.
    2.  Add corresponding numbers.
    3.  Subtract 26 if the sum exceeds 25.
    4.  Convert the result back to letters.


### 🧮 Hill Cipher 🧮

*   *Polyalphabetic substitution cipher*.
*   Uses matrix multiplication.
*   Algorithm:
    1.  Convert plaintext letters to numbers (0-25).
    2.  Form a matrix from the numbers.
    3.  Multiply the plaintext matrix by a key matrix (same size).
    4.  Take the modulo 26 of the resulting matrix.
    5.  Convert the numbers back to letters.


## 🔀 Transposition Techniques 🔀

### 🚧 Rail-Fence Cipher 🚧

*   A simple *transposition technique*.
*   Plaintext is written diagonally across multiple "rails".
*   Ciphertext is read row by row.


## 🤫 Steganography 🕵️‍♀️

*   Hiding a secret message within another message or medium (e.g., image).
*   Example:  Replacing the least significant bits of an image's bytes with the secret message.


✅ **Action Items:**

*   Further research on asymmetric encryption algorithms (RSA, ECC).
*   Implement the described ciphers in code (Python recommended).
*   Explore more advanced steganography techniques.

