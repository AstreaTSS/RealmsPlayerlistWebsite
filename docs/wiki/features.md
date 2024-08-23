---
description: All of the free features of the Realms Playerlist Bot.
---

!!! note "Note"
    This page only covers the free features of the bot. For the Premium features, see [the Premium page](premium.md).

# Features

## The Playerlist
Of course, this is the main feature of the bot. It's also one of those features that is easier to show than tell:

<figure markdown>
  ![Picture of how the playerlist looks like.](playerlist.png){ width="550" }
  <figcaption>The censored space are gamertags of users on the Realm.</figcaption>
</figure>

The command version (`/playerlist`) allows you to get who was on the Realm up to the last 24 hours (though it defaults to 12 hours). There is also an automatic version that runs every hour in a specified channel (as seen in the picture) - it displays a list going back an hour, every hour. This can be configured through `/config autorunning-playerlist-channel`.

The command can normally only be run by people with Manage Server permissions (can be adjusted the same way you adjust other slash command permissions[^1]) and is not meant to be seen by normal people. However, normal users, by default, can run `/online`, which shows everyone who is on the Realm at that moment:

<figure markdown>
  ![Picture of how /online looks like.](online.png){ width="450" loading="lazy"}
</figure>

## Specific Player Information

You can also request for a breakdown of join/leaves (otherwise known as sessions) via `/get-player-log`:

<figure markdown>
  ![Picture of how /get-player-log looks like.](get_player_log.png){ width="550" loading="lazy"}
</figure>

Using this command allows you to scroll through each session in an intuitive format. For fun, the command also displays their total playtime.

By default, the command only goes back a day, but it can go till 7, as seen here.

## Realm Offline Notifications

Realms go offline a lot if they're big, most likely because they can't handle the load. Sometimes, it can be useful to get pinged when that happens:

<figure markdown>
  ![Picture of how Realm offline notifications looks like.](realm_offline.png){ loading="lazy" }
  <figcaption>Note: despite the role name used, this does not exclusively trigger when the Realm crashes.</figcaption>
</figure>

This simply hooks onto your autorunning playerlist and can be managed through `/config realm-offline-role`. The Realm offline detection is mostly accurate[^2] - it may not work as well for smaller Realms, but for larger ones, it should work fine.

!!! note
    By default, Realm Offline messages are sent to your autorunning/automatic playerlist channel. You can change this through `/config notification-channel`.

## Playtime Leaderboard

By using `/leaderboard` and either voting or purchasing Premium, you can get a ranked list of players by playtime for your Realm:

<center>
  ![Picture of how /leaderboard looks like.](leaderboard.png){ width="350" loading="lazy"}
  <figcaption>Note: the playtimes are rounded for convenience, and so may be slightly off.</figcaption>
</center>

The period of time can be adjusted as needed - it can go all the way back to 30 days.

## Graphs

You can make cool graphs about your Realm and its users through the `/graph` commands:

<figure markdown>
  ![Picture on how graphs can looks like.](realm_chart.png){ width="550" loading="lazy"}
</figure>

There are a variety of options to chose from, from the graph up above to a day-to-day breakdown. The data isn't 100% accurate, but you can use it to observe patterns... or just show it off for fun.

Some of the graphs with longer time periods may require voting or purchasing Premium to use.

## Other Statistics

There are other, minor statistics you can get through the `/misc-stats` command. For example, you can get the average playtime of all players on the Realm:

<figure markdown>
  ![Picture on how /misc-stats average-playtime looks like.](average_playtime.png){ loading="lazy"}
</figure>

As of right now, there is:
- `/misc-stats average-playtime` - the average playtime of all players or a specified player on the Realm.
- `/misc-stats total-playtime` - the total playtime of all players or a specified player on the Realm.
- `/misc-stats longest-session` - the longest session of all players or a specified player on the Realm.

## Player Watchlist

You get can messages and even pings right when a player joins your Realm through the `/watchlist` commands:

<figure markdown>
  ![Picture on how the configuration command for the player watchlist looks like.](player_watchlist.png){ width="550" loading="lazy"}
</figure>

This can be used to keep track of players you want to keep an eye on, or just to get a ping when a friend joins your Realm. Messages are sent as soon as the bot detects a player has joined, which may take up to a minute.
You can watch up to 3 players at any one time.

!!! note
    Pings are not enabled for watchlists by default. You can enable them through `/watchlist ping-role`.

    By default, watchlist messages are sent to your autorunning/automatic playerlist channel. You can change this through `/watchlist channel` or `/config notification-channel`.

## Nicknames

You can set a nickname for a player with `/nickname set <Xbox gamertag> <nickname>`, and remove it with `/nickname remove`. This will replace this gamertag in most commands with the nickname you set. Feel free to use this however you want!

There is currently a limit of 10 people per server, which you can keep track of through `/nickname list`:

<figure markdown>
  ![An example of /nickname list. There is one censored player who has been nicknamed to "Test".](nicknames.png)
</figure>

!!! note
    This does not affect the *inputting* of names - you'll still need to use their proper gamertag. This only affects the *output* of the bot.

[^1]: https://support.discord.com/hc/en-us/articles/4644915651095-Command-Permissions
[^2]:
    As the name of the feature suggests, it detects when your Realm goes *offline* - more accurately, it detects when the bot can't detect the Realm.
    This does mean it can trigger if the bot is accidentally kicked or banned, or just because Minecraft decided to freak out for a few minutes.