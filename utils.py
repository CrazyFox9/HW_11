import json


def load_candidates_from_json(path):
    """ возвращает список всех кандидатов """

    with open(path, "r", encoding="UTF-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    """ возвращает одного кандидата по его id """

    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """ возвращает кандидатов по имени """

    candidates = load_candidates_from_json("candidates.json")
    result = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """ возвращает кандидатов по навыку """

    candidates = load_candidates_from_json("candidates.json")
    result = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result

