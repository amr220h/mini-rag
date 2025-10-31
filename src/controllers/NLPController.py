
from typing import List
from .BaseController import BaseController
from models.db_schemes import Project,DataChunk
from stores.llm.LLMEnums import DocumentEnum

class NLPController(BaseController):

    def __init__(self,vector_db_client,embedding_client,generation_client):
        super().__init__()

        self.vector_db_client = vector_db_client
        self.embedding_client = embedding_client
        self.generation_client = generation_client


    def create_collection_name(self,project_id:str):
        return f"project_{project_id}_collection".strip()
    
    def reset_vector_db_collection(self,project:Project):
        collection_name = self.create_collection_name(
            project_id=project.project_id
        )
        
        return self.vector_db_client.delete_collection(
                collection_name=collection_name
            )
    def get_vector_db_collection_info(self,project:Project):
        collection_name = self.create_collection_name(
            project_id=project.project_id
        )
        
        collection_info=self.vector_db_client.get_collection_info(
                collection_name=collection_name
            )
        
        return collection_info
    
    def index_into_vector_db(self, project:Project,chunks:List[DataChunk],
                             chunks_ids : List[int],
                             do_reset:bool=False):
        
        #step 1 : get collection name
        collection_name = self.create_collection_name(
            project_id=project.project_id
        )

        #step 2 : mange items

        texts=[c.chunk_text for c in chunks]
        metadata = [c.chunk_metadata for c in chunks] 
    
        vectors = [
            
            self.embedding_client.embed_text(
                text=text,
                document_type = DocumentEnum.DOCUMENT.value )
            for text in texts
        ]


        #step 3 : createe collection if not exists

        _ = self.vector_db_client.create_collection(
            collection_name=collection_name,
            do_reset = do_reset,
            embedding_size = self.embedding_client.embedding_size

        )
        


        #step 4 : insert into vector db

        _ = self.vector_db_client.insert_many(
            collection_name=collection_name,
            texts=texts,
            metadata = metadata,
            vectors = vectors,
            record_ids = chunks_ids

        )

        return True