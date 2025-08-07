# 📚 Key Takeaways from Digital Logic Design Notes

> This document summarizes key concepts in digital logic design, including number systems (binary, octal, hexadecimal), number representation (signed and unsigned), binary codes (weighted and non-weighted), error detection and correction, Boolean algebra, and logic gates.  It highlights important concepts and provides a structured overview for easy reference.

## 🔢 Number Systems and Representation 🧮

### Octal and Hexadecimal 
*   Octal: Base-8 number system (digits 0-7).
*   Hexadecimal: Base-16 number system (digits 0-9, A-F).
*   Conversions:  Efficient conversion between binary, octal, and hexadecimal is crucial for digital system understanding.

### Binary Number Complements 🔄
*   **Radix Complement (r's complement):**  For binary, this is the 2's complement. Used for subtraction simplification.
*   **Diminished Radix Complement ((r-1)'s complement):** For binary, this is the 1's complement.  Also used in subtraction and logical manipulation.

### Signed Number Representation ➕➖
*   **Sign Magnitude:** A sign bit (0 for positive, 1 for negative) precedes the magnitude.
*   **1's Complement:** Positive numbers are in true binary; negative numbers are the 1's complement of their magnitude.
*   **2's Complement:** Positive numbers are in true binary; negative numbers are the 2's complement of their magnitude.  *Simpler arithmetic operations (subtraction via addition)*.


## 💡 Binary Codes  🤖

### Weighted Binary Codes
*   **BCD (Binary Coded Decimal):**  Each bit has a weight (8421).  Sequential and useful for arithmetic, but less efficient than pure binary.
*   **BCD Addition:** Add 4-bit groups; add '0110' if the sum exceeds 9 or a carry is generated.

### Non-Weighted Codes
*   **Excess-3 (XS-3):**  8421 BCD code + 0011 (3). Self-complementing and sequential.
*   **Gray Code:** Successive codewords differ by only one bit. Useful in instrumentation to minimize errors during transitions.

### Alphanumeric Codes
*   **ASCII (American Standard Code for Information Interchange):**  Encodes characters, numbers, and symbols.
*   **EBCDIC (Extended Binary-Coded Decimal Interchange Code):** Another alphanumeric code.


## 🚫 Error Detection and Correction Codes 🔎

### Error-Detecting Codes
*   **Parity Bits:** Added bits to detect errors (odd or even parity).  Detects single-bit errors, but not multiple errors.

### Error-Correcting Codes
*   **Hamming Code:** Uses multiple parity bits to detect and locate single-bit errors, enabling correction.


## 🧮 Boolean Algebra and Logic Gates ⚙️

### Logic Levels
*   Two levels:  Logical high (1) and logical low (0), represented by voltage ranges.

### Logic Gates
*   **Basic Gates:** AND, OR, NOT (Inverter).
*   **Universal Gates:** NAND, NOR (Can implement any basic gate).
*   **Other Gates:** XOR (Exclusive-OR), XNOR (Exclusive-NOR).


