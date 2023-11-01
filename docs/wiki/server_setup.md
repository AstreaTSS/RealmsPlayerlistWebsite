---
description: A guide on how to set up the Realms Playerlist Bot.
---


# Server Setup Guide

Setting up the bot is easy. You'll just need:
- A Discord server.
- Either the Realm code or ownership over the Realm.
- If you wish to have the auto-ran playerlist, then you'll need a channel where the bot can send that information to ready.

## Steps

First, invite the bot to your Discord server. If you're using the version hosted by me/AstreaTSS, just [use this link to do so.](https://sh.astrea.cc/inviteplayerlist)

There are two methods of linking the bot to your Realm from here, and they depend on your situation:

=== "(RECOMMENDED) Realm Code"
    !!! note "Realm Code Notes"
        This method is recommended for most users, as it's the easiest to set up. This *requires* a Realm code to use.

    Use `/config link-realm` to link your Realm to the server via the Realm code. Make sure to fill in the option for the Realm code (don't set `unlink`)!

=== "Linking as Realm Owner"
    !!! note "Linking as Realm Owner Notes"
        This method requires the Realm owner to authenticate the bot with Microsoft/Xbox so the bot can link the Realm you want. Authentication data is not stored beyond the link process itself, and only the bot's own account is used for actual functionality beyond this process.

    Use `/config alternate-link` to link your Realm to the server via the alternate method. This will start a setup process that will guide you through the process of linking the Realm. Make sure to read the prompts carefully!

From here, the steps are the same for both methods:
- If you want the autorunning playerlist, make sure the bot is able to read and send messages to the channel, then use `/config playerlist-channel`. Once again, make sure to fill in the option for the channel (don't set `unset`!).
- Other configuration settings follow a similar pattern, and are usually in `/config` (with the exception of `/watchlist`).
- After that, free to check all of the commands the bot has either through scrolling through the command list or using `/help`!
  - [The features](features.md) talks more in-depth about specific (free) features.
  - [The Premium page](premium.md) talks more about what Premium is, the features it has, and how to get it, if you're interested.

And that's it! If you got no errors, then you're all set. If you do, please follow the instructions they provide.

You can view your configuration at any time via `/config info`.

## Invite Link

If you just want the invite link for the version hosted by me, you can use:

- https://sh.astrea.cc/inviteplayerlist
- If you don't trust that link (it's just a shortened link for the following, but still), you can use the raw Discord link: https://discord.com/api/oauth2/authorize?client_id=725483868777611275&permissions=309238025280&scope=applications.commands%20bot
