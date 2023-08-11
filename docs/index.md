---
title: Realms Playerlist Bot
hide:
  - footer
---

<figure markdown>
  ![Realm Playerlist Bot's banner.](_static/rpl_banner.min.jpg){ width="700"}
</figure>

<p align="center">
  <a href="wiki/server_setup.html">
    <img src="https://img.shields.io/badge/Server%20Setup%20Guide-Link-%23b05bff?style=for-the-badge&logo=bookstack&logoColor=%23b05bff" alt="Server Setup Guide" loading="lazy">
  </a>
  <a href="https://discord.gg/NSdetwGjpK">
    <img src="https://img.shields.io/badge/Support%20Server-Link-%235865F2?style=for-the-badge&logo=discord" alt="Support Server Link" loading="lazy">
  </a>
  <a href="wiki/premium.html#how-to-get-playerlist-premium">
    <img src="https://img.shields.io/badge/Purchase%20Premium-Link-%2326ad3e?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB2ZXJzaW9uPSIxLjIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDY0MCA1MTIiIHdpZHRoPSIxNTAiIGhlaWdodD0iMTIwIj48c3R5bGU%2BLmF7ZmlsbDojMjZhZDNlfTwvc3R5bGU%2BPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGFzcz0iYSIgZD0ibTE2MCAzMmg0MTZjMzUuMyAwIDY0IDI4LjcgNjQgNjR2MjI0YzAgMzUuMy0yOC43IDY0LTY0IDY0aC00MTZjLTM1LjMgMC02NC0yOC43LTY0LTY0di0yMjRjMC0zNS4zIDI4LjctNjQgNjQtNjR6bS0xMTIgMzI4YzAgMzkuOCAzMi4yIDcyIDcyIDcyaDQwMGMxMy4zIDAgMjQgMTAuNyAyNCAyNCAwIDEzLjMtMTAuNyAyNC0yNCAyNGgtNDAwYy02Ni4zIDAtMTIwLTUzLjctMTIwLTEyMHYtMjQwYzAtMTMuMyAxMC43LTI0IDI0LTI0IDEzLjMgMCAyNCAxMC43IDI0IDI0em0xMTItMjY0djY0YzM1LjMgMCA2NC0yOC43IDY0LTY0em0zNTIgMjI0aDY0di02NGMtMzUuMyAwLTY0IDI4LjctNjQgNjR6bTY0LTE2MHYtNjRoLTY0YzAgMzUuMyAyOC43IDY0IDY0IDY0em0tMjY0LjYgMTA0LjZjMTUgMTUgMzUuNCAyMy40IDU2LjYgMjMuNCAyMS4yIDAgNDEuNi04LjQgNTYuNi0yMy40IDE1LTE1IDIzLjQtMzUuNCAyMy40LTU2LjYgMC0yMS4yLTguNC00MS42LTIzLjQtNTYuNi0xNS0xNS0zNS40LTIzLjQtNTYuNi0yMy40LTIxLjIgMC00MS42IDguNC01Ni42IDIzLjQtMTUgMTUtMjMuNCAzNS40LTIzLjQgNTYuNiAwIDIxLjIgOC40IDQxLjYgMjMuNCA1Ni42em0tMTUxLjQgNTUuNGg2NGMwLTM1LjMtMjguNy02NC02NC02NHoiLz48L3N2Zz4%3D&logoColor=%2326ad3e" alt="Purchase Premium" loading="lazy">
  </a>
</p>

<p align="center">
  A bot that helps out owners of Minecraft: Bedrock Edition Realms by showing various statistics related to player join/leaves.
</p>

It's:
- 🚀 **Fast:** Under the right (and typical) circumstances[^1], it can generate a list of ~300 players in under *4 seconds,* 3-3.5 of which is only due to Discord's rate limits.[^2]
- 📊 **Informative:** The main feature of the bot, the playerlist, can give a detailed log of players on a Realm at a moment's notice. You can also get a breakdown for an individual player to analyze as you wish.[^3]
- 👌 **Easy to Use**: Simply add the bot, link your Realm, and you already have join/leave tracking enabled - no need to use your Xbox account for the bot's features. Take a look at the [Server Setup Guide](server_setup.md) for more information.
- 🔓 **Open Source**: The code is available to the public and able to be audited and learned from. Dedicated users can even (try to[^4]) self-host the bot, if they wish.

## Features

### The Playerlist
Of course, this is the main feature of the bot. It's also one of those features that is easier to show than tell:

<figure markdown>
  ![Picture of how the playerlist looks like.](_static/playerlist.png){ width="550" loading="lazy" }
  <figcaption>The censored space are gamertags of users on the Realm.</figcaption>
</figure>

The command version allows you to get who was on the Realm up to the last 24 hours (though it defaults to 12 hours). There is also an automatic version that runs every hour in a specified channel (as seen in the picture) - it displays a list going back an hour, every hour.

The command can normally only be run by people with Manage Server permissions (can be adjusted the same way you adjust other slash command permissions[^5]) and is not meant to be seen by normal people. However, normal users, by default, can run `/online`, which shows everyone who is on the Realm at that moment:

<figure markdown>
  ![Picture of how /online looks like.](_static/online.png){ width="450" loading="lazy"}
</figure>

### Specific Player Information

You can also request for a breakdown of join/leaves (otherwise known as sessions) via `/get-player-log`:

<figure markdown>
  ![Picture of how /get-player-log looks like.](_static/get_player_log.png){ width="550" loading="lazy"}
</figure>

Using this command allows you to scroll through each session in an intuitive format. For fun, the command also displays their total playtime.

By default, the command only goes back a day, but it can go till 7, as seen here.

### Realm Offline Notifications

Realms go offline a lot if they're big, most likely because they can't handle the load. Sometimes, it can be useful to get pinged when that happens:

<figure markdown>
  ![Picture of how Realm offline notifications looks like.](_static/realm_offline.png){ loading="lazy" }
  <figcaption>Note: despite the role name used, this does not exclusively trigger when the Realm crashes.</figcaption>
</figure>

This simply hooks onto your autorunning playerlist. The Realm offline detection is mostly accurate[^6] - it may not work as well for smaller Realms, but for larger ones, it should work fine.

### Graphs

You can make cool graphs about your Realm and its users:

<figure markdown>
  ![Picture on how graphs can looks like.](_static/realm_chart.png){ width="550" loading="lazy"}
</figure>

There are a variety of options to chose from, from the graph up above to a day-to-day breakdown. The data isn't 100% accurate, but you can use it to observe patterns... or just show it off for fun.

### Premium

**Realms Playerlist Premium** allows for extra features that otherwise could not be provided by the bot without funding. [Take a closer look at Premium here.](premium.md)

#### Live Playerlist

Instead of making the bot send a summary of people on every hour, a **live playerlist** shows who joined and left a Realm every minute, basically making it a live join/leave logger.

It looks something like this:

<figure markdown>
  ![Picture on how live playerlist looks like.](_static/live_playerlist.png){ width="420" loading="lazy"}
</figure>

This has a variety of uses, from statistical to moderation - it's really up to you what you do with this information. Some Realms use it both to narrow down subjects to a precise degree while also tracking active Realm times. Using Discord's search functionality, the possibilities are near endless.

#### Live Online List

Taking the live playerlist to its logical conclusion, a **live online list** is a message that constantly updates with the players currently on the Realm, as seen below:

<figure markdown>
  ![Animated picture on how the live online list looks like.](_static/live_online_list.webp){ width="500" loading="lazy"}
</figure>

As of right now, this feature requires the live playerlist to also be enabled.

#### Device Information

Through an extra toggle, the bot can fetch and display device information whenever a user is online. This affects `/online`, the normal playerlist, and the live playerlist.

For example, `/online` becomes this:

<figure markdown>
  ![Picture on how `/online` looks when the toggle is enabled.](_static/fetch_devices.png){ width="420" loading="lazy"}
</figure>

This does slow the bot down a bit when fetching the device[^7], and privacy settings may make some users not have information regardless[^8], but can used as an extra moderation/statistical tool.

This is also available as a toggle to non-Premium users of `/online` (and only `/online`) if they vote for the bot.

## Adding The Bot

If you wish to add this bot, just [use the Server Setup Guide on how to do so](server_setup.md). It'll give a basic rundown on how to set up the bot, as well as showing how to set basic options.

## FAQ

There's a whole section in the wiki about this! [Check it out here](faq.md).

[^1]:
    The bot relies on a cache to speed up certain parts of the playerlist - there's a rare chance that the bot's cache doesn't have any useful information in it when
    the playerlist is generated, but... well, it's rare because the bot caches a lot quickly.
[^2]:
    Admittedly, the test used to determine this wasn't very scientific, but the actual number for the speed of the playerlist is likely *lower*, not higher.
    Essentially, I measured the time until the bot sends the first part of the calculated playerlist, which is both the time it takes for the bot to calculate it
    *and* the time for the bot to make a web request to Discord to actually send the message (adding a considerable delay). The ratelimits come in when sending every
    part of the playerlist (as a list that big will not fit in one message) - the bot sleeps 0.2 seconds between messages to try not to trigger them, and Discord can
    still trigger them anyways, forcing the bot to wait longer. This test was also done with an old version which split the playerlist into shorter pieces than it should have.
[^3]: Through `/get-player-log`.
[^4]: This bot is *hard* to self-host due to the number of things it uses. Check out [this FAQ question][can-i-self-host-this] for more information.
[^5]: https://support.discord.com/hc/en-us/articles/4644915651095-Command-Permissions
[^6]:
    As the name of the feature suggests, it detects when your Realm goes *offline* - more accurately, it detects when the bot can't detect the Realm.
    This does mean it can trigger if the bot is accidentially kicked or banned, or just because Minecraft decided to freak out for a few minutes.
[^7]: This requires bypassing certain parts of the bot (its cache) to get up-to-date information, hence the slowdown.
[^8]: If users are offline on Xbox Live, their device won't appear. There may be settings that also make the user not share their current game details.
