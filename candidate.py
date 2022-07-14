from dataclasses import dataclass, field


@dataclass(slots=True)
class Candidate:

    id: int
    name: str
    picture: str
    position: str
    gender: str
    age: int
    skills: str
    skills_list: list | None = field(default=None, init=False)

    def __post_init__(self):
        self.skills_list = self.skills.lower().split(', ')
