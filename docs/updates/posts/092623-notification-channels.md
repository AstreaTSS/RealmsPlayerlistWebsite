---
date: 2023-09-26
authors:
  - astrea
categories:
  - Features

description: A configuration option has been added to allow you to change the channel that some notifications are sent to.
comments: true
---

# Notification Channels

A new configuration option has been added to allow you to change the channel that some notifications, like the Realm Offline and Player Watchlist messages, are sent to.

<!-- more -->

This is most useful for those who use the automatic/autorunning playerlist channel as a public view for who has been on the Realm, as it allows you to keep the notifications separate from the playerlist. It also can be used to make sure these types of messages don't get lost in the shuffle of the playerlist, which is especially possible when using the Live Playerlist.

You can change the channel that these notifications are sent to through `/config notification-channel`. The command allows you to pick what "feature" you want to change and if you want to set a channel or reset it back to the autorunning playerlist channel. Admittedly, the usage of this command is a bit clunky, and it may be changed in the future.