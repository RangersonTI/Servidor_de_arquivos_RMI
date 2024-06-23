import Pyro5.api as Pyro5

#name_server = Pyro5.locate_ns()
#url = name_server.lookup('obj')
url = "PYRO:obj_d95b1539d44d40738f9e3be785039ba9@localhost:3000"
o = Pyro5.Proxy(url)

print(o.listar_arquivos())
print(o.enviar_arquivo())