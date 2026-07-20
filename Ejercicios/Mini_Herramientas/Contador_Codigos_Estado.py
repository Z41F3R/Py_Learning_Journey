#!/usr/bin/env python3

codigos = {
    # 1xx: Informativos
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    
    # 2xx: Exitosos
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    
    # 3xx: Redirecciones
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    
    # 4xx: Errores del Cliente
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    
    # 5xx: Errores del Servidor
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required"
}


def contar_codigos_estado(ruta):
    estados = {}
    try:
        with open(ruta) as logs:
            for linea_de_texto in logs:
                for palabra in linea_de_texto.split():
                    try:
                        valor_obtenido = int(palabra)
                        if valor_obtenido in codigos:
                            codigo_representado = f"{valor_obtenido} {codigos[valor_obtenido]}"
                            if codigo_representado not in estados:
                                estados[codigo_representado] = 1
                            else:
                                estados[codigo_representado] += 1
                        else:
                            break
                    except ValueError:
                        continue
        return estados
    except FileNotFoundError:
        return "Archivo no encontrado"

result = contar_codigos_estado("logs.txt")
print(result)

#===============================================================================
# Esta herramienta fue desarrollada para practicar la lectura de archivos de   =
# registro (logs) y la extracción de datos de manera nativa. El objetivo       =
# principal es prescindir de librerías o herramientas externas para comprender =
# a fondo la lógica subyacente ("bajo nivel"). Al implementar estos algoritmos =
# de forma manual, se busca entender qué procesos ejecutan las librerías       =
# modernas por detrás y cómo estructurar esta lógica desde cero.               =
#===============================================================================
