
import discord, asyncio, feedparser

client = discord.Client()
#rss_feed is set at line 22 
async def rss_feed(channel_id, url):
	await client.wait_until_ready()
	channel = discord.Object(id=channel_id)
	
	feed = feedparser.parse(url)
	
	while not client.is_closed:
		await client.send_message(channel, feed.entries[0].title)
		await asyncio.sleep(15)
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
client.loop.create_task(rss_feed('412447735304814604', ''))
client.run('')
