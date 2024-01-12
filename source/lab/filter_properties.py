values = [
    "bg.ws.numerounico",
    "bg.ws.oficina",
    "bg.ws.terminal",
    "bg.ws.rol",
    "bg.ws.aplicacion",
    "bg.ws.canal",
    "bg.ws.nodo",
    "bg.ws.origen",
    "bg.ws.usuario",
    "bg.ws.moneda",
    "bg.ws.creditcard",
    "bg.ws.transferaccount",
    "bg.ws.thirdPartySaving",
    "bg.ws.colector",
    "bg.ws.topup",
    "bg.ws.colectorNoAfil",
    "bg.ws.iddevice",
    "bg.ws.deviceCode",
    "bg.ws.flag.login",
    "bg.ws.flag.collector",
    "bg.ws.flag.geolocalization",
    "bg.ws.flag.geolocalizationPilotEnabled",
    "bg.ws.perfil",
    "bg.ws.changepass",
    "bg.ws.origenlogin",
    "bg.ws.loanStatusCode",
    "bg.ws.loanDescription",
    "bg.ws.loanStatusDescription",
    "logging.level.org.springframework.ws.client.MessageTracing.sent",
    "logging.level.org.springframework.ws.client.MessageTracing.received",
    "bg.ws.flag.isOmniOnline",
    "bg.ws.flag.holiday",
    "bg.ws.flag.latiniaOnline",
    "bg.ws.flag.isAffiliation",
    "bg.ws.catalogue.creditCard",
    "bg.ws.colector.codeMetro",
    "bg.ws.flag.disableDynamoDb",
    "bg.ws.flag.yappyThirdPartyNotification",
    "bg.ws.flag.refreshAllPnsToken",
    "bg.ws.flag.isPiloto",
    "bg.ws.flag.disablePtP",
    "bg.ws.catalogue.profiles",
    "bg.ws.flag.isFriendFamilyYappyMarket",
    "bg.ws.flag.isFriendFamily",
    "bg.ws.flag.isFriendFamilyYappy",
    "bg.ws.accountopen.useropener",
    "bg.ws.accountopen.roleuseropener",
    "bg.ws.flag.isFriendFamilyCommercial",
    "bg.ws.flag.isEnabledCommercial",
    "bg.ws.flag.isFriendFamilyNotifications",
    "bg.ws.flag.isWebUpdateDataPersonal",
    "bg.ws.flag.enableUpdateDataPersonal",
    "bg.ws.flag.isEnableYappy",
    "bg.ws.flag.incomeSupportUpdtEnabled",
    "bg.ws.flag.personalInfoUpdtEnabled",
    "bg.ws.updatedata.appVersions",
    "bg.ws.flag.omniOnlineTc",
    "bg.ws.flag.isEnableCreateAccount",
    "bg.ws.flag.isAvailableYappyUrl",
    "bg.ws.url.yappymarket",
    "bg.ws.flag.isEnableContactSync",
    "bg.ws.flag.isYappyPlusEnabled",
    "bg.ws.flag.isValidateSecurityQuestion",
    "bg.ws.apiconnect.personal",
    "bg.ws.apiconnect.market",
    "bg.ws.apiconnect.commercial",
    "bg.ws.flag.isYappyAffiliationEnable",
    "bg.ws.flag.updateDeliveryMethodEnabled",
    "bg.ws.flag.facialBiometricsTable",
    "bg.ws.flag.facialBiometricsKeyName"
]

required_hash_set=set(values)

total_hash_set= set()

with open("application.properties") as properties:
    for line in properties:

        property=line

        if not property.startswith("#") and property.strip() !="":
            property= (line.split(sep="=")[0]).strip()
        
        if property in required_hash_set or property.startswith("#"):
            print(line)
            if not property.startswith("#"):
                total_hash_set.add(property)

            

print(len(required_hash_set))
print(len(total_hash_set))
