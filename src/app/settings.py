from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    app_name: str = Field(default="python-for-linear-algebra")
    debug: bool = Field(default=False)
