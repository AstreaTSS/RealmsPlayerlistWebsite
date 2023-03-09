# Frequently Asked Questions

## General

### What is this bot?

Well, like the `README` says: it's a bot that helps out owners of Minecraft: Bedrock Edition Realms by showing various statistics related to player join/leaves. The `README` has more information about that, though.

### How does it work?

Basically, the bot uses a [hidden little service](https://wiki.vg/Bedrock_Realms) that Bedrock Realms have, allowing anyone to get specific information about Realms if they know what they're doing. One piece of information we can get is a list of people online for *every* Realm an account is in at any one moment, which the bot essentially constantly polls in order to generate its list.

The hard part is actually *parsing* that data - again, you can only get every Realm at any one moment, so you have to poll it constantly in order to generate minute-to-minute data. There's also quite a bit of difficulty involving making the data human-readable for various reasons, including displaying players in a friendly format.

When you initially link your server to a Realm though, it uses a different method that is less reliable than the service, but is able to get data from the past. This is why the initial data may be inaccurate.

### Does this work on Bedrock servers? What about Java Edition Realms and servers?

Nope. This uses Realm-specific services. For servers (both editions), you can get away with plugins/mods; for Java Edition, there *is* a Java Realm service that someone could use if they're interested enough.

### What about the Realm Bot?

[I'm referring to this bot](https://realmbot.dev/), by the way. We're officially partnered with them too, check them out!

Anyways, that bot is great - it's a bot that can *massively* help out any Realm owners, and I won't deny that. In fact, it even has its own version of the `/online` command this bot has, which can be a little bit more accurate at times for technical reasons.

However, the Realm Playerlist Bot is not a "remote Realms control" bot (unlike Realm Bot). As the name suggest, the Playerlist Bot is a *tracking* bot, meant to take care of the workload of tracking players for whatever reasons you need. The Realm Bot cannot do anything like this, and so you can treat this bot as a *companion* to it, not a competitor.

I have doubts that the Realm Bot will be able to do what this bot does because of how complex it is. Regardless, use what you want to use, and there's no harm in having both.

(Note that the Realm Bot has `/realm players`, which is essentially Playerlist's `/online`. However, that produces different and usually less accurate data than `/online` due to a number of technical reasons.)

### Why can't it track a Realm's chat?

A couple of reasons:
- It's a bit difficult. There is a way out there, but it currently only works for *one single Realm-to-Discord server combination* unless you do a number of things to work around it. It's a huge time investment to make it work, and it would change how the bot is used by a decent bit.
- Even if I *do* get it to work, it requires a dummy account to *always* be on the Realm, thus taking up a player space. This is something I'm against doing ever.
- Frankly, it's out of scope for the bot. It would be nice, but the bot mostly tracks player join/leaves in order to not reinvent the wheel and allow for easier maintainability (the bot is largely written by one person, so maintainability is key).
- [The Realm Bot](https://realmbot.dev/) offers this feature in its premium version.

## Troubleshooting

### Help! The playerlist/online comamnd isn't working!

Well, this could be due to a number of reasons:
- For the autorunner version: was anyone on the Realm during that time? If there was no one, then the bot will not autorun the list during that time.
- Did you accidentally kick the account responsible for keeping track of the Realm? Did you decide to change which Realm a "Realm" is using? Try relinking it via `/config link-realm`!
- Did it spit out an error? I'll already have the error and more information, so don't worry about that.

### There's a user called "Account with XUID (insert numbers here)" on the list. Who's that?

Well, that happens when the bot fails to convert what can essentially be called Xbox's IDs into its respective gamertag. Let me explain.

You may have heard of a Discord ID - it's a bunch of numbers that represents a thing on Discord, like a user, a channel, or a role (we'll be focusing on users). These numbers are useful because trying to use names means we can have conflicts - there's *definitely* more than one user named "Hawk" out there, after all. Instead of referring to a user by name, Discord tools (and Discord itself) refers to users by their ID, with their usernames basically being a thing only people see.

A similar concept is present in Xbox Live, which is used a lot with Realms (and Bedrock Edition in general). "Gamertags" can be thought up as usernames here, and "XUID"s are like Discord IDs.

The methods the bot uses to keep track of people gets the *XUIDs* of people. This isn't useful for most people, though, and so the bot has to find out what a person's gamertag is based off their XUID. While this resolving works *most* of the time, there are times where it fails, which is when this question comes into play.

To reliably get the gamertag of the XUID shown, you can use `/gamertag-from-xuid`, which uses several (possibly slow) methods to make sure you actually get the gamertag.

## Technical

### Can I self-host this?

...yes, but I can only wish you luck. This thing is *far* from simple to get everything working, requiring you to know the ins-and-outs of most of the libraries I use. It can be a mess, and gathering the databases and servers needed even more so. There's also not much room for simplification here. If you do want to continue, it's best if you have a decent understanding at Python, PostgreSQL, Redis, and Sentry.io before trying this.

[This Xbox API library](https://github.com/OpenXbox/xbox-webapi-python) is a good place to start researching on how it all works, as you'll need it to generate tokens to authenticate. Everything the bot uses can be gotten for free in some way, shape, or form.

Little support will be given for self-hosters (not trying to sound cruel, but it takes away at my time. That being said, if you know what you're doing, I can help you with troubleshooting). I *do* plan on making a guide on how to host it eventually though.

### What programming language does this use?

Python. It's slow (though there a lot of tricks to make it faster), but I'm *very* familiar with it. It's my favorite commonly-used language, so that helps.

Note that Python is *not* like Javascript, the most popular language for making small bots. There are some fundamental differences between them.

### Why is this bot so complex?

A lot of reasons:
- The Xbox/Realm API (they're essentially the same thing, being made by Microsoft) is a pain to work with. There's a reason why people have made tools like [OpenXBL](https://xbl.io/) or [XAPI](https://xapi.us/) - there's a lot of pain points when it comes to *just authenticating into the APIs themselves*, and it's a lot easier to just let someone else do that work. Unforunately, it comes at a speed cost, and also has limits that would be too restrictive for Playerlist. Instead, we do everything ourselves, adding a lot of complexity.
  - Now, [there is an Xbox API library made in Python](https://github.com/OpenXbox/xbox-webapi-python), as discussed in an earlier question, and it does help shed some light on how the whole process works. However, that library is very obtuse (having several questionable design choices that go against the core of Python) and is slower than it could be for many reasons, so I've had to make mini-libraries in the bot itself. The library is still used, but mostly for a couple of convenience functions these days, and soon it will be removed entirely.
  - Even *when* you log in, the Xbox/Realm API is just a mess. A lot of inconsistency with capitalization that makes it a pain to parse, lots of undocumented fields and behaviors (90% of the bot's code uses undocumented endpoints), and general inconsistency with the results you get. I very much sense Microsoft made the API when they were new to making APIs, and is unable to improve it due to how many things that would break. That and they really do not like simple authentication.
  - Oh yeah, the APIs just *fail* sometimes. Like, it's a completely normal thing and you can't do anything about it.
- There's a lot of processing involved. Not just with the APIs, but also with the data gotten from it - it all eventually has to be converted into a format that is usable by the bot, which takes some effort. It also has to be *fast*, which takes even more effort to do (speed is the reason Redis is used, for example).
- Even when the data is stored, it has to be turned into a human-friendly format, which takes yet more work. It's more complex than you think.
- Some pains were taken to make the commands more user-friendly at the exchange of more complex code. It's just how it is.