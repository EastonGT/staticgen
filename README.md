# StaticGen: Static Site Generator

A Python-based tool developed as part of the Boot.dev curriculum. This project explores the fundamentals of how static sites are built by automating the conversion of Markdown files into a functional HTML website.

---

## 🚀 Overview
StaticGen recursively processes a directory of Markdown files, applies structured HTML templates, and generates a static output ready for web hosting.

### Key Objectives
* **Markdown Parsing**: Converting raw text and syntax into valid HTML blocks.
* **Template Integration**: Wrapping content in consistent layouts using a "base" HTML file.
* **Automation**: Handling complex file synchronization and public asset copying.

---

## 🛠️ Build Concepts
* **Python 3.12+**: Utilizing modern Python features for file I/O and string manipulation.
* **Testing**: Using test programs for each class to check for bugs and functionality before moving onto next Class.
* **Regex**: Using Regex with inline_markdown class to extract images and links.
* **CLI & Bash**: Programmed to run using bash files to execute the main.py file and build into the src folder from content.

---

## 📂 Project Structure
* `src/`: Contains the core logic for the generator.
* `content/`: Raw Markdown source files. Structured into subpages via folders. 
* `template.html`: The master HTML layout for the site.
* `static/`: CSS, images, and other non-markdown assets used throughout the site.
* `docs/`: The target directory where the final site is generated and displayed on GitHub Pages.

---

## ⚙️ Setup & Usage
### 1. Prerequisites
Ensure you have **Python 3.10** or higher installed on your system. You can check your version by running:
```bash
python3 --version
```

### 2. Clone Files To Local Machine
```
git clone [https://github.com/EastonGT/staticgen.git](https://github.com/EastonGT/staticgen.git)
cd staticgen
```

### 3. Build the Site
The project uses a shell script to automate the build process. This script clears the existing docs/ directory, copies over static assets, and generates the HTML files from your Markdown source:

```
./build.sh
```
*Note: If you receive a "permission denied" error, make the script executable first with ```chmod +x build.sh```.*

### 4. Local Development & Preview
To view your generated site locally, you can use Python's built-in HTTP server:

```
cd docs && python3 -m http.server 8888
```
Then, open your browser and navigate to `http://localhost:8888`.

### 5. Running Tests
This project follows a test-driven approach. To run the full suite of unit tests for the Markdown parsers and HTML generators:

```
./test.sh
```
Using ```chmod +x test.sh``` to enable it.



