# Server Setup

Setting up the bot is easy. You'll just need:
- A Discord server.
- The Realm code. If you don't have one for your Realm, you'll need one at least temporarily.
- If you wish to have the auto-ran playerlist, then you'll need a channel where the bot can send that information to ready.

## Steps
1. Invite the bot to your Discord server. If you're using the version hosted by me/AstreaTSS, just [use this link to do so.](https://sh.astrea.cc/inviteplayerlist)
2. Use `/config link-realm` to link your Realm to the server via the Realm code. Make sure to fill in the option for the Realm code (don't set `unlink`)!
3. If you want the auto-ran playerlist, make sure the bot is able to read and send messages to the channel, then use `/config playerlist-channel`. Once again, make sure to fill in the option for the channel (don't set `unset`!).
4. If you want to be pinged whenever the Realm goes down and/or crashes, use `/config realm-offline-role` (of course, don't set `unset`). That one will show you a prompt before actually setting it - pay attention to that!

And that's it! If you got no errors, then you're all set. If you do, please follow the instructions they provide.

You can view your configuration at any time via `/config info`.

## Invite Link

If you just want the invite link for the version hosted by me, you can use:
- https://sh.astrea.cc/inviteplayerlist
- If you don't trust that link (it's just a shortened link for the following, but still), you can use the raw Discord link: https://discord.com/api/oauth2/authorize?client_id=725483868777611275&permissions=309238025280&scope=applications.commands%20bot
