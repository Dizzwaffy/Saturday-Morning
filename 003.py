vlan_normal=range(1,1005)
vlan_extendida=range(1006,4094)
numero_vlan=int(input ("El numero de vlan es"))

if numero_vlan in vlan_normal:
    print ("Tu numero de vlan corresponde a una vlan normal")

elif numero_vlan in vlan_extendida:
    print("Tu numero de vlan corresponde a una vlan extendida")
else:
    numero_vlan 
    print("Tu numero no corresponde a una vlan")