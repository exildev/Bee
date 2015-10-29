# -*- encoding: utf8 -*-
import requests
import json

AccessToken = '09p6ZzhHaCqsDp5ibO76HXRtIsoa'
Service = "http://store.apicultur.com/api/desambigua/1.0.0"
## La función que llama a las APIs
endhs = ['Fp', 'Fc', 'CC', 'PR0CN000'] #separadores

def apicultur_post(texto):    
    texto = texto.replace(chr(13), ' ')
    texto = texto.replace(chr(10), ' ')
    print texto
    headers = {'content-type': 'application/json', 'Authorization':'Bearer '+ AccessToken}
    response = requests.post(Service, data='{"texto":"' + texto.encode('utf8') +'"}', headers=headers)
    if response.status_code == 200:
        
        results = response.json()
        print '--------------json impresado'+str(results)
        return results
    else:
        print 'respuesta erronea, codigo de error', response.status_code, 'valor devuelto', response
        return False
    #end if
#end def
