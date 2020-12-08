import nmap
class nmap():
    def __init__(self):
        try:
            print("Nombre: César Alejandro Rodríguez Pérez -  Matricula: 1734223")
            begin =int(input("Ingres el puerto inicial: "))
            end = int(input("Ingrese el puerto final: "))
            target = input("Ingrese la ip: ")
            str(target)
            scanner = nmap.PortScanner() 
            for i in range(begin,end+1):
                res = scanner.scan(target,str(i))
                res = res['scan'][target]['tcp'][i]['state']
                ar=open("ResE8CARP.csv","a")
                ar.write(res)
                ar.close()
                print(f'port {i} is {res}.')
        except:
            print("Error, por favor, vuelva a ejecutar el script.")
