# VSCodeHelpers

A curated collection of VS Code snippets, templates, and configurations designed to boost developer productivity. Includes ready-to-use code snippets for various programming languages, making it easier for developers to write clean, efficient, and consistent code.

## Features

### Snippets

- **Snippets organized by language**: Support for Java, JavaScript, Python, and Markdown.
- **Specialized categories**: Includes snippets for popular frameworks like Spring (Java), Django (Python), Express (Node.js), and more.
- **Automatic installation**: Python script to install all snippets easily.

### Setting

The folder `settings` contains different VS Code settings files, each designed for a specific programming style or workflow. You can switch between them to adapt the editor to your needs without installing any additional extensions.

## Supported Languages and Frameworks

- **Java**:
  - Core (arrays, classes, collections, exceptions, I/O, switches, advanced functions)
  - JSP (bases, conditionals, CRUD, forms, includes, links, loops, messages, tables)
  - PicoCLI (basics, options, prompts, subcommands)
  - Spring (querys, components, configuration, exceptions, Thymeleaf)

- **JavaScript**:
  - Core (arrays, basics, classes, collections, comments, exceptions, I/O, switches)
  - Node.js (child_process, events, fs, http, os, path, readline)
  - Express
  - React

- **TypeScript**:
  - Core (arrays, basics, classes, collections, comments, exceptions, I/O, switches)
  - React

- **Python**:
  - Core (basics, classes, collections, comments, exceptions, functions, I/O, loops)
  - Click (basics, echo/colors, options, subcommands)
  - Django (and more in development)

- **Markdown**:
  - Formatting, headings, links and media, lists, tables and code

## Installation

### Option 1: Automatic Installation (Recommended)

Run the `add-snippets.py` script to automatically install all snippets in your VS Code configuration:

```bash
python add-snippets.py
```

This script will copy the `.code-snippets` files to the VS Code user snippets folder.

### Option 2: Manual Installation

1. Open VS Code.
2. Go to `File > Preferences > User Snippets`.
3. Select the corresponding language (Java, JavaScript, Python, Markdown).
4. Copy and paste the content of the relevant `.code-snippets` files from the `snippets/` folder in this repository.

## Usage

Once the snippets are installed:

1. Open a file in the desired language in VS Code.
2. Type the snippet prefix (defined in each `.code-snippets` file).
3. Press `Tab` or `Enter` to expand the snippet.

For example, in a Java file, type `class` and press `Tab` to insert a basic class template.

## Project Structure

```
VSCodeHelpers/
├── add-snippets.py          # Script for automatic installation
├── LICENSE                  # Project license
├── README.md                
├── docs/                    # Documentation folder by idiom (en, es)
├── settings/                # Folder with settings for vscode
└── snippets/                # Main snippets folder
    ├── java/
    │   ├── core/
    │   ├── jsp/
    │   ├── picocli/
    │   └── spring/
    ├── javascript/
    │   ├── core/
    │   ├── node/
    │   └── react/
    ├── typecript/
    │   ├── core/
    │   └── react/
    ├── markdown/
    └── python/
        ├── click/
        ├── core/
        └── django/
```

## Contributions

Contributions are welcome! If you want to add new snippets or improve existing ones:

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/new-snippet`).
3. Add your changes and update test files if necessary.
4. Submit a Pull Request.

Make sure to follow the naming conventions and format of the `.code-snippets` files.

## License

This project is under the MIT License. See the `LICENSE` file for more details.

## Author

Created by [Your Name] - Feel free to contact me for questions or suggestions.