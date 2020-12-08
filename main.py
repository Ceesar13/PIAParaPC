#!/usr/bin/env python3
import ACifrado, BMetadata, CNmap, DCorreo, FSocket, GAPI, HHash
if __name__ == '__main__':
    print("Nombre: César Alejandro Rodríguez Pérez.\nMatricula: 1734223.\nGrupo: 064.\n\n")
    opc=0
    while opc<8:
        opc=int(input("MENU PRINCIPAL\n1: Cifrado.\n2: Metadata de Imagenes.\n3: Nmap.\n4: Enviar un correo.\n5: Socket.\n6: API´s\n7: HASH\n8: Salir\n\n\t\tSeleccione una opcion: "))
        if opc==1:
            print("Imprtante: Revisar el documento Archivo,txt, ahí hay un mini diccionario ya que el dictEsp me daba error para leerlo")
            obj1=ACifrado.Cifrado()
        if opc==2:
            print("IMPORTANTE: La ruta de las imagenes se puede encontrar en la misma carpeta donde se encuentre la carpeta del PIA, exactamente en la carpeta image")
            obj2=BMetadata.Metadata()
        if opc==3:
            print("Para este ejersicio se necesita tener nmap instalado")
            obj3=CNmap.nmap()
        if opc==4:
            obj4=DCorreo.mail()
        if opc==5:
            obj5=FSocket.sok()
        if opc==6:
            obj6=GAPI.api()
        if opc==7:
            obj7=HHash.hash()
        if opc==8:
            exit()
