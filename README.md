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

```text
your_project/
├── Core/
│   ├── __init__.py
│   └── identifiers.py