value: str = "IdentityProofingStageUpdated"

array = value[0].lower() + "".join(
    character if character.islower() else f"-{character.lower()}"
    for character in value[1:]
)
print(array)
