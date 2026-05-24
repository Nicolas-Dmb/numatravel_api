from typing import Optional

from pydantic import BaseModel, Field


class Contact(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str = Field(alias="email")
    message: str = Field(alias="message")
    phone: Optional[str] = Field(default=None, alias="phone")
    priceRange: str = Field(alias="priceRange")
    departureRange: str = Field(alias="departureRange")
    destination: str = Field(alias="destination")
    meta_event_id: Optional[str] = Field(default=None, alias="metaEventId")
    fbp: Optional[str] = Field(default=None, alias="fbp")
    fbc: Optional[str] = Field(default=None, alias="fbc")
