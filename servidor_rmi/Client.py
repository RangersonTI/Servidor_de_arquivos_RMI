import Pyro5.api as Pyro5

name_server = Pyro5.locate_ns()
url = name_server.lookup('obj')
o = Pyro5.Proxy(url)

print(o.saludar())