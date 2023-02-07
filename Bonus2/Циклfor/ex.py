'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis metus justo. Etiam blandit commodo elit sed pharetra.
Donec purus ligula, sodales at scelerisque id, aliquet ut justo. Morbi posuere, nibh quis pretium faucibus, 
nisl felis malesuada erat, vel interdum ligula massa ac ligula. Etiam sollicitudin efficitur neque vel accumsan.
'''

a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis metus justo. Etiam blandit commodo elit sed pharetra."
x = a.split(" ")
# x.append("Donec purus ligula, sodales at scelerisque id, aliquet ut justo. Morbi posuere, nibh quis pretium faucibus,")
# print(x)

# for i in range(len(x)):
#     print(x[i])

b = "Donec purus ligula, sodales at scelerisque id, aliquet ut justo. Morbi posuere, nibh quis pretium faucibus,"
y = b.split(" ")
# print(y)

# for i in range(len(y)):
#     print(y[i])

c = "nisl felis malesuada erat, vel interdum ligula massa ac ligula. Etiam sollicitudin efficitur neque vel accumsan."
z = c.split(" ")
# print(z)

x.extend(y)
x.extend(z)
for i in range(len(x)):
    print(x[i])



# for i in range(len(z)):
#     print(z[i])