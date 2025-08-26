print("Você torce para qual time?")
time = input("Digite o seu time: ")

if time.lower() == "flamengo" or time.lower()== "barcelona" or time.lower()== "inter miami" or time.lower() == "real":
    print(f"O {time} é muito bom")
else:
    print(f"O {time} é muito ruim") 
