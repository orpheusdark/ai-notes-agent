# 📚 Key Takeaways from .NET Programming Question Bank

> This document summarizes key concepts and answers from a .NET Programming question bank, covering topics from .NET architecture to exception handling and ADO.NET.  It provides a structured overview for quick reference and review.

## 🧠 Core Concepts 

### .NET Architecture 

*   **Components:** Common Language Runtime (CLR), Framework Class Library (FCL), Common Type System (CTS), Common Language Specification (CLS).
*   **Managed vs. Unmanaged Code:** Managed code runs under the CLR; unmanaged code runs outside the .NET framework.
*   **CLR Role:**  Manages execution, memory, security, and JIT compilation.
    *   *Automatic memory management*
    *   *Code access security*
    *   *Garbage collection*
    *   *JIT compilation*
*   **CTS:** Catalog of .NET types (value types and reference types).
*   **FCL:** Provides system services (I/O, database access, etc.).  Organized into nested namespaces (e.g., `System.IO`).

### C# Data Types & Operators

*   **Data Types:** Value types (int, char, etc.), reference types (string, objects), pointer types.
*   **Type Casting:** Implicit (widening) and explicit (narrowing) conversions.
*   **Boxing/Unboxing:** Converting between value types and reference types (`object`).
*   **Operators:** Arithmetic, relational, logical, bitwise, assignment.  Operator precedence matters!

### Control Structures & Arrays

*   **Conditional Statements:** `if`, `if-else`, nested `if`, `switch`, nested `switch`.
*   **Loops:** `while`, `for`, `do-while`.
*   **Arrays:** Jagged arrays (arrays of arrays with varying lengths).  Example: `int[][] jaggedArray = new int[4][];`

### Methods & Access Modifiers

*   **Method Overloading:** Defining multiple methods with the same name but different parameters.
*   **`ref` and `out` Keywords:** Used for passing parameters by reference.  `ref` requires initialization before passing; `out` requires initialization before returning.
*   **Access Modifiers:** `public`, `private`, `protected`, `internal`, `protected internal`.  Control access to class members.

### Exception Handling

*   **Structured Exception Handling:** `try-catch-finally` blocks.
*   **Exception Classes:**  `Exception` is the base class.  Many subclasses exist for specific error types (e.g., `DivideByZeroException`, `FileNotFoundException`).

### Windows Forms

*   **Message Boxes:** Display messages to the user; various button combinations available (`MessageBox.Show()`).
*   **Input Boxes:** Get user input (`Interaction.InputBox()`).
*   **Dialog Boxes:** Font, Color, Open File, Save File, Print dialogs.  These provide standard UI elements for common user actions.
*   **Context Menus & Menu Strips:** Create menus and context menus for user interaction.

### ADO.NET

*   **Architecture:** Data provider (connection, command, data reader, data adapter) and DataSet.  Provides a structured way to interact with databases.
*   **Data Provider:**  Connects to the database, executes commands, and retrieves data.
*   **DataSet:** An in-memory representation of data; can hold data from multiple tables.


## 💻 Code Examples (Snippets)

**Boxing/Unboxing:**

```csharp
int val = 2019;
object o = val; // Boxing
int x = (int)o; // Unboxing
```

**Jagged Array:**

```csharp
int[][] jaggedArray = new int[3][];
jaggedArray[0] = new int[] { 1, 2 };
jaggedArray[1] = new int[] { 3, 4, 5 };
jaggedArray[2] = new int[] { 6 };
```

**Message Box:**

```csharp
MessageBox.Show("Hello, world!");
```


## ✅ Action Items

*   Review all code examples and try implementing them.
*   Research and understand the differences between connected and disconnected architectures in ADO.NET.
*   Explore additional .NET features not covered in this summary.


