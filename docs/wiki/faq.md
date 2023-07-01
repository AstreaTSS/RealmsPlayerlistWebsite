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

Nope. This uses Realm-specific services. For servers (both editions), you can get away with plugins/mods; for Java Edition, there *is* a Java Realm service that someone could use if they're interested enough.

### What about other Realm-based bots? Why should I use your bot?

First off: *The Playerlist Bot is not a direct competitor to those bots.* You can think of this bot as a *companion* to your bot of choice. In fact, on the support server, we're partnered with a couple - check them out there!

The Playerlist Bot does one thing very well - track and showcase the join/leaves of players. Not many bots do this on the level of the Playerlist Bot due to the sheer complexity of it all, and they likely won't do it at the *speed* the Bot does it at.

Most bots instead either focus on more direct means of moderation (IE providing global banlists), controlling and viewing the Realm from Discord itself, or both. They're all great bots because of those features, but those features don't devalue the Playerlist Bot.

It's also worth noting:
- This bot *does not* require using your or an alternate account to do its job. It uses a single bot-owned account to do its work instead, and doesn't even take up a player slot being on the Realm itself.
- The bot is open source under the GNU General Public License v3.0[^3], and *will* always be open source. In general, the bot promotes collaboration with whoever it can find, and is the reason we have partnerships with other bots.

### Why can't it track a Realm's chat?

A couple of reasons:
- It's difficult (at least with the programming language I'm using). It's a huge time investment to make it work, and it would change how the bot's fundamentals a decent bit.
- Even if I *do* get it to work, it requires a dummy account to *always* be on the Realm, thus taking up a player space. This is something I'm against doing ever.[^4]
- Frankly, it's out of scope for the bot. It would be nice, but the bot mostly tracks player join/leaves in order to not reinvent the wheel and allow for easier maintainability (the bot is largely written by one person, so maintainability is key).
- Many other bots, like [the Realm Bot](https://realmbot.dev/), offer this feature (usually through a premium version or with restrictions).

### Can I link multiple Realms to one Discord server? Can I have two playerlist channels, each one being linked to a different Realm?

Nope. It would be a nice feature admittedly, and I've gotten plenty of people asking, but...

- It would be a pain to go into the code for the bot to make it work, as the bot very much assumes and abuses the fact that there is only one Realm per Discord server.
- Even if it was supported, it would create additional strain on the bot, and most likely be a Premium feature.

Your best bet is to just have two servers, one per Realm. This idea is most likely not ever going to happen, but it may in the far future.

## Troubleshooting

### Help! The playerlist/online command isn't working!

Well, this could be due to a number of reasons:
- For the autorunner version: was anyone on the Realm during that time? If there was no one, then the bot will not autorun the list during that time.
- Did you accidentally kick the account responsible for keeping track of the Realm? Did you decide to change which Realm a "Realm" is using? Try relinking it via `/config link-realm`!
- Did it spit out an error? I'll already have the error and more information, so don't worry about that.
- Something else? Honestly, relinking usually fixes the problem anyways. Taking a look at `/config info` and seeing if anything's off is a good idea though.

### There's a user called "Account with XUID (insert numbers here)" on the list. Who's that?

Well, that happens when the bot fails to convert what can essentially be called Xbox's IDs into its respective gamertag. Let me explain.

You may have heard of a Discord ID - it's a bunch of numbers that represents a thing on Discord, like a user, a channel, or a role (we'll be focusing on users). These numbers are useful because trying to use names means we can have conflicts - there's *definitely* more than one user named "Hawk" out there[^5], after all. Instead of referring to a user by name, Discord tools (and Discord itself) refers to users by their ID, with their usernames basically being a thing only people see.

A similar concept is present in Xbox Live, which is used a lot with Realms (and Bedrock Edition in general). "Gamertags" can be thought up as usernames here, and "XUID"s are like Discord IDs.

The methods the bot uses to keep track of people gets the *XUIDs* of people. This isn't useful for most people, though, and so the bot has to find out what a person's gamertag is based off their XUID. While this resolving works *most* of the time, there are times where it fails, which is when this question comes into play.

To reliably get the gamertag of the XUID shown, you can use `/gamertag-from-xuid`, which uses several (possibly slow, and so not used in the bot at large) methods to make sure you actually get the gamertag.

## Technical

### Can I self-host this?

...yes, but I can only wish you luck. This thing is *far* from simple to get everything working, requiring you to know the ins-and-outs of most of the libraries I use.[^6] It can be a mess, and gathering the databases and servers needed even more so. There's also not much room for simplification here. If you do want to continue, it's best if you have a decent understanding at Python, PostgreSQL, Redis, and Sentry.io before trying this.

