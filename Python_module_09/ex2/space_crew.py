try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ModuleNotFoundError:
    raise SystemExit("Pydantic not installed. Run: pip install pydantic")
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def misssion_id_validator(self):
        if self.mission_id[0] != 'M':
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode="after")
    def crew_validation(self) -> "SpaceMission":
        has_leader = any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    @model_validator(mode="after")
    def long_mission_validation(self) -> "SpaceMission":
        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced * 2 < len(self.crew):
                raise ValueError("""
Long missions (> 365 days) need 50% experienced crew (5+ years)""")
        return self


if __name__ == "__main__":
    valid_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2024-06-01T09:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 45,
                "specialization": "Mission Command",
                "years_experience": 20,
            },
            {
                "member_id": "CM002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 38,
                "specialization": "Navigation",
                "years_experience": 10,
            },
            {
                "member_id": "CM003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 29,
                "specialization": "Engineering",
                "years_experience": 4,
            },
        ],
    }

    print("Space Mission Crew Validation")
    print("=========================================")
    mission = SpaceMission.model_validate(valid_data)
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"""
- {member.name} ({member.rank.value}) - {member.specialization}
""")

    print("=========================================")

    invalid_data = dict(valid_data)
    invalid_data["crew"] = [
        {
            "member_id": "CM010",
            "name": "Bob Lee",
            "rank": "officer",
            "age": 33,
            "specialization": "Science",
            "years_experience": 6,
        },
    ]

    try:
        SpaceMission.model_validate(invalid_data)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))
