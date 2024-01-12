from typing import List
import enum


class Stages(enum.Enum):
    IDENTITY_PROOFING= enum.auto()
    IDENTITY_VERIFICATION= enum.auto()
    LOCATION= enum.auto()

def get_min_required_stages()-> List[Stages]:
    return [
        Stages.IDENTITY_PROOFING,
        Stages.IDENTITY_VERIFICATION,
        Stages.LOCATION
    ]

def get_required_stages()->  List[Stages]:
    
    stages= get_min_required_stages()

