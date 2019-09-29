from core.util import shifter, standby, get_crd

sh = "templates/t1.jpeg"
tmp = "templates/quick.png"

x = shifter((10,10), 10)
y = standby(sh, tmp)

print(x)
print(y)