import requests
import json
import csv
import os

osfile = os.path.dirname(os.path.realpath(__file__))
url_request = "http://portaldamister.tech"
try:
    with open(
        osfile + "/acc.csv", 'r'

        ) as acc_c:
        accounts = csv.reader(acc_c)
        next(accounts)

        acc = []
        for x in accounts:
            if len(x) == 2 and all(x):
                acc.append({
                    "email": x[0].strip(),
                    "passw": x[1].strip()
                })
        
        try:
            msg_req = requests.get(url_request + "/portal").json()
            print("Atenção! Insira as suas credenciais de acesso! -", msg_req['message'])

            user = input("Usuário: ")
            passw = input("Senha: ")
            token = input("Token de acesso: ")

            chat_projz = input("Chat do Projz: ")

            payl = {
                "token": token.strip(),
                "chat-projz": chat_projz.strip(),

                "acc": acc
            } 

            try:
                response_qi = requests.post(
                    url_request + f"/api/user/z/doar-qi/?username={user}&passw={passw}",
                    json=payl
                    )
                print(json.dumps(response_qi.json(), ensure_ascii=False, indent=4))
            except requests.exceptions.JSONDecodeError:
                print("Erro ao requisitar a API")

        except KeyboardInterrupt:
            print("\nProcesso Interrompido") 
        
        except requests.exceptions.JSONDecodeError:
            print("Erro ao requisitar a API")

except FileNotFoundError:
    print("Não foi localizdo o arquivo 'acc.json'!\nO arquivo será criado")
    with open(
        osfile + "/acc.csv", 'w'
        ) as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['EMAIL', 'PASSW'])

        print("Arquivo criado!\nO arquivo está localizado em", osfile)