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
                "priority": 2,
                "name": "PARTIAL_AML Configuration",
                "pattern": {
                    "stage": "PARTIAL_AML"
                },
                "configuration": {
                    "stages_config": [
                        {
                            "stage": "PARTIAL_AML",
                            "stage_action": {
                                "action": "EXECUTE_PROVIDER",
                                "provider": "LEXIS_NEXIS"
                            },
                            "is_active": False,
                            "sources": [
                                "International,Consolidated Sanctions List",
                                "Security Council",
                                "US-U.S. Office of Foreign Asset Control (OFAC)",
                                "EU-European Union List",
                                "UK-Her Majesty's Treasury Financial Sanctions",
                                "CO-Departamento Administrativo de Seguridad",
                                "CO-Autorregulador del Mercado de Valores",
                                "CO-Armada Nacional de Colombia",
                                "CO-Colombian Air force",
                                "CO-Corte Suprema de Justicia, República de Colombia",
                                "CO-Ejército Nacional de Colombia",
                                "CO-Fiscalía General de la Nación",
                                "CO- Ministerio de Ambiente y Desarrollo Sostenible",
                                "CO-Ministerio de Educacion - Mineducacion",
                                "CO-Ministerio de Transporte",
                                "CO-Ministry of Mines and Energy",
                                "CO-Policía Nacional de Colombia",
                                "CO-Procuraduría General de la Nación",
                                "CO-Superintendencia de Industria y Comercio",
                                "CO- Superintendencia de la Economia Solidaria",
                                "CO-Superintendencia de Puertos y Transporte",
                                "CO-Superintendencia de Sociedades",
                                "CO-Superintendencia Financiera de Colombia",
                                "International,Website",
                                "PEP"
                            ],
                            "stage_additional_config": None
                        }
                    ]
                }
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