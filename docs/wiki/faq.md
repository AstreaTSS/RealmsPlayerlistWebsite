---
description: Frequently asked questions about the Realms Playerlist Bot.
---

# Frequently Asked Questions

## General

### What is this bot?

Well, like the [home page](../../index.html) says: it's a bot that helps out owners of Minecraft: Bedrock Edition Realms by showing various statistics related to player join/leaves. The home page has more information about that, though.

### How does it work?

Basically, the bot uses a [hidden little service](https://wiki.vg/Bedrock_Realms) that Bedrock Realms have, allowing anyone to get specific information about Realms if they know what they're doing. One piece of information we can get is a list of people online for *every* Realm an account is in at any one moment, which the bot essentially constantly polls in order to generate its list.

The hard part is actually *parsing* that data - again, you can only get every Realm at any one moment, so you have to poll it constantly in order to generate minute-to-minute data.[^1] There's also quite a bit of difficulty involving making the data human-readable for various reasons, including displaying players in a friendly format.

When you initially link your server to a Realm though, it uses a different method that is less reliable than the service[^2], but is able to get data from the past. This is why the initial data may be inaccurate.

### Does this work on Bedrock servers? What about Java Edition Realms and servers?

Nope. This uses Bedrock Realms specific services, and will never expand out to other versions/servers.

For Java Edition, if you're running a server, you *should* be running something that isn't a vanilla server (IE Fabric or Paper) and so should have options for full chat tracking, including joins/leaves. For Realms, [there *is* a service for them](https://wiki.vg/Realms_API) - I can't verify if it would work for a player tracking bot, but it's worth a shot.

For Bedrock servers, you may have luck with special addons or plugins - I've found addons like [BedrockBridge](https://bedrockbridge.esploratori.space/) out there (not affiliated), and I'm sure there's many more.

### What about other Realm-based bots? Why should I use your bot?

First off: *The Playerlist Bot is not a direct competitor to those bots.* You can think of this bot as a *companion* to your bot of choice. In fact, on the support server, we're partnered with a couple - check them out there!

The Playerlist Bot does one thing very well - track and showcase the join/leaves of players. Not many bots do this on the level of the Playerlist Bot due to the sheer complexity of it all, and they likely won't do it at the *speed* the Bot does it at.

Most bots instead either focus on more direct means of moderation (IE providing global ban lists), controlling and viewing the Realm from Discord itself, or both. They're all great bots because of those features, but those features don't devalue the Playerlist Bot.

It's also worth noting:
- This bot *does not* require using your or an alternate account to do its job. It uses a single bot-managed account to do its work instead, and doesn't even take up a player slot being on the Realm itself.
- The bot is open source under the GNU Affero General Public License v3.0[^3], and *will* always be open source. In general, the bot promotes collaboration with whoever it can find, and is the reason we have partnerships with other bots.

### Why can't it track a Realm's chat?

A couple of reasons:
- The Bedrock Realm specific services the bot uses does not allow for this. To work around this, the bot would have to *be on the Realm,* listening to the chat as its received.
  - Of course, this means a slot would be taken up by a bot account. Being realistic, this would mean *you making an alt account* (or me making a bunch of them) to do this, which is a pain. Also, it taking up a slot is something I'm against doing ever.[^4]
  - It's difficult, at least with the programming language I'm using. It's a huge time investment to make it work, especially with how low level it would be.
- Frankly, it's out of scope for the bot. It would be nice, but the bot mostly tracks player join/leaves in order to not reinvent the wheel and allow for easier maintainability (the bot is largely written by one person, so maintainability is key).
- Many other bots, like [the Realm Bot](https://realmbot.dev/) and [UniqueShield](https://discord.gg/WAmKwkewgH) offer this feature (usually through a premium version or with restrictions).

### Can I link multiple Realms to one Discord server? Can I have two playerlist channels, each one being linked to a different Realm?

Nope. It would be a nice feature admittedly, and I've gotten plenty of people asking, but...

- It would be a pain to go into the code for the bot to make it work, as the bot very much assumes and abuses the fact that there is only one Realm per Discord server (though it *does not* assume the opposite - feel free to have multiple Discord servers tracking one Realm if you really want to).
- Even if it was supported, it would create additional strain on the bot, and most likely be a Premium feature.

Your best bet is to just have two servers, one per Realm. This idea is most likely not ever going to happen, but it may in the far future.

### Where can I find information about updates? What's your update policy like?

There are two places you can find updates - the [updates page](../../updates/index.html) and the [support server](https://discord.gg/NSdetwGjpK). The updates page always will contain new features and major adjustments, but the support server will also contain bug fixes and other miscellaneous announcements (IE downtime announcements) that you may find useful.

Unlike some other bots, there are no version numbers or the like associated with each update - the bot has *rolling updates*, and so routinely gets updates as things are [committed to the GitHub repository](https://github.com/AstreaTSS/RealmsPlayerlistBot). Most of these updates, especially if they're minor bugfixes or the like, get quietly pushed out without any announcement - the bot may be down for 1-2 minute intervals sporadically due to this.[^5] Most major features are quietly dropped in these rolling updates and then later announced when I determine them to be stable - this is so I have enough time to gather and fix bugs if needed.

## Troubleshooting

### Help! The playerlist/online command isn't working!

Well, this could be due to a number of reasons:
- For the autorunner version: was anyone on the Realm during that time? If there was no one, then the bot will not autorun the list during that time.
- Did you accidentally kick the account responsible for keeping track of the Realm? Did you decide to change which Realm a "Realm" is using? Try relinking it - you can follow [the Server Setup Guide](server_setup.md) for how to do that.
- Did it spit out an error? I'll already have the error and more information, so don't worry about that.
- Something else? Honestly, relinking usually fixes the problem anyways. Taking a look at `/config info` and seeing if anything's off is a good idea though.

### There's a user called "Account with XUID (insert numbers here)" on the list. Who's that?

Well, it's first worth explaining that that happens when the bot fails to convert Xbox (or, well, Microsoft) IDs into its respective gamertag. Let me explain.

You may have heard of a Discord ID - it's a bunch of numbers that represents a thing on Discord, like a user, a channel, or a role (we'll be focusing on users). These numbers are useful because computers *much* prefer numbers over text - this allows accounts to have better performance and also allows flexibility with naming systems[^6]. Instead of referring to a user by name, Discord tools (and Discord itself) refers to users by their ID, with their usernames basically being a thing only people see.

A similar concept is present in Xbox Live, which is used a lot with Realms (and Bedrock Edition in general). "Gamertags" can be thought up as usernames here, and "XUID"s are like Discord IDs.

The methods the bot uses to keep track of people gets the *XUIDs* of people. This isn't useful for most people, though, and so the bot has to find out what a person's gamertag is based off their XUID. While this resolving works *most* of the time, there are times where it fails, which is when this question comes into play.

To reliably get the gamertag of the XUID shown, you can use `/gamertag-from-xuid`, which uses several (possibly slow, and so not used in the bot at large) methods to make sure you actually get the gamertag.

### The bot displays an "Unknown Player" on the list. Who's that?

There's a variety of people it could be - "Unknown Player" is used when the bot is unable to get *any* information on a player, even their Xbox ID. This most often happens because said player is a *subclient* - basically, whenever a player uses splitscreen to let another player play on the same device, then the player that's not the host is a subclient. Subclients are impossible to track with the means the bot uses - they don't have Xbox IDs (with Mojang giving them an unhelpful placeholder of "0", not even identifying who they're subclienting off of), and they don't have gamertags. They're just... there.

Of course, there could be other reasons why that appeared (IE bugs), but those are rarer.

### The bot unlinked itself and stopped tracking my Realm and/or sending out the autorunning playerlist! Is this a bug?

This is very likely not a bug - usually, this happens because of an intended mechanic of the bot.

The bot will automatically unlink itself after *7 days of not seeing any join/leave activity on your Realm.* This happens often because either a Realm closes, the account behind the bot was banned, or a Realm was simply that inactive. The bot tries to send warnings about this lack of inactivity far beforehand, but if you have no autorunning playerlist, this warning will not appear. There is also a setting that turns off these warnings (`/config realm-warning`), but the unlinking itself will still happen after 7 days - it's usually a better idea to keep the warnings on so you have a better idea of the time you have left.

This is done so that the bot's processing power and storage are not spent trying to gather inactive Realms, and so will not be removed. If your Realm was active, check that the account wasn't banned or kicked. If your Realm isn't active, unforunately, there isn't a way to exempt yourself from the check. In any case, you should be able to go through the [setup process again](server_setup.md) to re-enable the bot.

There is also a similar behavior specific to the autorunning playerlist and any notification channels - if the bot has tried 3 times to send a message to the channel and has failed due to a non-outage fault (IE permissions became invalid or the channel was deleted), then it will unlink the playerlist. Please check that the channel you want to use actually exists and that the bot has permissions to Read and Send Messages and Embed Links. Once again, if this unlinking happens to you, you can simply re-link the channel.

### There's another problem not answered here. Where can I ask about it?

In the [support server](https://discord.gg/NSdetwGjpK), of course! You can also ask for features there.

## Technical

### Can I self-host this?

...yes, but I can only wish you luck. This thing is *far* from simple to get everything working, requiring you to know the ins-and-outs of most of the libraries I use.[^7] It can be a mess, and gathering the databases and servers needed even more so. There's also not much room for simplification here. If you do want to continue, it's best if you have a decent understanding at Python, PostgreSQL, Redis, and Sentry.io before trying this.

For the Xbox/Realm related parts, [my custom Xbox/Bedrock Realms library](https://github.com/AstreaTSS/elytra-ms)'s little setup section should tell you what to do (worth noting that the oauth file you get from `elytra-authenticate` needs to be named `tokens.json` for backwards compatibility). In general, everything the bot uses can be gotten for free in some way, shape, or form.[^8]

Little support will be given for self-hosters (not trying to sound cruel, but it takes away at my time. That being said, if you know what you're doing, I can help you with troubleshooting). I *do* plan on making a guide on how to host it eventually though.

### What programming language does this use?

Python. It's slow (though there a lot of tricks to make it faster), but I'm *very* familiar with it. It's my language of choice for Discord bots in general, so that helps.

Note that Python is *not* like JavaScript, the most popular language for making small bots. There are some fundamental differences between them, so please note that if you decide to contribute or self-host.[^9]

### Why is this bot so complex?

A lot of reasons:
- The Xbox/Realm API (they're essentially the same thing, being made by Microsoft) is a pain to work with. There's a reason why people have made tools like [OpenXBL](https://xbl.io/) or [XAPI](https://xapi.us/) - there's a lot of pain points when it comes to *just authenticating into the APIs themselves*, and it's a lot easier to just let someone else do that work[^10]. Unfortunately, it comes at a speed cost, and also has limits that would be too restrictive for Playerlist[^11]. Instead, we do everything ourselves, adding a lot of complexity.
  - Now, [there is an Xbox API library made in Python](https://github.com/OpenXbox/xbox-webapi-python), as discussed in an earlier question, and it does help shed some light on how the whole process works. However, that library is very obtuse (having several questionable design choices)[^12] and is slower than it could be for many reasons[^13], so I've had to make mini-libraries in the bot itself that do it better. Of course, it doesn't handle the Realms API either, though that's not its fault.
  - Even *when* you log in, the Xbox/Realm API is just a mess. A lot of inconsistency with capitalization that makes it a pain to parse, lots of undocumented fields and behaviors (90% of the bot's code uses undocumented endpoints), and general inconsistency with the results you get. I very much sense Microsoft made the API when they were new to making APIs, and is unable to improve it due to how many things that would break.[^14] That and they really do not like simple authentication.
  - Oh yeah, the APIs just *fail* sometimes. Like, it's a completely normal thing and you can't do anything about it.[^15]
- There's a lot of processing involved. Not just with the APIs, but also with the data gotten from it - it all eventually has to be converted into a format that is usable by the bot, which takes some effort. It also has to be *fast*, which takes even more effort to do (speed is the reason Redis is used, for example).[^16]
- Even when the data is stored, it has to be turned into a human-friendly format, which takes yet more work. It's more complex than you think.[^17]
- Some pains were taken to make the commands more user-friendly at the exchange of more complex code. It's just how it is.

[^1]:
    Yes, the bot polls the service *every minute*. Mojang seems fine with it for my bot specifically, but be careful about doing this for your own projects - the
    account behind the bot has been banned before for this very reason.
[^2]:
    To be more specific: every Realm has a thing called a "club", which is used to store photos and messages in the activity log of the Realm. The bot can usually
    exploit this to gain past data, though clubs are a weird thing.
[^3]:
    This very website is *also* open source, under Apache License 2.0, [as you can see on the GitHub page](https://github.com/AstreaTSS/RealmsPlayerlistWebsite). Only the Premium
    Dashboard for this bot *isn't* open source yet, and that's because it's an experimental project that has security involved. Can you tell I like open source?
[^4]:
    Not because it's a horrible idea or anything. In fact, the Realm Bot does it for its premium service. I just rather provide services that don't need a player
    on for convenience's (for you and me) sake and to distinguish the Playerlist Bot from other bots.
[^5]: Not all updates require the bot to restart - in fact, I try not to restart the bot as much as possible. The bot also restarts quickly, so this shouldn't affect you much.
[^6]: Of course, Discord itself, post discriminators, only uses one username per account, but it does allow other services to not do that if they want.
[^7]: "Ins-and-outs" may be the wrong word here. The bot just requires decent knowledge of Python in general.
[^8]:
    Redis gives you a free 20 MB cluster through their cloud service, Supabase and CockroachDB provide good free tiers for Postgres, Sentry.io is free for one project,
    Xbox Live accounts are free, and Python and the dependencies used in this project are free. Hosting the bot may require some looking, but there are services
    which'll host a small bot for free (usually with a credit card, though a very select few do it without).
[^9]: Not like either language is better than the other - it just so happens that most Realm bots use JavaScript while I decided not to.
[^10]: There are no tools like the two listed for the Realms API.
[^11]: OpenXBL is still used as a fallback because of how... weird the Xbox API can be.
[^12]: Purely my opinion, I know, but it is seriously one of the worst libraries I have used development-wise because of how it is designed. Not like it's used in the bot anymore.
[^13]: 
    Namely with its lack of support for `orjson` or any alternative to the very slow `json`, its usage of `httpx` over `aiohttp` (granted, `httpx` has a better UX),
    and its overall bloated design.
[^14]: Perhaps this is too nice of an assumption - even their more recent additions have the same issue.
[^15]: By all means, any API is bound to have 5XX errors every once in a while. It's a *daily* occurrence for the Xbox/Realms API.
[^16]: Speed is also why the bot *has* a Premium tier - there's no way I could offer those benefits at scale with the speeds the bot has right now.
[^17]:
    More specifically, the bot gets and stores players in the form of XUIDs - as mentioned earlier, those are Xbox's version of Discord IDs. Fetching has to be done
    to get the gamertag of those XUIDs, and Microsoft *really* didn't design either of the APIs with the sheer amount we need to fetch in mind. As of the right now,
    the bot uses a combination of excessive caching and an undocumented endpoint that is more supportive of the bot's workload to do the work.
