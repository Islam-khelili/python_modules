from datetime import date
try:
    from pydantic import BaseModel, Field, ValidationError
except ModuleNotFoundError:
    raise SystemExit("Pydantic not installed. Run: pip install pydantic")


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: date = Field(...)
    is_operational: bool = Field(default=True)
    note: str | None = Field(default=None, max_length=200)


data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2026-01-27",
        "is_operational": True
}


if __name__ == "__main__":
    space_station = SpaceStation.model_validate(data)
    print('Space Station Data Validation')
    print('========================================')
    print('Valid station created:')
    print(f'ID: {space_station.station_id}')
    print(f'Name: {space_station.name}')
    print(f'Crew: {space_station.crew_size} people')
    print(f'Power: {space_station.power_level}%')
    print(f'Oxygen: {space_station.oxygen_level}%')
    print(f'Status: {space_station.is_operational}\n')
    print('========================================')

    try:
        SpaceStation.model_validate(50)
    except ValidationError as e:
        print(f"Expected validation error: {e}")
