from enum import Enum
from typing import List, Optional, Set

import pydantic


class EconomicActivity(pydantic.BaseModel):
    name: str
    ciiu: str
    mcc: str
    mcc_visa: Optional[str]
    mcc_mastercard: Optional[str]

class EconomicActivities(Enum):
    ACCOUNTING_AND_ADVICES = EconomicActivity(
        name="Contabilidad / Asesorías",
        ciiu="9412",
        mcc="7392",
        mcc_visa="7311",
        mcc_mastercard="7311",
    )
    AGRICULTURAL = EconomicActivity(
        name="Agricultura / Agropecuaria",
        ciiu="161",
        mcc="763",
        mcc_visa="5912",
        mcc_mastercard="5912",
    )
    ALCOHOLIC_DRINKS = EconomicActivity(
        name="Licores",
        ciiu="4711",
        mcc="5921",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    ARCHITECTURE_AND_ENGINEERING = EconomicActivity(
        name="Arquitectura e ingeniería",
        ciiu="9412",
        mcc="8999",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    AUTOMOTIVE = EconomicActivity(
        name="Automotriz y autopartes",
        ciiu="4520",
        mcc="7538",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    AUTO_PARTS_SHOP = EconomicActivity(
        name="Auto partes",
        ciiu="4530",
        mcc="5533",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    BABY_SISTER_SERVICE = EconomicActivity(
        name="Servicio de niñera",
        ciiu="9700",
        mcc="8351",
        mcc_visa="8220",
        mcc_mastercard="8220",
    )
    BAR_CLUB_DISCO = EconomicActivity(
        name="Bar / Club / Discoteca",
        ciiu="5630",
        mcc="5813",
        mcc_visa="",
        mcc_mastercard="",
    )
    BEAUTY_DISTRIBUTOR = EconomicActivity(
        name="Distribuidora",
        ciiu="9602",
        mcc="5977",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    BEAUTY_SALOON = EconomicActivity(
        name="Salón de belleza",
        ciiu="9602",
        mcc="7230",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    BOOKS_AND_STATIONERY = EconomicActivity(
        name="Libros / Papelería",
        ciiu="4761",
        mcc="5942",
        mcc_visa="5942",
        mcc_mastercard="5942",
    )
    BUILDING_MATERIALS = EconomicActivity(
        name="Materiales de construcción",
        ciiu="4752",
        mcc="5251",
        mcc_visa="5815",
        mcc_mastercard="5310",
    )
    BUS = EconomicActivity(
        name="Bus",
        ciiu="5021",
        mcc="4131",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    BUTCHER_SHOP = EconomicActivity(
        name="Carnicería",
        ciiu="4723",
        mcc="5422",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    BYCICLES_AND_ACCESSORIES_SALE = EconomicActivity(
        name="Venta de bicicletas y accesorios",
        ciiu="4762",
        mcc="5940",
        mcc_visa="5994",
        mcc_mastercard="5310",
    )
    CATALOG_SALE = EconomicActivity(
        name="Venta por catálogo",
        ciiu="4792",
        mcc="5963",
        mcc_visa="5994",
        mcc_mastercard="5310",
    )
    CARPENTRY = EconomicActivity(
        name="Carpintería",
        ciiu="3110",
        mcc="1520",
        mcc_visa="1731",
        mcc_mastercard="5211",
    )
    CARWASH = EconomicActivity(
        name="Autolavado",
        ciiu="4520",
        mcc="5532",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    CATERING = EconomicActivity(
        name="Catering",
        ciiu="5621",
        mcc="5811",
        mcc_visa="5814",
        mcc_mastercard="5814",
    )
    CHURCH = EconomicActivity(
        name="Iglesias",
        ciiu="9491",
        mcc="8999",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    CLOTHES_AND_ACCESSORIES = EconomicActivity(
        name="Ropa / Accesorios",
        ciiu="4771",
        mcc="5651",
        mcc_visa="5949",
        mcc_mastercard="5949",
    )
    COACHING = EconomicActivity(
        name="Coach",
        ciiu="8692",
        mcc="7392",
        mcc_visa="7311",
        mcc_mastercard="7311",
    )
    CRYSTALWARE_SHOP = EconomicActivity(
        name="Vidrieras",
        ciiu="2310",
        mcc="5231",
        mcc_visa="5231",
        mcc_mastercard="5310",
    )
    CULTURAL_CENTERS = EconomicActivity(
        name="Centros culturales",
        ciiu="8553",
        mcc="5971",
        mcc_visa="5231",
        mcc_mastercard="5310",
    )
    DELIVERY = EconomicActivity(
        name="Domicilios",
        ciiu="5320",
        mcc="4789",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    DESIGN_AND_PHOTOGRAPHY = EconomicActivity(
        name="Diseño / Fotografía",
        ciiu="7420",
        mcc="5946",
        mcc_visa="5816",
        mcc_mastercard="5310",
    )
    DIAPER_SHOP = EconomicActivity(
        name="Pañalera infantil",
        ciiu="1313",
        mcc="5651",
        mcc_visa="5949",
        mcc_mastercard="5949",
    )
    ENTERTAINMENT = EconomicActivity(
        name="Entretenimiento",
        ciiu="9329",
        mcc="5816",
        mcc_visa="5816",
        mcc_mastercard="5310",
    )
    EROTIC_SHOP = EconomicActivity(
        name="Erotismo / Lencería",
        ciiu="4769",
        mcc="7296",
        mcc_visa="5949",
        mcc_mastercard="5949",
    )
    EVENTS_AND_FESTIVALS = EconomicActivity(
        name="Eventos / Festivales",
        ciiu="9007",
        mcc="7929",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    FASHION_SHOE_STORE = EconomicActivity(
        name="Moda / Zapatería",
        ciiu="4772",
        mcc="5661",
        mcc_visa="5949",
        mcc_mastercard="5949",
    )
    FAST_FOOD = EconomicActivity(
        name="Comida rápida",
        ciiu="5611",
        mcc="5814",
        mcc_visa="5814",
        mcc_mastercard="5814",
    )
    FLORIST = EconomicActivity(
        name="Floristería",
        ciiu="4759",
        mcc="5992",
        mcc_visa="5992",
        mcc_mastercard="5310",
    )
    FOOD_PRODUCTS = EconomicActivity(
        name="Productos alimenticios",
        ciiu="1089",
        mcc="5411",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    FOUNDATION = EconomicActivity(
        name="Fundación",
        ciiu="9499",
        mcc="8398",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    FURNITURE_AND_DECORATION = EconomicActivity(
        name="Muebles / Decoración",
        ciiu="7410",
        mcc="5712",
        mcc_visa="5211",
        mcc_mastercard="5211",
    )
    GROCERY_AND_MARKET = EconomicActivity(
        name="Abarrotes / Mercado",
        ciiu="4781",
        mcc="5411",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    GYM = EconomicActivity(
        name="Gimnasio",
        ciiu="9311",
        mcc="7298",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    HANDICRAFTS = EconomicActivity(
        name="Artesanías",
        ciiu="4759",
        mcc="5932",
        mcc_visa="5932",
        mcc_mastercard="5310",
    )
    HARDWARE_SHOP = EconomicActivity(
        name="Ferretería",
        ciiu="4663",
        mcc="5251",
        mcc_visa="5815",
        mcc_mastercard="5310",
    )
    HEALTH_FOOD_STORE = EconomicActivity(
        name="ienda naturista",
        ciiu="4773",
        mcc="5912",
        mcc_visa="5912",
        mcc_mastercard="5912",
    )
    HOTELS = EconomicActivity(
        name="Hoteles",
        ciiu="5511",
        mcc="7011",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    HOSTALS = EconomicActivity(
        name="Hostales",
        ciiu="5511",
        mcc="7011",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    HOME_APPLIANCE = EconomicActivity(
        name="Electrodomésticos",
        ciiu="4754",
        mcc="5722",
        mcc_visa="5211",
        mcc_mastercard="5211",
    )
    HOME_ELEMENTS = EconomicActivity(
        name="Elementos del hogar",
        ciiu="4755",
        mcc="5719",
        mcc_visa="5211",
        mcc_mastercard="5211",
    )
    HOUSE_CLEANING = EconomicActivity(
        name="Limpieza del hogar",
        ciiu="8121",
        mcc="7349",
        mcc_visa="5949",
        mcc_mastercard="5949",
    )
    ICE_CREAM_SHOP = EconomicActivity(
        name="Heladería",
        ciiu="5619",
        mcc="5499",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    INSURANCE = EconomicActivity(
        name="Seguros",
        ciiu="6511",
        mcc="6300",
        mcc_visa="6300",
        mcc_mastercard="6300",
    )
    INDEPENDENT_MASSAGE_THERAPIST = EconomicActivity(
        name="Masajista independiente",
        ciiu="9609",
        mcc="7298",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    INDEPENDENT_STYLIST = EconomicActivity(
        name="Estilista independiente",
        ciiu="9602",
        mcc="7230",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    INTERNET_CAFE = EconomicActivity(
        name="Café internet",
        ciiu="6190",
        mcc="5943",
        mcc_visa="5942",
        mcc_mastercard="5942",
    )
    INDEPENDENT_CONTRACTOR = EconomicActivity(
        name="Contratista independiente",
        ciiu="4390",
        mcc="1520",
        mcc_visa="1731",
        mcc_mastercard="5211",
    )
    JEWELRY = EconomicActivity(
        name="Joyería",
        ciiu="3210",
        mcc="5944",
        mcc_visa="5815",
        mcc_mastercard="5310",
    )
    KINDERGARDEN = EconomicActivity(
        name="Jardín infantil",
        ciiu="8512",
        mcc="8351",
        mcc_visa="8220",
        mcc_mastercard="8220",
    )
    LABORATORY = EconomicActivity(
        name="Laboratorio",
        ciiu="8610",
        mcc="8071",
        mcc_visa="8021",
        mcc_mastercard="8011",
    )
    LOCKSMITH_SHOP = EconomicActivity(
        name="Cerrajería",
        ciiu="8020",
        mcc="5251",
        mcc_visa="5815",
        mcc_mastercard="5310",
    )
    LODGING = EconomicActivity(
        name="Hospedaje",
        ciiu="5512",
        mcc="7011",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    LOGISTICS = EconomicActivity(
        name="Logística",
        ciiu="5229",
        mcc="7349",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    LOCATIVE_REPAIRS = EconomicActivity(
        name="Reparaciones locativas",
        ciiu="9529",
        mcc="1520",
        mcc_visa="1731",
        mcc_mastercard="5211",
    )
    LAUNDRY = EconomicActivity(
        name="Lavandería",
        ciiu="9601",
        mcc="7210",
        mcc_visa="5949",
        mcc_mastercard="5949",
    )
    MACHINERY = EconomicActivity(
        name="Maquinaria",
        ciiu="3312",
        mcc="5211",
        mcc_visa="5211",
        mcc_mastercard="5211",
    )
    MEDICAL_EQUIPMENTS = EconomicActivity(
        name="Equipos médicos",
        ciiu="3250",
        mcc="5975",
        mcc_visa="5816",
        mcc_mastercard="5310",
    )
    MEDICINE_AND_DENTISTRY = EconomicActivity(
        name="Medicina / Odontología",
        ciiu="8622",
        mcc="8011",
        mcc_visa="8011",
        mcc_mastercard="8011",
    )
    MESSENGER_SERVICE = EconomicActivity(
        name="Mensajería",
        ciiu="5320",
        mcc="4215",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    MOTELS = EconomicActivity(
        name="Moteles",
        ciiu="5530",
        mcc="7033",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    MOTOTAXI = EconomicActivity(
        name="Mototaxi",
        ciiu="5229",
        mcc="4111",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    MISCELANEOUS_SHOP = EconomicActivity(
        name="Misceláneas",
        ciiu="4759",
        mcc="5331",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    MORTUARY = EconomicActivity(
        name="Funeraria",
        ciiu="5530",
        mcc="7261",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    MOVING = EconomicActivity(
        name="Mudanza",
        ciiu="4923",
        mcc="4214",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    NEW_VEHICLES_SALE = EconomicActivity(
        name="Venta de vehículos nuevos",
        ciiu="4511",
        mcc="5511",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    OPTICS = EconomicActivity(
        name="Óptica",
        ciiu="3250",
        mcc="8043",
        mcc_visa="8011",
        mcc_mastercard="8011",
    )

    OTHER_BEAUTY_AND_CARE = EconomicActivity(
        name="Otro",
        ciiu="9603",
        mcc="7299",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )

    OTHER_EDUCATION = EconomicActivity(
        name="Otro",
        ciiu="8559",
        mcc="8299",
        mcc_visa="8220",
        mcc_mastercard="8220",
    )
    OTHER_FOOD_AND_DRINKS = EconomicActivity(
        name="Otro",
        ciiu="1081",
        mcc="5499",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    OTHER_REPAIR_AND_CLEANING = EconomicActivity(
        name="Otro",
        ciiu="1081",
        mcc="7349",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    OTHER_RETAIL_TRADE = EconomicActivity(
        name="Otro",
        ciiu="4774",
        mcc="5331",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    OTHER_SERVICES = EconomicActivity(
        name="Otro",
        ciiu="6399",
        mcc="8999",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    OTHER_TRANSPORT = EconomicActivity(
        name="Otro",
        ciiu="1081",
        mcc="5499",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    OTHER_TOURISM_AND_ENTERTAINMENT = EconomicActivity(
        name="Otro",
        ciiu="5519",
        mcc="7999",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    PASTRY_AND_BAKERY = EconomicActivity(
        name="Repostería / Panadería",
        ciiu="5613",
        mcc="5462",
        mcc_visa="5441",
        mcc_mastercard="5441",
    )
    PETS = EconomicActivity(
        name="Mascotas", ciiu="4759", mcc="5995", mcc_visa="5912", mcc_mastercard="5912"
    )
    PHARMACY = EconomicActivity(
        name="Farmacia", ciiu="4773", mcc="5912", mcc_visa="5912", mcc_mastercard="5912"
    )
    PERFUMERY = EconomicActivity(
        name="Perfumería",
        ciiu="4773",
        mcc="5977",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    PERSONAL_TRAINER = EconomicActivity(
        name="Entrenador personal",
        ciiu="8552",
        mcc="7999",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    PROPERTY_RENT = EconomicActivity(
        name="Alquiler/arriendo de propiedades",
        ciiu="9499",
        mcc="7349",
        mcc_visa="8398",
        mcc_mastercard="8398",
    )
    REAL_STATE = EconomicActivity(
        name="Inmobiliarias",
        ciiu="6820",
        mcc="6513",
        mcc_visa="6300",
        mcc_mastercard="6300",
    )
    RENT_A_CAR = EconomicActivity(
        name="Alquiler de vehículos",
        ciiu="7710",
        mcc="7512",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    RECREATION_AND_SPORTS_CENTER = EconomicActivity(
        name="Centro de recreación y deporte",
        ciiu="9319",
        mcc="7997",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    RESELLER = EconomicActivity(
        name="Revendedor",
        ciiu="5963",
        mcc="4792",
        mcc_visa="5994",
        mcc_mastercard="5310",
    )
    RESTAURANT_CAFE = EconomicActivity(
        name="Restaurante / Café",
        ciiu="5611",
        mcc="5812",
        mcc_visa="5814",
        mcc_mastercard="5814",
    )
    SECURITY_ELEMENTS = EconomicActivity(
        name="Elementos de seguridad",
        ciiu="4719",
        mcc="5975",
        mcc_visa="5816",
        mcc_mastercard="5310",
    )
    SUPPLIES = EconomicActivity(
        name="Insumos", ciiu="2593", mcc="5311", mcc_visa="5441", mcc_mastercard="5441"
    )
    SPA = EconomicActivity(
        name="Spa", ciiu="9609", mcc="7298", mcc_visa="7230", mcc_mastercard="7298"
    )
    SUPPLEMENTS = EconomicActivity(
        name="Suplementos",
        ciiu="1104",
        mcc="5912",
        mcc_visa="5912",
        mcc_mastercard="5912",
    )
    SCHOOLS = EconomicActivity(
        name="Colegios", ciiu="8521", mcc="8220", mcc_visa="8220", mcc_mastercard="8220"
    )
    SPECIAL_SERVICE = EconomicActivity(
        name="Servicio especial",
        ciiu="4921",
        mcc="4111",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    SPORTS_STORE = EconomicActivity(
        name="Tienda de deportes",
        ciiu="4762",
        mcc="5941",
        mcc_visa="5815",
        mcc_mastercard="5310",
    )
    SURPRISE_BREAKFAST = EconomicActivity(
        name="Desayunos sorpresa",
        ciiu="5629",
        mcc="5811",
        mcc_visa="5814",
        mcc_mastercard="5814",
    )
    TUTOR_AND_TEACHERS = EconomicActivity(
        name="Tutor / Profesor",
        ciiu="8522",
        mcc="7392",
        mcc_visa="7311",
        mcc_mastercard="7311",
    )
    TATOO = EconomicActivity(
        name="Centro de tatuajes",
        ciiu="9602",
        mcc="7298",
        mcc_visa="7230",
        mcc_mastercard="7298",
    )
    TECHNOLOGY_RETAIL_TRADE = EconomicActivity(
        name="Tecnología",
        ciiu="4741",
        mcc="4812",
        mcc_visa="4814",
        mcc_mastercard="5310",
    )
    TOY_STORE = EconomicActivity(
        name="Juguetería / Piñatería",
        ciiu="4769",
        mcc="5945",
        mcc_visa="5816",
        mcc_mastercard="5310",
    )
    TEXTILES = EconomicActivity(
        name="Textiles", ciiu="7940", mcc="5949", mcc_visa="5949", mcc_mastercard="5949"
    )
    THERAPIES = EconomicActivity(
        name="Terapias", ciiu="8692", mcc="7298", mcc_visa="7230", mcc_mastercard="7298"
    )
    TECHNOLOGY_AND_SOFTWARE = EconomicActivity(
        name="Tecnología y software",
        ciiu="6201",
        mcc="7392",
        mcc_visa="7311",
        mcc_mastercard="7311",
    )
    TOURISM = EconomicActivity(
        name="Turismo", ciiu="4722", mcc="4722", mcc_visa="7999", mcc_mastercard="7999"
    )
    TRAVEL_AGENCY = EconomicActivity(
        name="Agencia de Viajes",
        ciiu="7911",
        mcc="4722",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    TOURIST_PACKAGES = EconomicActivity(
        name="Paquetes turísticos",
        ciiu="7912",
        mcc="4722",
        mcc_visa="7999",
        mcc_mastercard="7999",
    )
    TOURS = EconomicActivity(
        name="Tours", ciiu="5229", mcc="4722", mcc_visa="7999", mcc_mastercard="7999"
    )
    TAXI = EconomicActivity(
        name="Taxi", ciiu="4921", mcc="4111", mcc_visa="4111", mcc_mastercard="4111"
    )
    USED_VEHICLES_SALE = EconomicActivity(
        name="Venta de vehículos usados",
        ciiu="4512",
        mcc="5511",
        mcc_visa="4111",
        mcc_mastercard="4111",
    )
    VETERINARY = EconomicActivity(
        name="Veterinaria",
        ciiu="7500",
        mcc="742",
        mcc_visa="5912",
        mcc_mastercard="5912",
    )

    VIDEO_GAMES = EconomicActivity(
        name="Videojuegos",
        ciiu="4741",
        mcc="5945",
        mcc_visa="5816",
        mcc_mastercard="5310",
    )
    WEB_DEVELOPMENT = EconomicActivity(
        name="Desarrollo web",
        ciiu="6201",
        mcc="7311",
        mcc_visa="7311",
        mcc_mastercard="7311",
    )
    WORKSHOPS_AND_COURSES = EconomicActivity(
        name="Talleres / Cursos / Capacitaciones",
        ciiu="8523",
        mcc="8299",
        mcc_visa="8220",
        mcc_mastercard="8220",
    )

class RiskAssessedPersonScoreCalculated(pydantic.BaseModel):
    name: Optional[str]
    economic_activities: Optional[
        Set[EconomicActivities]
    ] = pydantic.Field(default_factory=set)
    total_score: int
    stage_score: int

class RiskAssessedPerson(pydantic.BaseModel):
    name: Optional[str]
    economic_activities: List[EconomicActivity] = pydantic.Field(
        default_factory=list
    )

risk_assessed_person: RiskAssessedPerson= RiskAssessedPerson(
    name="Pepe", 
    economic_activities=[
    EconomicActivity(
        name="Contabilidad / Asesorías",
        ciiu="9412",
        mcc="7392",
        mcc_visa="7311",
        mcc_mastercard="7311",
    )
])

    
economic_activities_map = {
    (
        economy_activity.value.name, 
        economy_activity.value.ciiu, 
        economy_activity.value.mcc, 
        economy_activity.value.mcc_visa, 
        economy_activity.value.mcc_mastercard
    ): economy_activity
    for economy_activity in EconomicActivities
}


def _map_economic_activities(activities: List[EconomicActivity])-> Optional[Set[EconomicActivities]]:
    converted_activities: Set[EconomicActivities] = set()
    for activity in activities:
        key = (activity.name, activity.ciiu, activity.mcc, activity.mcc_visa, activity.mcc_mastercard)
        if key in economic_activities_map:
            converted_activities.add(economic_activities_map[key])
    
    if len(converted_activities) <= 0:
        return None

    return converted_activities



score_calculated= RiskAssessedPersonScoreCalculated(
            name=risk_assessed_person.name,
            economic_activities=_map_economic_activities(risk_assessed_person.economic_activities),
            total_score=100,
            stage_score=100
        )



print(score_calculated.json(exclude_unset=True))