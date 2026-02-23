# Core Identifiers 🚀

Centralize service  and robust to manage unique identifier (UUID) inside Python ecosistem

This component was designed to be **agnostic**, allow multiple project (APIs , microservices) using the same logic to generate IDs, ensuring consistency

## ✨ Functionalities

- **UUID v4**: Generate IDs totally random for session and transactions
- **UUID v4 Hex**: Compact version (without dashes) ideal for file names or url key
- **UUID v5**: Generate IDs based *Namespace* and *Input* (ex: email). The same input generate always the same ID - perfect to avoid duplicates in the database like MongoDB or MySQL
- **Static Typing**: Fully compatible with `mypy` and modern IDEs (Type Hints).

## 🛠️ How to use

### 1. Project structure
To use this component, simply copy the `Core` folder to the root of your project:

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

```
Test coverage

| Test | Description |
|------|-------------|
| `test_uuid4_is_string` | Checks that UUID v4 returns a string |
| `test_uuid4_valid_format` | Validates UUID v4 format |
| `test_uuid4_hex_no_dashes` | Checks that hex version has no dashes |
| `test_uuid5_deterministic` | Same input always returns same ID |
| `test_uuid5_different_inputs` | Different inputs return different IDs |
```

## 📁 Project Structure
```text
core-identity/
├── UUID/
│   ├── __init__.py
│   └── identifiers.py
├── tests/
│   ├── __init__.py
│   └── test_identifiers.py
├── README.md
└── LICENSE