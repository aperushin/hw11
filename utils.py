import json
from candidate import Candidate
from config import CANDIDATES_FILE


def load_json(filename: str) -> dict | list:
    """Load data from a JSON file"""
    with open(filename, encoding='utf8') as f:
        data = json.load(f)
    return data


def load_candidates(filename: str) -> list[Candidate]:
    """
    Load candidates from a JSON file, creating Candidate instances
    :param filename: Path to JSON file
    """
    candidates = load_json(filename)
    result = []
    for candidate in candidates:
        result.append(Candidate(**candidate))
    return result


def get_candidate(candidate_id: int) -> Candidate | None:
    """Get candidate by id"""
    candidates: list[Candidate] = load_candidates(CANDIDATES_FILE)
    for candidate in candidates:
        if candidate.id == candidate_id:
            return candidate
    return None


def get_candidates_by_name(name: str) -> list[Candidate]:
    """Get candidates by name"""
    candidates: list[Candidate] = load_candidates(CANDIDATES_FILE)
    result = [c for c in candidates if name.lower() in c.name.lower()]
    return result


def get_candidates_by_skill(skill) -> list[Candidate]:
    """Get candidates by skill"""
    candidates = load_candidates(CANDIDATES_FILE)
    result = [c for c in candidates if skill.lower() in c.skills_list]
    return result
