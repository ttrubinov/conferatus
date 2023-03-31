from dataclasses import dataclass

@dataclass(frozen=True)
class UserDefinedParameters:
    port: str
    filename: str
    person: str

    frequency: int
    batchSize: int
    angle: int