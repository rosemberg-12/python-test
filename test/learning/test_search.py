import source.working.search as suject

def test_search_info_test_ok_response():

    res={
        "hits":{
            "total":{
                "value": 23
            }
        }
    }

    respuesta= suject.search_info("lo que sea", res=res)

    assert "status" in respuesta
    assert "code" in respuesta["status"]
    assert respuesta["status"]["code"]=="U0000"


def test_search_info_test_fail_response():

    res={
        "hits":{
            "total":{
                "value": -50
            }
        }
    }

    respuesta= suject.search_info("lo que sea", res=res)

    assert "status" in respuesta
    assert "code" in respuesta["status"]
    assert respuesta["status"]["code"]=="U0002"

