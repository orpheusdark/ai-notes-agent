# 📚 Digital Logic Design: Key Takeaways

> This document summarizes key concepts in digital logic design, covering combinational circuits (adders, subtractors, multipliers, code converters, comparators, multiplexers, demultiplexers, encoders, decoders) and sequential circuits (latches, flip-flops).  It highlights the functionality and differences between various components and their applications.

## 🧮 Combinational Circuits 

*These circuits produce outputs based solely on current inputs.*

###  ➕ Adders & Subtractors

*   **Propagation Delay:**  The time it takes for a signal to propagate through a circuit.  ⏱️
*   **Look-Ahead Carry Adder:**  Faster addition by calculating carries concurrently. Uses more hardware than ripple carry adders. 🚀
*   **BCD Adder:** Adds Binary Coded Decimal (BCD) numbers, handling corrections for sums exceeding 9. 🔢
*   **Half-Subtractor:** Subtracts two single bits; produces difference and borrow. ➖
*   **Full-Subtractor:** Subtracts three bits (two inputs, one borrow-in); produces difference and borrow-out. ➖
*   **Binary Adder-Subtractor:**  Single circuit for both addition and subtraction using 2's complement.  Uses a mode select input. ➕➖

### ✖️ Multipliers & Code Converters

*   **Multipliers:** Perform binary multiplication using partial product summation. 🧮
*   **Code Converters:**  Convert between different coding schemes (e.g., binary to Gray, BCD to Excess-3). 🔄

### ⚖️ Comparators & Multiplexers/Demultiplexers

*   **Comparators (Magnitude Comparators):** Compare two binary numbers; outputs indicate which is greater, less than, or equal.  ➡️⬅️=
*   **Multiplexers (Mux):** Select one of several inputs to a single output line using select lines. 🔀
*   **Demultiplexers (Demux):** Route a single input to one of many outputs based on select lines. 📤

### 🗝️ Encoders & Decoders

*   **Encoders:** Convert multiple inputs to a unique binary code.  🔑
*   **Priority Encoder:**  Outputs the highest priority active input. 👑
*   **Decoders:** Convert binary input to multiple unique outputs (up to 2<sup>n</sup> for n inputs). Generate minterms. ⬇️
*   **BCD to Seven-Segment Decoder:** Converts BCD to drive a seven-segment display. 💡


## 🔄 Sequential Circuits

*These circuits' outputs depend on both current and past inputs.*

### Latch vs. Flip-Flop 

*   **Latches:** Level-sensitive; output changes with input as long as enabled.  ⏳
*   **Flip-Flops:** Edge-triggered; output changes only at clock edges (rising or falling).  The fundamental building blocks of sequential circuits. 🧱

###  Different Types of Flip-Flops

*   **SR Latch/Flip-Flop:** Set (Q=1) and Reset (Q=0) inputs; has an invalid state. 🚫
*   **Gated SR Latch:** Adds an enable input for synchronization. 🚦
*   **D Latch/Flip-Flop (Data/Delay):** Single input 'D'; Q<sub>next</sub> = D; eliminates invalid state. ➡️
*   **Gated D Latch:**  Similar to gated SR latch, but with a single data input.
*   **JK Flip-Flop:** Overcomes the SR latch's invalid state; toggles when J=K=1. 🔄
*   **T Flip-Flop (Toggle):** Toggles output when T input is high; holds state when low. 🗘
*   **Master-Slave Flip-Flops:**  Two latches to prevent race conditions.


✅ **Action Items:**

* Research and compare different adder implementations (ripple carry vs. look-ahead carry).
* Design a simple code converter (e.g., binary to Gray).
* Implement a JK flip-flop using logic gates.

