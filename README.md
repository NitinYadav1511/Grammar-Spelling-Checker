# Grammar and Spelling Checker

## Overview

The **Grammar and Spelling Checker** is a web application designed to help users identify and correct spelling and grammar errors in their text. Built using Python with Flask as the web framework, it provides an intuitive interface where users can input text or upload files for analysis.

## Features

- **Spell Check**: Identifies and corrects spelling mistakes in the input text
- **Grammar Check**: Detects grammatical errors and provides correction suggestions
- **User-Friendly Interface**: Clean, responsive design built with Bootstrap
- **File Upload Support**: Process text files directly through file upload
- **Real-time Processing**: Instant feedback on text corrections
- **Export Options**: Download corrected text in various formats

## Project Structure

```
Grammar-Spelling-Checker/
├── templates/
│   └── index.html
├── model.py
├── app.py
└── README.md
```

## Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework
- **TextBlob**: Natural language processing and spell checking
- **LanguageTool**: Advanced grammar checking
- **Bootstrap**: Frontend styling and responsiveness
- **jQuery**: Frontend interactivity

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NitinYadav1511/Grammar-Spelling-Checker.git
   cd Grammar-Spelling-Checker
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`

## Usage

1. **Text Input**:
   - Type or paste your text into the main text area
   - Click "Check Text" to process
   - Review suggested corrections highlighted in the results

2. **File Upload**:
   - Click "Choose File" to select a text document
   - Click "Upload and Check" to process
   - Download the corrected version when ready

3. **Export Options**:
   - Choose your preferred format (TXT, DOCX, PDF)
   - Click "Export" to download the corrected text

## API Reference

The application exposes the following API endpoints:

- `POST /api/check`: Check text for spelling and grammar errors
  ```json
  {
    "text": "Your text here"
  }
  ```

- `POST /api/file`: Upload and check a file
  ```
  multipart/form-data
  file: your_text_file.txt
  ```

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request

## Configuration

Configure the application by modifying `config.py`:

```python
class Config:
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'txt', 'doc', 'docx'}
    LANGUAGE_TOOL_PATH = 'path/to/languagetool'
```


## Error Handling

The application includes comprehensive error handling for:
- Invalid file types
- File size limits
- Processing timeouts
- API rate limiting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- TextBlob library for natural language processing
- LanguageTool for grammar checking capabilities
- Flask community for excellent documentation
- Contributors who have helped improve this project
