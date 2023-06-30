from typing import Optional, Dict, Any
import json
import pydantic
import pydash

class Value(pydantic.BaseModel):
    authenticationType: str 
    date: str

class Protocol(pydantic.BaseModel):
    name: str 

class Answer(pydantic.BaseModel):
    id: str
    protocol: Protocol
    value: Value
    _type: str

class SeonResponseA(pydantic.BaseModel):
    id: str
    answer: Optional[Dict[str, Any]]

class SeonResponseB(pydantic.BaseModel):
    id: str
    answer: Answer

class SeonResponseC(pydantic.BaseModel):
    id: str
    answer: Optional[Dict[str, Any]]
    test: Optional[str]

class SeonWrapper(pydantic.BaseModel):
    item: SeonResponseA

payload= {
            "answer": {
                "id": "3b25e3ed-5d48-4f99-af61-0d5db9e3b18e",
                "protocol": {
                    "name": "THREEDS",
                    "version": "2.1.0",
                    "network": "Test",
                    "challengePreference": "NO_PREFERENCE",
                    "simulation": True,
                    "_type": "test",
                },
                "value": {
                    "authenticationType": "CHALLENGE",
                    "authenticationId": {
                        "authenticationIdType": "dsTransId",
                        "value": "e8286d62-006e-413e-ad3b-328503b14e71",
                        "_type": "test",
                    },
                    "date": "20-04-2023",
                    "status": "FAILED",
                    "extension": {
                        "authenticationType": "THREEDS_V2",
                        "threeDSServerTransID": "3b25e3ed-5d48-4f99-af61-0d5db9e3b18e",
                        "dsTransID": "e8286d62-006e-413e-ad3b-328503b14e71",
                        "acsTransID": "54feb2ac-9666-4ce3-86e5-d8f947cebd87",
                        "transStatusReason": "01",
                        "_type": "test",
                    },
                    "reason": {
                        "code": "CARD_AUTHENTICATION_FAILED",
                        "_type": "test",
                    },
                    "_type": "Test",
                },
                "_type": "test",
            },
            "id": "test",
}

payload_json= json.dumps(payload)
#print(payload_json)
#print(type(payload_json))

payload_json_response= json.loads(payload_json)
#print(payload_json_response)
#print(type(payload_json_response))

response_a= SeonResponseA.parse_obj(payload_json_response)
response_b= SeonResponseB.parse_obj(payload_json_response)

print(type(response_a))
print(response_a.json(indent=3))

print(type(response_b))
print(response_b.json(indent=3))



response_c= SeonResponseC(
    id=response_a.id,
    test="This is a test",
    answer=pydash.pick(response_a.answer, ["value.date", "_type", "protocol"])
)

test: Dict[str, Any]= {
    "answer": "test"
}

#print(response_a.answer)
#print(test)

#print(pydash.pick(response_a.answer, ["answer"]))
#print(pydash.pick(test, ["answer"]))

print(type(response_c))
print(response_c.json(indent=3))

wrapper= SeonWrapper(
    item=response_a
)

response_c_v2= SeonResponseC(
    id=wrapper.item.id,
    test="This is a test",
    answer=pydash.pick(wrapper.item.__dict__, ["answer.value.date", "answer._type", "answer.protocol", "id"])
)


print(response_c_v2.json(indent=3))