from copy import copy

from copy import deepcopy

vridha_favt_food=[

    ["idli","dosa"],
    ["biriyani","chicken"],
    ["chappathi","vegkuruma"]
]

shiva_favt_food=deepcopy(vridha_favt_food)

shiva_favt_food[0][1]="poori"

print(shiva_favt_food)

print(vridha_favt_food)