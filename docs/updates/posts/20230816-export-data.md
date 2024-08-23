---
date: 2023-08-16
authors:
  - astrea
categories:
  - Playerlist Premium

description: A new command to export Realm session data has been added for Playerlist Premium subscribers.
comments: true
---

# Exporting Realm Data

A new command to export Realm session data (a session being a period of time where the player was on a Realm, including when they joined and were last seen) has been added for Playerlist Premium subscribers. While the graph commands given through the bot may be more than enough for most users, some may wish to be able to make their own graphs, or just to try to analyze the data themselves.

<!-- more -->

# Details

By using a new command, `/premium export`, you can get a raw data dump that gathers around the last 30 days of Realm session data and exports it to a CSV file:

<figure markdown>
  ![Picture on how that data is sent.](export_data.png){ width="750" loading="lazy"}
</figure>

This data is in a CSV format, allowing you to use it in a spreadsheet program like Excel or Google Sheets. However, some processing will likely need to be done - the data given lists out each and every session, and does *not* do any calculations like how long a player was on or the like. While that can be found out through the data given, it's not as easy as just opening the file and using the graph feature. Regardless, you still may find it useful.