<img alt="Awlise: An awmazing API wrapper for Alise" src=".github/assets/banner.svg" width="100%" />

_This library **is not** affiliated with [Alise](https://alise.net/) in any way._

## What is "Alise" ?

Alise is a platform designed for managing bookings, reservations, and other administrative tasks for various establishments. It provides a web-based interface for users to interact with its services. Awlise aims to simplify and enhance the interaction with Alise's API by providing a Python-based wrapper.

## Installation

Install Awlise via pip:

```bash
pip install awlise
```

## Usage

```python
from awlise import login_credentials

# Example usage
session = asyncio.run(
    login_credentials(site_id="example_site", username="user", password="password")
)
```

## Implementations

You're currently on the `index` branch.

Since we're implementing this library in different programming languages, we have a branch for each of them.

| [JS/TS](https://github.com/LiterateInk/Awlise/tree/js) | Rust | Python | Swift |
| :----------------------------------------------------: | :--: | :----: | :---: |
|                         Kotlin                         |  C#  |  Dart  |       |

## Contributing

We welcome contributions! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE.md](LICENSE.md) file for details.
