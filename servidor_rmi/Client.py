import Pyro5.api as Pyro5

#name_server = Pyro5.locate_ns()
#url = name_server.lookup('obj')
url = "PYRO:obj_87716e1ca45e4d668890499b45a00508@localhost:3000"
o = Pyro5.Proxy(url)

print(o.saludar())