import time, flask, json, threading, os, discord
from flask import request
from threading import Thread
from discord_webhook import DiscordWebhook, DiscordEmbed
orders = []

config = json.load(open("config.json", encoding="utf-8"))
app = flask.Flask(__name__)

def getinviteCode(invite_input): #gets invite CODE
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite
    
@app.route("/sellix", methods=["GET", "POST"])
def sellix():
    data = request.json
    if data in orders:    
        pass
    elif data not in orders:
        threading.Thread(target=start_sellix, args=[data, ]).start()
        orders.append(data)
    return '{"status": "received"}', 200

def start_sellix(data):
    try:
        if 'boosts' in data['data']['product_title'].lower():
            nick = ''
            invite_link = ''
            
            for i in data['data']['custom_fields']:
                
                if i == config['field_name_invite']:
                    invite_link = data['data']['custom_fields'][i]
                if i == "Boosting Account's Name":
                    nick = data['data']['custom_fields'][i].capitalize()
                    
            if nick == "":
                nick = config['server_nick'].capitalize()
                
            if data['data']['product_title'].replace(" ", "-").split("-")[0].lower() == "custom":
                amount = data['data']['quantity']
            
            if data['data']['product_title'].replace(" ", "-").split("-")[0].isdigit():
                amount = int(data['data']['product_title'].replace(" ", "-").split("-")[0])
                
            months = 3 if "3" in data['data']['product_title'].split("[")[1] else 1
            invite = getinviteCode(invite_link)
            
            if amount % 2 != 0:
                amount += 1
                
            embed = DiscordEmbed(title = "Sellix Order", description = f"*Started to boosts https://discord.gg/{invite} {amount}x for {months} month(s)*", color = 'ED00FF')
            sprint(f"Recieved New Sellix Order!", True)
            embed.set_timestamp()
            webhook = DiscordWebhook(url=config["order_logs"])
            webhook.add_embed(embed)
            webhook.execute()
            print()
            start = time.time()
            boosted = tboost(invite, amount, months, nick)
            end = time.time()
            time_taken = round(end - start, 2)
            
            if boosted == False:
                with open('success.txt', 'w') as f:
                    for line in variables.success_tokens:
                        f.write(f"{line}\n")
                
                with open('failed.txt', 'w') as g:
                    for line in variables.failed_tokens:
                        g.write(f"{line}\n")
            
                embed2 = DiscordEmbed(title = "**Error!**", description = f"*Failed to boost https://discord.gg/{invite} {amount}x for {months} month(s)*", color = 'FF0004')
                sprint(f"Failed to complete Sellix Order!", False)
                embed2.set_timestamp()
                webhook = DiscordWebhook(url=config["failed_boosts"])
                webhook.add_embed(embed2)
                webhook.execute()
                print()
            
                print()
                
                webhook = DiscordWebhook(url=config["failed_boosts"])
                with open("success.txt", "rb") as f:
                    webhook.add_file(file=f.read(), filename='success.txt')
                with open("failed.txt", "rb") as f:
                    webhook.add_file(file=f.read(), filename='failed.txt')
                webhook.execute()
                
                os.remove("success.txt")
                os.remove("failed.txt")
                
            elif boosted:
                with open('success.txt', 'w') as f:
                    for line in variables.success_tokens:
                        f.write(f"{line}\n")
                
                with open('failed.txt', 'w') as g:
                    for line in variables.failed_tokens:
                        g.write(f"{line}\n")
                        
                embed3 = DiscordEmbed(title = "Boost Log", description = f"*Boosted https://discord.gg/{invite} {amount}x in {time_taken}s for {months} month(s)*\n**Finished Boosts: **`{len(variables.success_tokens)*2}`\n**Failed Boosts: **`{len(variables.failed_tokens)*2}", color = 'ED00FF')
                sprint(f"Completed Sellix Order!", False)
                embed3.set_timestamp()
                webhook = DiscordWebhook(url=config["boosts_logs"])
                webhook.add_embed(embed3)
                webhook.execute()
                print()
                print()
                
                webhook = DiscordWebhook(url=config["boosts_logs"])
                with open("success.txt", "rb") as f:
                    webhook.add_file(file=f.read(), filename='success.txt')
                with open("failed.txt", "rb") as f:
                    webhook.add_file(file=f.read(), filename='failed.txt')
                webhook.execute()
                
                os.remove("success.txt")
                os.remove("failed.txt")
                
        else:
            pass
    
    except Exception as e:
        print(f"{e} | Function: Start_Sellix", False)
        pass
    
