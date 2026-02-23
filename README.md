# Core Identifiers 🚀


![Tests](https://github.com/BrunoBarroso09/core-identity/actions/workflows/tests.yml/badge.svg)

Centralized and robust service to manage unique identifiers (UUID) inside the Python ecosystem.

This component was designed to be **agnostic**, allowing multiple projects (APIs, microservices) 
to use the same logic to generate IDs, ensuring consistency.

## ✨ Functionalities

- **UUID v4**: Generates totally random IDs for sessions and transactions
- **UUID v4 Hex**: Compact version (without dashes), ideal for file names or URL keys
- **UUID v5**: Generates IDs based on *Namespace* and *Input* (e.g. email). The same input always generates the same ID — perfect to avoid duplicates in databases like MongoDB or MySQL
- **Static Typing**: Fully compatible with `mypy` and modern IDEs (Type Hints)

## 🛠️ How to use

### 1. Project structure
Copy the `UUID` folder to the root of your project:
```text
your_project/
├── UUID/
│   ├── __init__.py
│   └── identifier.py
```

### 2. Usage examples
```python
from UUID.identifier import Identifier

# Random UUID v4
print(Identifier.v4())    # "550e8400-e29b-41d4-a716-446655440000"

# UUID v4 Hex (no dashes)
print(Identifier.hex())   # "550e8400e29b41d4a716446655440000"

# Deterministic UUID v5 (same input = same ID)
print(Identifier.v5("user@email.com"))  # always the same
```

## 🧪 Running Tests

Install pytest:
```bash
pip install pytest
```

Run all tests:
```bash
pytest tests/
```

Expected output:
```
tests/test_identifiers.py .....   5 passed in 0.02s
```

### Test coverage

| Test | Description |
|------|-------------|
| `test_uuid4_is_string` | Checks that UUID v4 returns a string |
| `test_uuid4_format_valido` | Validates UUID v4 format |
| `test_uuid4_hex` | Checks that hex version has no dashes |
| `test_uuid5_deterministic` | Same input always returns same ID |
| `test_uuid_v5_inputs_different` | Different inputs return different IDs |

## 📁 Project Structure
```text
core-identity/
├── UUID/
│   ├── __init__.py
│   └── identifier.py
├── tests/
│   ├── __init__.py
│   └── test_identifiers.py
├── README.md
└── LICENSE
```