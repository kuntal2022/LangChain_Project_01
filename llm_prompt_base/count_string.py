
import pydantic , typing
from pydantic import BaseModel,  Field
from typing import Optional, Dict, Any, Literal


class TokenCount(BaseModel):
    output_tokens: int = Field(..., description="Number of tokens in the output")
