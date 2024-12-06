
# QuickRAG Q&A API

QuickRAG is a lightweight Retrieval-Augmented Generation (RAG) application built using OpenAI's GPT models. It combines document retrieval and generative AI to create answers based on the provided textual data. This project demonstrates the integration of FAISS for vector search, LangChain utilities for document processing, and FastAPI for a simple API interface.

## Features
- **Document Retrieval**: Uses FAISS for efficient similarity searches over text documents.
- **Answer Generation**: Leverages OpenAI's GPT model to generate context-aware answers.
- **API Integration**: Provides a FastAPI endpoint for seamless interaction with the application.

## Installation

### Prerequisites
- Python 3.9+
- An OpenAI API key (set as an environment variable)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/adilabbass/QuickDocAssistant-RapidRag
   cd QuickDocAssistant-RapidRag
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set the OpenAI API key in your environment:
   ```bash
   export OPEN_AI_API_KEY=your_openai_api_key  # On Windows: set OPENAI_API_KEY=your_openai_api_key
   ```

5. Place your text documents in the `data/` folder.

6. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

### API Endpoints
- **Root Endpoint**:
  - URL: `/`
  - Method: `GET`
  - Description: Provides a welcome message.

- **Question Answering Endpoint**:
  - URL: `/ask/`
  - Method: `POST`
  - Parameters: 
    - `query` (string): The question to be answered.
  - Description: Retrieves relevant documents and generates an answer.
  - Example:
    ```bash
    curl -X POST "http://127.0.0.1:8000/ask/" -H "Content-Type: application/json" -d '{"query": "What is QuickRAG?"}'
    ```

### Sample Response
```json
{
    "query": "What is QuickRAG?",
    "context": "QuickRAG is a lightweight Retrieval-Augmented Generation application...",
    "answer": "QuickRAG is an application that combines document retrieval with generative AI."
}
```

## File Structure
```
app/
    ├── main.py          # FastAPI application entry point
    ├── retriever.py     # Handles document retrieval and vector search
    ├── generator.py     # Generates answers using OpenAI GPT models
├── requirements.txt # Python dependencies
├── data/            # Folder containing text documents for retrieval
├── .env 
```

## Key Technologies
- **LangChain**: For document loading and splitting.
- **FAISS**: To create a vector store for fast document retrieval.
- **OpenAI API**: To generate human-like answers.
- **FastAPI**: To build and expose the API.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenAI for their GPT models.
- LangChain community for document processing tools.
- FAISS for efficient similarity search.

## Contact
For any queries, reach out via:
- GitHub: [@adilabbass](https://github.com/adilabbass/QuickDocAssistant-RapidRag)
- Email: madil.abbass@gmail.com