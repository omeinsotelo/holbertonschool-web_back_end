#! / usr / bin / env python3
"" "
¿Dónde puedo aprender Python?
"" "
desde  pymongo  importar  MongoClient

if  __name__  ==  "__main__" :
    cliente  =  MongoClient ( 'mongodb: //127.0.0.1: 27017' )
    nginx_collection  =  cliente . registros . nginx
    número  =  colección_nginx . contar ()
    number_get  =  nginx_collection . buscar ({ "método" : "OBTENER" }). contar ()
    número_post  =  nginx_collection . buscar ({ "método" : "POST" }). contar ()
    number_put  =  nginx_collection . encontrar ({ "método" : "PUT" }). contar ()
    parche_número  =  colección_nginx . buscar ({ "método" : "PATCH" }). contar ()
    number_delete  =  nginx_collection . buscar ({ "método" : "BORRAR" }). contar ()
    number_status  =  nginx_collection . encontrar (
        { "método" : "OBTENER" , "ruta" : "/ estado" }). contar ()
    number_ips  =  nginx_collection . agregado ([
            { "$ grupo" : { "_id" : "$ ip" , "total" : { "$ suma" : 1 }}},
            { "$ sort" : { "total" : - 1 }},
            { "$ límite" : 10 }
        ])

    imprimir ( "{} registros" . formato ( número ))
    print ( "Métodos:" )
    print ( " \ t método GET: {}" . formato ( number_get ))
    print ( " \ t método POST: {}" . formato ( número_post ))
    print ( " \ t método PUT: {}" . formato ( number_put ))
    print ( " \ t método PATCH: {}" . formato ( number_patch ))
    print ( " \ t método DELETE: {}" . formato ( number_delete ))
    print ( "{} verificación de estado" . formato ( number_status ))
    imprimir ( "direcciones IP:" )
    para  ips  en  number_ips :
        print ( " \ t {}: {}" . formato ( ips . get ( "_id" ), ips . get ( "total" )))
