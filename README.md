# Local AI Agent with RAG

### Description

This project demonstrates a local Retrieval-Augmented Generation (RAG) agent designed to answer questions about a pizza restaurant's reviews. The agent uses a local Large Language Model (LLM) and a vector database to retrieve relevant information from a set of restaurant reviews before generating a response.

### Features

  * **Local LLM**: The agent uses the `mistral` model, which is run locally via [Ollama](https://ollama.com/).
  * **Retrieval-Augmented Generation (RAG)**: It retrieves relevant restaurant reviews from a vector database to provide context to the LLM.
  * **Vector Database**: The project uses ChromaDB for its vector store, which persists the database locally in a directory named `chrome_langchain_db`.
  * **Data Ingestion**: A CSV file named `realistic_restaurant_reviews.csv` containing sample reviews is automatically processed and converted into a vector database on the first run.
  * **Interactive Command Line Interface**: The agent runs in a `while` loop, allowing continuous questioning until the user chooses to quit.

### Getting Started

#### Prerequisites

Before running the agent, ensure you have the following installed:

  * **Python 3.x**
  * **Ollama**: Download and install Ollama, then pull the required models:
    ```bash
    ollama pull mistral
    ollama pull mxbai-embed-large
    ```

#### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/songyinggoh/Local-AI-Agent-with-RAG.git
    cd Local-AI-Agent-with-RAG
    ```

2.  Install the required Python libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    [cite\_start]The required packages are `langchain`, `langchain-ollama`, and `langchain-chroma`[cite: 1].

### Usage

To start the local AI agent, run the `main.py` script from your terminal.

```bash
python main.py
```

The application will prompt you to ask a question about the restaurant reviews. Type your question and press Enter. To exit the application, type `q` and press Enter.

### Project Structure

  * `main.py`: This is the main script that runs the interactive chat loop. It combines a prompt template, the Ollama LLM, and the vector retriever to answer user questions.
  * `vectorsearchDB.py`: This script handles the creation and management of the ChromaDB vector store. It converts data from the CSV file into vector embeddings and sets up the retriever for RAG.
  * [cite\_start]`requirements.txt`: Lists the Python dependencies required for the project[cite: 1].
  * `realistic_restaurant_reviews.csv`: The dataset of restaurant reviews used to populate the vector database.

### License

(Please choose and add a license file, such as MIT or Apache 2.0, to specify how others can use your project.)
