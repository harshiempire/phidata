from typing import Optional, Any
from pydantic import BaseModel, ConfigDict


class Message(BaseModel):
    """Pydantic model for holding LLM messages"""

    # The role of the messages author.
    # One of system, user, assistant, or function.
    role: str
    # The contents of the message. content is required for all messages,
    # and may be null for assistant messages with function calls.
    content: str
    # The name of the author of this message. name is required if role is function,
    # and it should be the name of the function whose response is in the content.
    # May contain a-z, A-Z, 0-9, and underscores, with a maximum length of 64 characters.
    name: Optional[str] = None
    # The name and arguments of a function that should be called, as generated by the model.
    function_call: Optional[Any] = None


class ConversationRow(BaseModel):
    """Pydantic model for holding LLM conversations"""

    # The ID of this conversation.
    id: Optional[int] = None
    # The ID of the user who is participating in this conversation.
    user_id: str
    # The persona of the user who is participating in this conversation.
    user_persona: Optional[str] = None
    # The data of the user who is participating in this conversation.
    user_data: Optional[Any] = None
    # True if this conversation is active.
    is_active: Optional[bool] = None
    # The chat history with the user participating in this conversation.
    chat_history: Optional[Any] = None
    # The history with the LLM participating in this conversation.
    llm_history: Optional[Any] = None
    # The usage data of this conversation.
    usage_data: Optional[Any] = None
    # The timestamp of when this conversation was created.
    created_at: Optional[str] = None
    # The timestamp of when this conversation was last updated.
    updated_at: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)