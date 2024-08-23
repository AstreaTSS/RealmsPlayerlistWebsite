---
date: 2023-09-07
authors:
  - astrea
categories:
  - Features

description: A new feature has been added, allowing you to get notifications right when specific players joins a Realm.
comments: true
---

# Player Watchlist

A new feature has been added to the Playerlist Bot, allowing you to get notifications (and a ping, if configured) right when specific players joins a Realm. This command can be used to track people in real time, or to just get a notification when a friend joins a Realm.

<!-- more -->

## Configuring the Watchlist

You can configure the watchlist through the `/watchlist` commands. Here is an example of the `/watchlist list` command, used for seeing your configuration for your watchlist:

<figure markdown>
  ![Picture on how the configuration command for the player watchlist looks like.](player_watchlist.png){ width="550" loading="lazy"}
</figure>

To add or remove players, use the `/watchlist add` and `/watchlist remove` commands. Notifications about players joining will be sent in your autorunning playerlist channel (which must be turned on to use this command) - by default, the message will not have a ping with it, but you can add one with `/watchlist ping-role`.

Messages are sent as soon as the bot detects a player has joined, which may take up to a minute.