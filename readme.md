People be selling this edit shit for $75+ so have it for free

ISUSES

If you are having trouble with the discord bot shit and it gives errors do:

pip uninstall pycord

pip uninstall discord.py

pip uninstall discord

pip install -U git+https://github.com/Pycord-Development/pycord

pip install colorama httpx tls_client flask fade discord_webhook



INSTALLATION GUIDE



- Go to https://ngrok.com/, download and signup. Connect your account using your auth token. (It is important to create an account and connect it. If you do not do that your session will expire in 2 hrs and you will have to create a new session with a new webhook.)
- Open ngrok and type 'ngrok http 6969'
- Copy the url written after 'Forwarding' and before -> (https://xxxxxxxxxxxxxxxxxx.io). This is the ngrok webhook url.

- Fill in the config

Sellix:

- Create a product named in this format: {Amount} Server Boosts [{Months} Months], example: 14 Server Boosts [3 Months]. This is important as the program will not detect the amount of boosts and for how many months the server needs to be boosted.
- Set the maximum quantity to 1.
- Add a custom field and name it whatever you want (this field should be set for taking the server invite link as an input) Set 'type' to 'Text'. Copy and paste that name in config.json, 'field_name_invite' field.
- After creating all the products, head over to Developers > Webhooks.
- Click on Add Webhooks Endpoint.
- Type: Sellix, Webhook URL: {ngrok webhook url}/sellix, Event: Order > order:paid.
- You are all done.

Sell.App:
- Create a product named in this format: {Amount} Server Boosts [{Months} Months], example: 14 Server Boosts [3 Months]. This is important as the program will not detect the amount of boosts and for how many months the server needs to be boosted.
- Click on 'Content', select 'Dynamic Product' and 'Manual Service'. In the 'Dynamic Webhook URL' field input {ngrok webhook url}/sellapp and in 'Service Info' input the message you want your customer to get on their email.
- Set the maximum quantity to 1.
- Add a custom field and name it whatever you want (this field should be set for taking the server invite link as an input) Set 'type' to 'Text'. Copy and paste that name in config.json, 'field_name_invite' field.

Sellpass:
- Input your sellpass api key in the config. You can find the api key here: https://dashboard.sellpass.io/settings/security
- Create a product named in this format: {Amount} Server Boosts [{Months} Months], example: 14 Server Boosts [3 Months]. This is important as the program will not detect the amount of boosts and for how many months the server needs to be boosted.
- Click on 'Content', select 'Dynamic Product' and 'Manual Service'. In the 'Dynamic Webhook URL' field input {ngrok webhook url}/sellpass and in 'Service Info' input the message you want your customer to get on their email.
- Set the maximum quantity to 1.
- Add a custom field and name it whatever you want (this field should be set for taking the server invite link as an input) Set 'type' to 'Text'. Copy and paste that name in config.json, 'field_name_invite' field.

