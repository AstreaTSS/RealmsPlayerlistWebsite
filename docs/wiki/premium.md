# Playerlist Premium and How to Get It

Hey! **Realms Playerlist Premium** is a monthly purchase you can make in order to get special features not usually obtainable. These are usually locked behind a paywall because it would be infeasible to allow everyone to use these features without making the bot as a whole suffer - by limiting the amount of users who can use them, I can still provide these features to those who need it while also earning funds necessary to keep the bot alive and running as it grows (scaling isn't cheap).

## Features

### Live Playerlist

Instead of making the bot send a summary of people on every hour, a **live playerlist** shows who joined and left a Realm every minute, basically making it a live join/leave logger.

It looks something like this (minus the obvious censoring):

<p align="center">
  <img src="../_static/live_playerlist.png" alt="Preview on how the live playerlist looks like." height=420/>
</p>

This has a variety of uses, from statistical to moderation - it's really up to you what you do with this information. I know of one Realm owner who uses it both to narrow down subjects to a precise degree while also tracking active Realm times. Using Discord's search functionality (heavily suggest looking into that if you haven't use it, by the way), the possibilities are near endless.

Of course, this is more spammy than the summary given every hour, and also *replaces the autorunner version entirely.* The `/playerlist` command will still be available to you, though, and the benefits most likely outweigh the downsides for you.

### Device Information

Through an extra toggle (`/premium fetch-devices`), the bot can fetch and display device information whenever a user is online. This affects `/online`, the normal playerlist, and the live playerlist.

For example, `/online` becomes this:

<p align="center">
  <img src="../_static/fetch_devices.png" alt="Preview on how `/online` looks when the toggle is enabled." height=420/>
</p>

This does slow the bot down a bit when fetching the device, and privacy settings may make some users not have information regardless, but can used as an extra moderation/statistical tool.

### More Options For Graphs

Free users have a limited period of how far they can go back in terms of the data graphed, and have limited options on how it can be graphs. With Premium, users can go back 30 days and graph in a variety of ways.

## How to Get Playerlist Premium

Now, you might be wondering how to get it, huh?

You'll need:
- A valid payment source.
- A Discord account that can join and stay in a server.
- Of course, a server to actually redeem Premium in. Or, well, you actually can redeem it in two servers if you want.

Anyways:

1. Head over to [my Ko-Fi page](https://ko-fi.com/astreatss) and where it says "Support Astrea", you should see options to do either a one-time purchase or for a membership. Click on the membership tag, and proceed to join the "Realms Playerlist Premium" tier, setting up your payment source and all.
    - Note that I have very little control over payments - if it doesn't get accepted by either PayPal or the card method (which is powered by Stripe), then I can't do anything.
    - I do *not* accept alternative modes of payment. Makes things a lot simplier for me.

2. Link your Discord account with Ko-Fi and join the "Astrea's Galaxy" Discord server. Annoyingly, Ko-Fi doesn't give me a good way of seeing how this step works, so bear with me and [consult this article as necessary](https://help.ko-fi.com/hc/en-us/articles/8664701197073-How-Do-I-Join-a-Creator-s-Discord-Server-).
    - You do need to make a Ko-Fi account to do all of this - if you don't have one and your purchase Premium, you should get an email that'll allow you to create an account.
    - Ko-Fi may give you a prompt to join the Discord server right after you purchase Premium. If so, that's great! Just click that button. Otherwise, you can find a "Connect to Discord & Claim" button on my Ko-Fi page, or you can find it your "Payments and Orders" tab.
    - From there, it'll likely ask you if Ko-Fi can access your Discord account - you have to agree to it to continue.
    - Hopefully, it should automatically join the server for you. If not, [you can join here](https://discord.gg/NSdetwGjpK).
    - If you wait a couple of minutes and get the "Playerlist Premium Supporter" role, you're all set for the next step!
    - Please consult the article linked at the very beginning of this page if you have any problems.

3. Once you get the "Playerlist Premium Supporter" role, you should be able to see the channel "`#〉get-playerlist-premium`" under the "Technical Side" category (where all of the bot channels are). Click on that, read the message that's in there, and open a ticket.

4. Wait for Astrea/me to respond and give you a code. **Save this code somewhere safe.** Also note that this code is tied to you *specifically*, and only you can use it.

5. On the server you want to enable Premium in, use the command `/premium redeem` and input the code you got. If it all works, the bot should tell you it was a success. Just note *you cannot undo this action, and will permanently use one of your two uses.*

And you're done! Some Premium features may still need to be enabled afterwards - for example, the live playerlist needs to be enabled by `/premium toggle-live-playerlist` before it'll start working. You can check that you still have Premium by using `/config info`.

Also, if you ever leave "Astrea's Galaxy", you'll lose Premium immediately. Sorry, just a limitation with how I verify you're still subscribed to the membership tier.