---
date: 2024-06-06
authors:
  - astrea
categories:
  - Updates

description: An update post for Early June 2024.
---

# Update Post - Early June 2024

Hello! I've been working on the bot over the past week or two, and already have a few things to show for it.
**All of these changes are on Realm Playerlist Zero only for now, and will come to the main bot after some time.**
<!-- more -->
As a reminder, Zero is the new beta testing bot that will receive features faster than the main bot, but may be less stable. You can check out [the last update post](052324-may-updates.md#realms-playerlist-zero) for more information on it.

## Nicknames

Nicknames are now a thing! You can set a nickname for a player with `/nickname set <Xbox gamertag> <nickname>`, and remove it with `/nickname remove`. This will replace this gamertag in most commands with the nickname you set. Feel free to use this however you want!

There is currently a limit of 10 people per server, which you can keep track of through `/nickname list`:

<figure markdown>
  ![An example of /nickname list. There is one censored player who has been nicknamed to "Test".](nicknames.png)
</figure>

The 10 people limit may get adjusted as time goes on.

## Merging the Link Realm Commands

For quite a while now, there have been two methods for linking a Realm, and two commands to handle each of those methods - `/config link-realm` and `/config alternate-link`. However, I don't wish for people to think the "alternate link" method isn't as good as the "normal" method, so I've merged the two commands into one: `/config link-realm`.

As you use the new `/config link-realm`, you'll notice how the command asks you which method you wish to use (either a Realm code/link or direct linking). These methods are the same as the old ones, though using a Realm code/link is a little bit different now.

## Security Check

Also for a while, I've been testing out a new check when linking a Realm via a Realm code/link, and in Zero, it's finally being turned on for everyone. This check will make sure that you are the owner or an operator of the Realm in question before linking it, and will prevent you from linking a Realm you don't have access to.

To do this, the bot has to *temporarily* establish some connection from your Xbox account to your Discord account. There are two methods for this - either you temporarily link your Xbox account a la the direct link/`alternate-link` method, or you DM the Xbox account of the bot a specific code. Both will only store the connection between the two accounts for the command itself, and will not be stored after the command is done. You can verify this by checking the source code yourself [(`/config link-realm` starts here, you may need to hop around the code a bit)](https://github.com/AstreaTSS/RealmsPlayerlistBot/blob/81b5f48126d08239d306ba8bf3cd3b1becabac64/exts/guild_config.py#L386).

<figure markdown>
  ![An example of the new security check.](security_check.png){ width="650" loading="lazy"}
</figure>

I do want to apologize if you have any issues with this check, but I believe it is necessary to prevent abuse of the bot. If you have any issues with it, please let me know in the [support server](https://discord.gg/NSdetwGjpK).