For the Xbox/Realm related parts, [this Xbox API library](https://github.com/OpenXbox/xbox-webapi-python)'s little introduction section (up to "Dependencies") should tell you the first steps of what to do - [this little script](https://github.com/AstreaTSS/RealmsPlayerlistBot/blob/main/xbox_authenticate.py) included in the source code of the bot can do the rest (once you install dependecies for the bot). In general, everything the bot uses can be gotten for free in some way, shape, or form.[^7]

Little support will be given for self-hosters (not trying to sound cruel, but it takes away at my time. That being said, if you know what you're doing, I can help you with troubleshooting). I *do* plan on making a guide on how to host it eventually though.

### What programming language does this use?

Python. It's slow (though there a lot of tricks to make it faster), but I'm *very* familiar with it. It's my language of choice for Discord bots in general, so that helps.

Note that Python is *not* like Javascript, the most popular language for making small bots. There are some fundamental differences between them.[^8]

### Why is this bot so complex?

A lot of reasons:
- The Xbox/Realm API (they're essentially the same thing, being made by Microsoft) is a pain to work with. There's a reason why people have made tools like [OpenXBL](https://xbl.io/) or [XAPI](https://xapi.us/) - there's a lot of pain points when it comes to *just authenticating into the APIs themselves*, and it's a lot easier to just let someone else do that work[^9]. Unforunately, it comes at a speed cost, and also has limits that would be too restrictive for Playerlist[^10]. Instead, we do everything ourselves, adding a lot of complexity.
  - Now, [there is an Xbox API library made in Python](https://github.com/OpenXbox/xbox-webapi-python), as discussed in an earlier question, and it does help shed some light on how the whole process works. However, that library is very obtuse (having several questionable design choices)[^11] and is slower than it could be for many reasons[^12], so I've had to make mini-libraries in the bot itself that do it better. Of course, it doesn't handle the Realms API either, though that's not its fault.
  - Even *when* you log in, the Xbox/Realm API is just a mess. A lot of inconsistency with capitalization that makes it a pain to parse, lots of undocumented fields and behaviors (90% of the bot's code uses undocumented endpoints), and general inconsistency with the results you get. I very much sense Microsoft made the API when they were new to making APIs, and is unable to improve it due to how many things that would break.[^13] That and they really do not like simple authentication.
  - Oh yeah, the APIs just *fail* sometimes. Like, it's a completely normal thing and you can't do anything about it.[^14]
- There's a lot of processing involved. Not just with the APIs, but also with the data gotten from it - it all eventually has to be converted into a format that is usable by the bot, which takes some effort. It also has to be *fast*, which takes even more effort to do (speed is the reason Redis is used, for example).[^15]
- Even when the data is stored, it has to be turned into a human-friendly format, which takes yet more work. It's more complex than you think.[^16]
- Some pains were taken to make the commands more user-friendly at the exchange of more complex code. It's just how it is.

[^1]:
    Yes, the bot polls the service *every minute*. Mojang seems fine with it for my bot specifically, but be careful about doing this for your own projects - the
    account behind the bot has been banned before for this very reason.
[^2]:
    To be more specific: every Realm has a thing called a "club", which is used to store photos and messgaes in the activity log of the Realm. The bot can usually
    exploit this to gain past data, though clubs are a weird thing.
[^3]:
    This very website is *also* open source, under MIT, [as you can see on the GitHub page](https://github.com/AstreaTSS/RealmsPlayerlistWebsite). Only the Premium
    Dashboard for this bot *isn't* open source yet, and that's because it's an experimental project that has security involved. Can you tell I like open source?
[^4]:
    Not because it's a horrible idea or anything. In fact, the Realm Bot does it for its premium service. I just rather provide services that don't need a player
    on for convenience's (for you and me) sake and to distinguish the Playerlist Bot from other bots.
[^5]: Though the system post-discriminators does mean there's only one @Hawk - still, an ID is easier for programs to use for various reasons (computers love numbers).
[^6]: "Ins-and-outs" may be the wrong word here. The bot just requires decent knowledge of Python in general.
[^7]:
    Redis gives you a free 20 MB cluster through their cloud service, Supabase and CockroachDB provide good free tiers for Postgres, Sentry.io is free for one project,
    Xbox Live accounts are free, and Python and the dependencies used in this project are free. Hosting the bot may require some looking, but there are services
    which'll host a small bot for free (usually with a credit card, though a very select few do it without).
[^8]: This line was added more for self-hosters so that they know what they're getting into more than anything.
[^9]: There are no tools like the two listed for the Realms API.
[^10]: OpenXBL is still used as a fallback because of how... weird the Xbox API can be.
[^11]: Purely my opinion, I know, but it is seriously one of the worst libraries I have used development-wise because of how it is designed. Not like it's used anymore.
[^12]: 
    Namely with its lack of support for `orjson` or any alternative to the very slow `json`, its usage of `httpx` over `aiohttp` (granted, `httpx` has a better UX),
    and its overall bloated design.
[^13]: Perhaps this is too nice of an assumption - even their more recent additions have the same issue.
[^14]: By all means, any API is bound to have 5XX errors every once in a while. It's a *daily* occurance for the Xbox/Realms API.
[^15]: Speed is also why the bot *has* a Premium tier - there's no way I could offer those benefits at scale with the speeds the bot has right now.
[^16]:
    More specically, the bot gets and stores players in the form of XUIDs - as mentioned earlier, those are Xbox's version of Discord IDs. Fetching has to be done
    to get the gamertag of those XUIDs, and Microsoft *really* didn't design either of the APIs with the sheer amount we need to fetch in mind. As of the right now,
    the bot uses a combination of excessive caching and an undocumented endpoint that is more supportive of the bot's workload to do the work.
