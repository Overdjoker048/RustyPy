# 🚀 Python → Rust Optimizing Compiler

## 📌 Overview

This project is a **hybrid Python → Rust compiler and optimizer** whose goal is to **reduce binary size**, **increase performance**, and **produce a native executable** from Python code.

The core idea is simple but ambitious:
- analyze Python source code,
- remove everything unnecessary,
- **automatically replace performance-critical parts with highly optimized Rust implementations**,
- generate a **final native binary**.

The project currently focuses on **Python**, with a gradual transition toward a **Rust-based core**.

---

## 🎯 Main Goals

- 🔥 Aggressive Python code optimization
- 🧹 Removal of useless tokens and dead code
- ⚙️ Compile-time evaluation of deterministic variables
- 🦀 Targeted replacement of Python code with Rust
- 📦 Native executable generation
- 🧠 Conditional Rust code inclusion (only when required)

---

## 🔁 Code Parts Rewritten in Rust

Some critical components are **systematically rewritten in Rust**, while keeping a **strictly identical API on the Python side**.

### 🔧 Direct Function Replacement

Optimized functions are **not wrapped**:

- they are **injected directly at their usage sites**
- replacement happens at the **AST / IR level**
- no runtime indirection cost

👉 The generated code directly calls the final Rust implementation.

---

### 1️⃣ Types

- Python built-in types are **reimplemented in Rust**
- Identical behavior and semantics
- Low-level optimized implementation

#### 🧠 Memory & Performance Optimization

- reduced memory footprint
- improved cache locality
- faster primitive operations

#### 🔁 Builtins Replacement

Rust types **replace existing `builtins` types at compile time**.

👉 Any usage in the codebase is transparently redirected to the optimized version, **without modifying user code**.

---

### 2️⃣ Console Input / Output

All I/O operations are redirected to Rust implementations:

- `stdin`
- `stdout`
- `stderr`

Optimizations include:
- preformatted output
- reduced syscall overhead
- optional complete removal of console output

---

### 3️⃣ File Type (Rust + mmap)

A **new internal file type** is introduced:

- implemented in Rust
- uses **`mmap`** for memory access
- extremely fast read/write operations

#### 🧵 Asynchronous / Threaded Operations

File modifications can be:
- executed on a **dedicated thread**
- scheduled asynchronously
- synchronized only when results are required

👉 Goal: **no slowdown of the main execution flow**, even during heavy disk operations.

---

### 4️⃣ Performance Timing Decorator

A dedicated decorator allows execution time measurement:

```python
@timeit
def my_function():
    ...
```

- high-precision timing (Rust-based)
- minimal overhead
- useful for benchmarking and profiling

---

## 🧠 Compiler Optimizations

### 🔹 Compile-Time Variable Evaluation

Any variable that can be evaluated at compile time is replaced:

```python
a = 10 * 5  # becomes a = 50
```

- constant propagation
- runtime computation removal

---

### 🔹 Console Output Preformatting

```python
print("value:", x)
```

➡️ becomes a preformatted output when possible.

---

### 🔹 Conditional Rust Imports

Rust modules are included **only if required**:

| Feature used | Rust module imported |
|-------------|---------------------|
| `print` only | stdout |
| `input` | stdin |
| `print + errors` | stdout + stderr |

👉 Zero unnecessary dependencies.

---

### 🔹 Python Import Optimization

- removal of unused imports
- strict minimum dependency inclusion
- import merging and reduction

---

## ⚙️ Compiler Options

### 📄 Keep docstrings

```bash
-doc
```

- preserves docstrings
- useful for debugging and introspection

---

### 🧪 Keep assertions

```bash
-asr
```

- keeps `assert` statements
- otherwise they are removed

---

### 🖥️ GUI Mode (No Console)

```bash
-gui
```

- no terminal window
- `stdin`, `stdout`, `stderr` become no-op calls
- known console-related methods are removed

---

### 📦 Output executable name

```bash
-o my_program
```

---

### 🎨 Executable icon

```bash
-icon icon.png
```

---

### 🗑️ Disable Garbage Collector

```bash
-nogc
```

- disables Python GC
- intended for fully controlled memory usage

---

## 📤 Output

- Optimized native executable
- Reduced size
- Increased performance
- Minimal dependencies

---

## 📊 Performance Gain Estimation

Actual gains depend heavily on the program profile, but realistic estimates can be made.

| Optimization | Estimated gain |
|-------------|----------------|
| Dead code / token removal | +5 to +15% |
| Constant precomputation | +10 to +30% |
| Import optimization | +5 to +10% |
| Rust-based console I/O | +20 to +60% |
| Output preformatting | +10 to +25% |
| `mmap` file access | +30 to +200% |
| GC disabling (when applicable) | +5 to +20% |

### ⚡ Global Estimated Speedup

Depending on the program type:

- **Simple scripts / I/O bound**: **+20 to +50%**
- **Heavy I/O applications**: **+50 to +150%**
- **CPU-bound but optimizable code**: **+30 to +80%**

> ⚠️ Maximum gains are achieved when the code is mostly deterministic and weakly dynamic.

---

## 🛠️ Project Status

- ✅ Python analysis
- ✅ Base optimizations
- 🚧 Rust backend in progress
- 🚧 Executable generation

---

## 📜 Philosophy

> *"Write Python as usual, run it as if it were Rust."*

---

## 🤝 Contributions

Ideas, benchmarks, and feedback are welcome.

---

## 📄 License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
