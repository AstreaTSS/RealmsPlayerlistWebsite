---
date: 2023-12-23
authors:
  - astrea
categories:
  - Playerlist Premium

description: A new feature has been added to allow you to have a reoccurring leaderboard if you're a Playerlist Premium subscriber.
---

# Reoccurring Leaderboard

A new feature has been added to allow you to have a reoccurring leaderboard sent to a channel of your choice *if you're a Playerlist Premium subscriber*. This can be used to give rewards for active players, or just to see who's been on the most.

<!-- more -->

Instead of having to manually run `/leaderboard` every time you want to see the leaderboard, you can have it automatically run every every week, every other week, or every month in a specified channel. This can be configured through `/premium reoccurring-leaderboard`.

<figure markdown>
  ![Picture on how the reoccurring leaderboard looks when sent.](reoccurring_lb.png){ width="375" loading="lazy"}
</figure>

After configuration, the bot will send out a leaderboard with a specified period (last X days) at the frequency set, showing roughly the top 20 players (or less, if there were fewer people on that week).

