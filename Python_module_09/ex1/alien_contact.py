try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    raise SystemExit("Pydantic not installed. Run: pip install pydantic")
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def ID_validation(self):
        if self.contact_id[:2] != 'AC':
            raise ValueError("Contact id must start with 'AC'")
        return self

    @model_validator(mode='after')
    def physical_validation(self):
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def telepathic_validation(self):
        if self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        return self

    @model_validator(mode='after')
    def signal_validation(self):
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("Strong signals, messages missing")
        return self


if __name__ == "__main__":
    data = {
        "contact_id": "AC_2004_001",
        "timestamp": "2026-01-27T14:30:00",
        "location": "Area 51, Nevada, USA",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": 'Greeting from Zeta Reticuli',
        "is_verified": True
    }
    invalid_data = {
        "contact_id": "AC_2024_002",
        "timestamp": "2026-01-27T14:30:00",
        "location": "Roswell, New Mexico",
        "contact_type": "telepathic",
        "signal_strength": 5.0,
        "duration_minutes": 30,
        "witness_count": 2,
        "message_received": None,
        "is_verified": False,
    }

    alien_contact = AlienContact.model_validate(data)
    print('Alien Contact Data Validation')
    print('========================================')
    print('Valid contact created:')
    print(f'ID: {alien_contact.contact_id}')
    print(f'Timestamp: {alien_contact.timestamp}')
    print(f'Location: {alien_contact.location}')
    print(f'Contact Type: {alien_contact.contact_type}')
    print(f'Signal Strength: {alien_contact.signal_strength}')
    print(f'Duration: {alien_contact.duration_minutes} minutes')
    print(f'Witness Count: {alien_contact.witness_count}')
    print(f'Message Received: {alien_contact.message_received}')
    print(f'Is Verified: {alien_contact.is_verified}\n')
    print('========================================')

    try:
        AlienContact.model_validate(invalid_data)
    except ValidationError as error:
        print(f"Expected validation error: {error}")
