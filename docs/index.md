---
title: Realms Playerlist Bot
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
  A bot that helps out owners of Minecraft: Bedrock Edition Realms by showing various statistics related to player join/leaves. A great companion to other Realm bots.
</p>

It's:
- ⚙️ **Feature-Filled**: The main feature of the bot, the playerlist, can give a detailed log of players that have been on a Realm both as a command and automatically every hour. There are plenty of more commands able to do more, like commands to:
  - Make graphs of a Realm/player.
  - Give specific details of a player and times they joined/left.
  - Send a leaderboard to find out who's been on your Realm the most.
  - And more! Check out [the features page](features.md) for more information.
- 🚀 **Fast**: Under typical circumstances, it can send a list of ~300 players that have been on a Realm in under *2 seconds*[^1]. Other commands are similarly fast, even with large amounts of players.[^2]
- 👌 **Easy to Use**: Simply add the bot, link your Realm using a Realm code or a one-time authentication process, and you already have join/leave tracking enabled - no need to use your Xbox account for the bot's actual features. Take a look at the [Server Setup Guide](server_setup.md) for more information.
- 🔓 **Open Source**: The code is available to the public under the GNU AGPL license and able to be audited and learned from. Dedicated users can even (try to[^3]) self-host the bot, if they wish.

With ***Playerlist Premium***, only $2 a month, you can get these features and more:
- **Live Playerlist**, which showcases who left and joined every minute.
- **Live Online List**, which sends a message that constantly updates to show currently online players.
- **Device information fetching**, which allows you to see which devices players are using for many commands.
- **Full Realm data exporting**, which allows for complete control over your Realm's data.

You can check out every feature of Premium and how to get it [on the Premium Page](premium.md).

## Features

As noted above, you can find more information about the (free) features the Playerlist Bot has [on the features page](features.md).

Information about Playerlist Premium and the features it brings can be found at [the Premium page](premium.md).


## Adding The Bot

If you wish to add this bot, just [use the Server Setup Guide on how to do so](server_setup.md). It'll give a basic rundown on how to set up the bot, as well as showing how to set basic options.

## FAQ

There's a whole section in the wiki about this! [Check it out here](faq.md).

[^1]:
    During the tests I did to determine this fact (around August 2023), the bot spent around 0.5 seconds from the time the command is received by the bot to actually gather and process the data into embeds. The other ~1.5 seconds is literally spent sending the embeds through Discord (web requests take a bit, and the bot also only sends one embed per message due to character limits).
[^2]: In general, commands shouldn't take more than 10 seconds. At worst, they won't take more than a minute.
[^3]: This bot is *hard* to self-host due to the number of things it uses. Check out [this FAQ question][can-i-self-host-this] for more information.
