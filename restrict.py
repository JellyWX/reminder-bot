import discord
import json
from globalvars import restrictions

async def restrict(message, client):
  if not message.author.server_permissions.administrator:
    await client.send_message(message.channel, embed=discord.Embed(description='You must be an admin to run this command'))
    return

  if message.channel.id not in restrictions.keys():
    restrictions[message.channel.id] = []

  disengage_all = True
  args = 0

  for role in message.role_mentions:
    args = 1
    if role.id not in restrictions[message.channel.id]:
      disengage_all = False
    restrictions[message.channel.id].append(role.id)

  if disengage_all and args:
    for role in message.role_mentions:
      restrictions[message.channel.id].remove(role.id)
      restrictions[message.channel.id].remove(role.id)

    await client.send_message(message.channel, embed=discord.Embed(description='Disabled channel reminder permissions for roles.'))

  elif args:
    await client.send_message(message.channel, embed=discord.Embed(description='Enabled channel reminder permissions for roles.'))

  else:
    await client.send_message(message.channel, embed=discord.Embed(description='Allowed: <@&{}>'.format('> <@&'.join(restrictions[message.channel.id]))))

  with open('DATA/restrictions.json', 'w') as f:
    json.dump(restrictions, f)
