from phi.knowledge.website import WebsiteKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.assistant import Assistant

from resources import vector_db  # type: ignore

# Create a knowledge base with the seed URLs
knowledge_base = WebsiteKnowledgeBase(
    urls=["https://docs.phidata.com/introduction"],
    # Number of links to follow from the seed URLs
    max_links=10,
    # Table name: ai.website_documents
    vector_db=PgVector2(
        collection="website_documents",
        db_url=vector_db.get_db_connection_local(),
    ),
)
# Load the knowledge base
knowledge_base.load(recreate=False)

# Create an assistant with the knowledge base
assistant = Assistant(
    knowledge_base=knowledge_base,
    add_references_to_prompt=True,
)

# Ask the assistant about the knowledge base
assistant.print_response("How does phidata work?")
