class Cifrado():
    def __init__(self):
        try:
            clave=0
            abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            cad=input("Ingresa una palabra: ").upper()
            while clave<1 or clave>5:
                clave=int(input("Ingresa una clave numerica entre 1 y 5: "))
            con=True
            while con:
                opc= int(input("MENU\n1: Cifrar.\n2: Descifrar.\n3: Hack.\n4: Salir.\n\n\n\t\tSelecciona una opcion: "))
                if opc==1:
                    text_Cifrado=""
                    for i in cad:
                        if i in abc:
                            pos_letra=abc.index(i)
                            nueva_pos=(pos_letra + clave)%len(abc)
                            text_Cifrado+=abc[nueva_pos]
                        else:
                            text_Cifrado+=i
                    print("Mensaje cifrado: ",text_Cifrado)

                if opc==2:
                    aux=int(input("Ingresa una clave numerica para desencriptar el mensaje "+text_Cifrado+": "))
                    if aux==clave:
                        text_DesCifrado=""
                        for i in text_Cifrado:
                            if i in abc:
                                pos_letra=abc.index(i)
                                nueva_pos=(pos_letra - clave)%len(abc)
                                text_DesCifrado+=abc[nueva_pos]
                            else:
                                text_DesCifrado+=i
                        print("Mensaje cifrado: ",text_DesCifrado)
                    else:
                        print("Clave incorrecta, por favor, vuelva a intentar!!")

                if opc==3:
                    f=open("Archivo.txt", "r")
                    #Aqui hice un diccinario más pequeño ya que el que venia en Teams me daba error, estaba muy grande tal vez.
                    cont=f.read()
                    if cad in cont:
                        print("Esta palabra es vulnerable!!")
                    else:
                        print("Esta palabra no se encuentra en el diccionaio de palabras, no es posible desifrarla!!")
                    f.close()
                if opc==4:
                    print("Fin del programa!!")
                    con=False
        except:
            print("Hubo un error desconocido, por favor inicie el programa de nuevo.")
        


    
    
        



    
