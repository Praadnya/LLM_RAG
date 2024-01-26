### RAG Pipeline:

**Components:**

- **Reader (`reader.py`):** Responsible for reading documents, extracting their content, and providing it for further processing.
- **Adapter (`adapter.py`):** Segments the document content into smaller chunks to facilitate processing and analysis.
- **Embedder (`embedder.py`):** Embeds the chunks of text into numerical vectors, typically using pre-trained language models.
- **Vector Database (`vector_database.py`):** Stores the embeddings of document chunks in a database, enabling efficient retrieval based on queries.
- **LLM(`llm.py`):** GPT4All model used with gptj as backend to generate the response.

  testpdf is an example document to run the RAG pipeline.

  ### test.py as the below flow:
  **Pipeline Execution:**

- The pipeline begins with the **`reader`** loading a document and extracting its content.
- The **`adapter`** then segments the content into chunks.
- The **`embedder`** processes each chunk to generate embeddings, representing the semantic content of the text.
- The embeddings, along with metadata, are stored in the **`vector_database`** for later retrieval.

**Querying and Retrieval:**

- A sample query (e.g., a question) is embedded using the same **`embedder`**.
- The **`vector_database`** is queried with the embedded query to retrieve the most relevant chunks.
- The retrieved chunks can serve as potential answers or relevant information.

**Language Model (LLM - Language Model):**

- The **`llm.py`** module integrates a language model (e.g., GPT-4) to generate responses based on a given context and query.
- It uses the processed document chunks as context and a user-provided query to generate responses.

**Configurations:**

- Configuration parameters such as **`chunk_size`**, **`chunk_overlap`**, and model paths are used to customize the behavior of each component.
- Embedding models and backend configurations(gptj) are specified for the language model.

**Prompt Template:**

- A **`PromptTemplate`** is used to format the input prompt for GPT-J, including placeholders for the context and query. This template aids in constructing a coherent prompt for the model.
  
