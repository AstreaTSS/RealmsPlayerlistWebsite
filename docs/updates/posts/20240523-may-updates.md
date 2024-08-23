---
date: 2024-05-23
authors:
  - astrea
categories:
  - Updates

description: An update post for May 2024, noting performance benefits and feature tweaks.
comments: true
---

# Update Post - May 2024

Long time no see, huh? Admittedly, being a one person team, it is a bit draining to work on the bot, especially when I have other things to do. However, the bot's still being actively worked on: here's a few updates since December about what's been improved and changed.

<!-- more -->

(Spoiler alert: there's no new features. Kind of.)

## Realms Playerlist Zero

The biggest change in this update is the introduction of the alpha (beta?) version of the bot, Realms Playerlist Zero! This version of the bot will be used as a testing ground for new features, and will be updated more frequently than the main bot. Of course, this means that it may be less stable than the main bot, but it will allow me to test new features and changes more easily.

!!! warning "Before You Invite"
    - Realm Playerlist Zero, by nature, will receive features fast and not very tested. As such, it may be down more often or suffer more bugs than the main bot.
    - Data is separate from the main bot, and may be occasionally be wiped at any time (although I will try to avoid this).
    - Since data is separate, you can use both the main bot and Realm Playerlist Zero at the same time. This means you can have two Realms on one server through this... but I don't recommend it.
    - If you have [Playerlist Premium](premium.md), your Premium code will not work on Realm Playerlist Zero. You will need to get a different code for it - you can do that by [joining the support server](https://discord.gg/NSdetwGjpK) and asking for one through `〉pl-premium-support`.

    If you're okay with all of the above, you can invite the bot [from this link](https://discord.com/api/oauth2/authorize?client_id=1118750188778045560&permissions=309238025280&scope=applications.commands%20bot).

<figure markdown>
  ![A picture of Realm Playerlist Zero's /about.](rpl_zero.png){ width="550" loading="lazy"}
  <figcaption>The /about for Realm Playerlist Zero. Looks a bit small right now.</figcaption>
</figure>

## Self-Hosting Guide

After years of people asking for it, I've finally written a guide on how to self-host the bot. You can find it [right here](self_hosting.md), although be warned that it is a bit technical and complex.

## Performance Improvements

There's a lot of little improvements that added over time, but the biggest ones are:
- `/leaderboard` now should be faster (by quite a bit for large Realms with the 30 days option) to run, though will be a bit slower while switching pages. This is because the bot now only fetches the gamertags of the people on the current page of the leaderboard, instead of fetching them all at once.
- Autorunners have been tweaked so that they should be a bit faster to run, and should be more reliable in general. This is because all of the autorunners now are ran at the same time instead of being run in batches.[^1]
- Many commands that have to fetch data should be a *little* bit faster due to optimizations with how the bot queries data.[^2]

## Other Changes

- `/leaderboard` will now always have a select menu no matter how many pages it generates, although the select menu can only show 25 pages at a time.
- The Live Online List now displays a special message when the bot detects the linked Realm is offline.
- `/config help` now also links the [features page](features.md), adding to the previous link for the [Server Setup Guide](server_setup.md).
- `/support` now also links the [FAQ](faq.md), adding to the previous link for the [support server](https://discord.gg/NSdetwGjpK).
- The bot now has a basic test suite to test out features of the bot to make sure they don't break. It doesn't cover much of the bot, but it's a good first step.

[^1]: This wasn't done before as the autorunners used to break with that many running, but backend changes have made it so that they can all run at once now.
[^2]: This comes down to enabling features with the ORM I'm using and monkeypatching (replacing) some functions of it to be faster.