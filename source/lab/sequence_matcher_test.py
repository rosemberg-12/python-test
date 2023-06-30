from difflib import SequenceMatcher

tusdatos_nit= " abcd"

person_nit= "abcd abcd"


matcher=SequenceMatcher(lambda x: x==" ", tusdatos_nit, person_nit)

print(matcher.ratio())


matcher=SequenceMatcher(None, tusdatos_nit, person_nit)

print(matcher.ratio())
