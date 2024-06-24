import Pyro5.api as Pyro5

#name_server = Pyro5.locate_ns()
#url = name_server.lookup('obj')
url = "PYRO:servidor.arquivo.rmi@192.168.1.103:3000"
o = Pyro5.Proxy(url)

print(o.listar_arquivos())
#print(o.enviar_arquivo())