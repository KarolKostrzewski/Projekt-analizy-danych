from snooker.api.snooker_org import SnookerOrgApi


client = SnookerOrgApi(headers={'X-Requested-By': 'KarolProject'})

player = client.player(5)

print(player)