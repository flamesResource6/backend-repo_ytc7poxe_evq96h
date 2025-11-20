"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (you can keep or remove if not needed)
class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Electrician business inquiry schema
class Inquiry(BaseModel):
    """
    Customer inquiries and quote requests
    Collection name: "inquiry"
    """
    name: str = Field(..., description="Customer full name")
    email: Optional[EmailStr] = Field(None, description="Customer email address")
    phone: Optional[str] = Field(None, description="Customer phone number")
    service: Literal[
        "General Maintenance",
        "Rewires",
        "Smoke Alarms",
        "Security & CCTV",
        "EV Chargers",
        "Lighting",
        "Other",
    ] = Field(..., description="Requested service type")
    message: Optional[str] = Field(None, description="Additional details from customer")
    source: Optional[str] = Field(None, description="Lead source, e.g., website form")
    status: Literal["new", "contacted", "scheduled", "completed", "archived"] = Field(
        "new", description="Inquiry status"
    )