@app.route("/sellapp", methods=["GET", "POST"])
def sellapp():
    data = request.json
    if data in orders:    
        pass
    elif data not in orders:
        threading.Thread(target=start_sellapp, args=[data, ]).start()
        orders.append(data)
    return 'Our server has received your order.', 200


def start_sellapp(data):
    try:
        nick = ''
        invite_link = ''

        for i in data['additional_information']:
            print(i)
            if i['label'] == config['field_name_invite']:
                invite_link = i['value']
                
            if i['label'] == "Boosting Account's Name":
                nick = i['value'].capitalize()
        
        if nick == "":
            nick = config['server_nick'].capitalize()
        
        if data['listing']['slug'].split("-")[0].lower() == "custom":
            amount = data['quantity']
            
        elif data['listing']['slug'].split("-")[0].isdigit():
            amount = int(data['listing']['slug'].split("-")[0])
            
        months = 3 if "3" in data['listing']['title'].split("[")[1] else 1
        invite = getinviteCode(invite_link)
        
        if amount % 2 != 0:
            amount += 1
            
        embed = DiscordEmbed(title = "Sell.App Order", description = f"*Started to boosts https://discord.gg/{invite} {amount}x for {months} month(s)*", color = 'ED00FF')
        sprint(f"Recieved New Sell.App Order!", True)
        embed.set_timestamp()
        webhook = DiscordWebhook(url=config["order_logs"])
        webhook.add_embed(embed)
        webhook.execute()
        print()
        start = time.time()
        boosted = tboost(invite, amount, months, nick)
        end = time.time()
        time_taken = round(end - start, 2)
        
        if boosted == False:
            with open('success.txt', 'w') as f:
                for line in variables.success_tokens:
                    f.write(f"{line}\n")
            
            with open('failed.txt', 'w') as g:
                for line in variables.failed_tokens:
                    g.write(f"{line}\n")
        
        
            embed2 = DiscordEmbed(title = "Boost Log", description = f"*Failed to boost https://discord.gg/{invite} {amount}x for {months} months(s)*", color = 'FF0004')
            sprint(f"Failed to complete Sell.App Order!", False)
            embed2.set_timestamp()
            webhook = DiscordWebhook(url=config["failed_boosts"])
            webhook.add_embed(embed2)
            webhook.execute()
            print()
            print()

            webhook = DiscordWebhook(url=config["failed_boosts"])
            with open("success.txt", "rb") as f:
                webhook.add_file(file=f.read(), filename='success.txt')
            with open("failed.txt", "rb") as f:
                webhook.add_file(file=f.read(), filename='failed.txt')
            webhook.execute()
            
            os.remove("success.txt")
            os.remove("failed.txt")
                
        elif boosted:
            with open('success.txt', 'w') as f:
                for line in variables.success_tokens:
                    f.write(f"{line}\n")
            
            with open('failed.txt', 'w') as g:
                for line in variables.failed_tokens:
                    g.write(f"{line}\n")
                    
            embed3 = DiscordEmbed(title = "Boost Log", description = f"*Boosted https://discord.gg/{invite} {amount}x in {time_taken}s for {months} month(s)*\n**Finished Boosts: **`{len(variables.success_tokens)*2}`\n**Failed Boosts: **`{len(variables.failed_tokens)*2}", color = 'ED00FF')
            sprint(f"Completed Sell.App Order!", True)
            embed3.set_timestamp()
            webhook = DiscordWebhook(url=config["boosts_logs"])
            webhook.add_embed(embed3)
            webhook.execute()
            print()
            print()

            webhook = DiscordWebhook(url=config["boosts_logs"])
            with open("success.txt", "rb") as f:
                webhook.add_file(file=f.read(), filename='success.txt')
            with open("failed.txt", "rb") as f:
                webhook.add_file(file=f.read(), filename='failed.txt')
            webhook.execute()
            
            os.remove("success.txt")
            os.remove("failed.txt")
            
    except Exception as e:
        print(f"{e} | Function: Start_Sellapp", False)
        pass

def run():
    app.run(host="0.0.0.0", port=6969, debug=False, use_reloader=False)
     
def keep_alive():
    t = Thread(target=run)
    t.start()
