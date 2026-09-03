---
description: Information about Realms Playerlist Premium and how to get it.
---


# Playerlist Premium

**Realms Playerlist Premium** is a $2 USD monthly purchase (or a $20 USD yearly purchase) you can make in order to get special features not usually obtainable. These are usually locked behind a paywall because it would be infeasible to allow everyone to use these features without making the bot as a whole suffer - by limiting the amount of users who can use them, I can still provide these features to those who need it while also earning funds necessary to keep the bot alive and running as it grows (scaling isn't cheap).

## Features

### Live Playerlist

Instead of making the bot send a summary of people on every hour, a **live playerlist** shows who joined and left a Realm every minute, basically making it a live join/leave logger. It can be enabled through `/premium live-playerlist`.

It looks something like this:

<figure markdown>
  ![Picture on how live playerlist looks like.](live_playerlist.png){ width="420"}
</figure>

This has a variety of uses, from statistical to moderation - it's really up to you what you do with this information. Some Realms use it both to narrow down subjects to a precise degree while also tracking active Realm times. Using Discord's search functionality, the possibilities are near endless.

Of course, this is more spammy than the summary given every hour, and also *replaces the autorunner version entirely.* The `/playerlist` command will still be available to you, though, and the benefits most likely outweigh the downsides for you.

### Live Online List

Taking the live playerlist to its logical conclusion, a **live online list** is a message that constantly updates with the players currently on the Realm, as seen below:

<figure markdown>
  ![Animated picture on how the live online list looks like.](live_online_list.webp){ width="500" loading="lazy"}
</figure>

Simply send with `/premium send-live-online-list` and you should be good to go.

As of right now, this feature requires the live playerlist to also be enabled.

### Device Information

Through an extra toggle (`/premium device-information`), the bot can fetch and display device information whenever a user is online. This affects `/online`, the normal playerlist, and the live playerlist.

For example, `/online` becomes this:

<figure markdown>
  ![Picture on how `/online` looks when the toggle is enabled.](fetch_devices.png){ width="420" loading="lazy"}
</figure>

This does slow the bot down a bit when fetching the device[^1], and privacy settings may make some users not have information regardless[^2], but can used as an extra moderation/statistical tool.

This is also available as a toggle to non-Premium users of `/online` (and only `/online`) if they vote for the bot.

### Reoccurring Leaderboard

Instead of having to manually run `/leaderboard` every time you want to see the leaderboard, you can have it automatically run every day, every week, every other week, or every month in a specified channel. This can be configured through `/premium reoccurring-leaderboard`.

<figure markdown>
  ![Picture on how the reoccurring leaderboard looks when sent.](reoccurring_lb.png){ width="375" loading="lazy"}
</figure>

After configuration, the bot will send out a leaderboard with a specified period (last X days) at the frequency set, showing roughly the top 20 players (or less, if there were fewer people on that week). This can be used to give rewards for active players, or just to see who's been on the most.

### Realm Session Export

You can export your Realm's session data (a session being a period of time where the player was on a Realm, including when they joined and were last seen) for around the last 30 days to a CSV file (through `/premium export`), which can be opened in a spreadsheet program like Excel or Google Sheets. This can be used to make your own graphs (though some fiddling around will be needed), or just to have the data for yourself.

<figure markdown>
  ![Picture on how that data is sent.](export_data.png){ width="750" loading="lazy"}
</figure>

### Voting Bypass

Any features that require voting (large graphs, `/online` with device information, `/leaderboard`) can be bypassed if you have Premium. This is useful if you want to use those features without having to vote every 12 hours.

## How to Get Playerlist Premium

**You can no longer purchase Playerlist Premium because the bot will be shutting down in December.**

If you purchased Playerlist Premium through the Premium Dashboard, you can manage it [with this link](https://rpldash.astrea.cc/premium/).

If you purchased Playerlist Premium through the Discord Bot Store, you can manage it [through Discord](https://support.discord.com/hc/en-us/articles/360017693772-Managing-Subscriptions-and-Billing-FAQ).


[^1]: This requires bypassing certain parts of the bot (its cache) to get up-to-date information, hence the slowdown.
[^2]: If users are offline on Xbox Live, their device won't appear. There may be settings that also make the user not share their current game details.
