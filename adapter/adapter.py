import json
import sys
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


class adapter:
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 10,
        seperator: str = "\n\n",
        verbose: bool = True,
    ) -> str:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.seperator = seperator
        self.verboseprint = print if verbose else lambda *a: None

        self.verboseprint(
            f"ADAPTER: Adapter initialised successfully with the following configuration: chunk_size = {self.chunk_size}  chunk_overlap = {self.chunk_overlap}"
        )

    def _document_dictionary_to_lang_chain_document(self, text: str) -> Document:
        return Document(page_content=text, metadata={})

    def get_chunks(self, doc: list[str]):
        chunk_list = []

        for d in doc:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
            )
            document = self._document_dictionary_to_lang_chain_document(
                d,
            )
            texts = text_splitter.split_documents([document])

            for text in texts:
                chunk_list.append(text.page_content)

        self.verboseprint(
            f"ADAPTER: Document chunking successful. No of chunks = {len(chunk_list)}"
        )
        return chunk_list
