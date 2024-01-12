import json
from typing import Any, Dict

import pydantic


def test_convertir_response_en_request_listas_de_configuracion() -> None:
    class ConfigListModelInput(pydantic.BaseModel):
        priority: int
        name: str
        pattern: Dict[str, Any]
        configuration: Dict[str, Any]

    class ConfigListModelRequest(pydantic.BaseModel):
        name: str
        pattern: str
        configuration: str

    rule: Dict[str, Any] = {
        "priority": 1,
        "name": "High Risk 80 Activities Pattern",
        "pattern": {
            "economic_activities_ciiu": [
                "722",
                "729",
                "820",
                "2421",
                "2520",
                "3830",
                "4662",
                "990",
                "4665",
                "6614",
                "6615",
                "9200",
                "6810",
            ]
        },
        "configuration": {"score_config": {"weight": 80, "blocker": True}},
    }
    convert_rule = ConfigListModelInput.parse_obj(rule)
    request = ConfigListModelRequest(
        name=convert_rule.name,
        pattern=json.dumps(convert_rule.pattern),
        configuration=json.dumps(convert_rule.configuration),
    )
    print("\n----------------------------------------\n")
    print(request.json())
    print("\n----------------------------------------\n")
    print("Revisar el request por si acaso")


test_convertir_response_en_request_listas_de_configuracion()
