def search_info(es, res):
    print('#### Query Res')
    print(res)
    # validate 
    if res['hits']['total']['value'] > 0:
        response = {"body": { "options": "ejemplo" }, "status": {"code": "U0000","description": "Se ejecuto la consulta con exito"}}
    else:
        print("## DATA NOT FOUND | searchQuery ")
        response = {"status": {"code": "U0002","description": "No se encontro la busqueda, favor verifique"}, "body": { "options": [] }}
    return response