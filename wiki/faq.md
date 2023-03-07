# Frequently Asked Questions

## General

### What is this bot?

Well, like the `README` says: it's a bot that keeps a log of players who joined and left for Minecraft: Bedrock Edition Realms. The `README` has more information about that, though.

### How does it work?

There are two "methods" to keep in mind. Why am I talking about these? Well, you'll see, but:
- The "Realms" method relies on a [hidden little service](https://wiki.vg/Bedrock_Realms) that Bedrock Realms have, allowing anyone to get specific information about Realms if they know what they're doing. One piece of information we can get is a list of people online for *every* Realm an account is in at any one moment, which the bot essentially constantly polls in order to generate its list.
- The "Clubs" method uses the fact that all Bedrock Realms have Xbox Clubs (basically, a little group that players can use to communicate with each other on Xbox Live); you can see this yourself by using the Xbox app and looking at your own profile if you've joined a Realm, or by using the social feed in game, which is powered by clubs. Among other things, clubs keep a list of players who are on and who *were* on, so the bot can poll that as needed.

While being set up, the bot will uses the "Clubs" method in order to get past data from before it joined the Realm. After being set up, it uses the "Realms" method to continually poll data from there. While I would *like* to use the "Clubs" method for every part, the method doesn't like to be abused, and so I can't exactly poll 50+ clubs for the playerlist at once for the version that runs every hour - who would have thought 😅. 

### Does this work on Bedrock servers? What about Java Edition Realms and servers?

Nope. Neither of the methods listed above work with those. For servers (both editions), you can get away with plugins/mods; for Java Edition, there *is* a Java Realm service that someone could use if they're interested enough.

### What about the Realm Bot?

I'm referring to [this bot](https://realmbot.dev/), by the way. We're officially partnered with them too, check them out!

Anyways, that bot is great - it's a bot that can *massively* help out any Realm owners, and I won't deny that. In fact, it even has its own version of the `/online` command this bot has, which can be a little bit more accurate at times for technical reasons.

However, the Realm Playerlist Bot is not a "remote Realms control" bot (unlike Realm Bot). As the name suggest, the Playerlist Bot is a *tracking* bot, meant to take care of the workload of tracking players for whatever reasons you need. The Realm Bot cannot do anything like this, and so you can treat this bot as a *companion* to it, not a competitor.

I have doubts that the Realm Bot will be able to do what this bot does because of how complex it is. Regardless, use what you want to use, and there's no harm in having both.

(As for *why* `/online` is less accurate than Realm Bot's `/realm players` - the Playerlist bot caches results for performance, while Realm Bot does a request each time the command is run. Note that the Playerlist requires one Xbox account to operate that you don't typically even have to see, while the Realm Bot requires you to link your account, which it'll then use for everything. Due to a number of technical reasons, this means if the Playerlist bot did a request each time the command was ran, it would have to process a *lot* more data than the Realm Bot does, which isn't ideal.)

### Why can't it track a Realm's chat?

Sadly, because it isn't *really* possible. In short, while there *is* a (somewhat) easy way of making a bot for *one single Realm-to-Discord server combination* do it, it's more or less *impossible* to make it work with multiple combinations outside of literally making a new Xbox account per Realm. Each account would only be able to track one Realm's chat at a time.

The Playerlist Bot focuses on being able to support multiple servers/Realms, so it isn't happening.

The [Realm Bot](https://realmbot.dev/) does offer this feature in its premium version. No idea about the technical details for how it works, but it requires a space to be taken for a dummy account anyways, so it still isn't happening here. The Playerlist Bot is not even supposed to touch the Realm, beyond reading the playerlist.

## Troubleshooting

### Help! The playerlist/online comamnd isn't working!

Well, this could be due to a number of reasons:
- For the autorunner version: was anyone on the Realm during that time? If there was no one, then the bot will not autorun the list during that time.
- Did you accidentally kick the account responsible for keeping track of the Realm? Did you decide to change which Realm a "Realm" is using? Try relinking it via `/config link-realm`!
- Did it spit out an error? I'll (or whoever is running the instance of your bot) already have the error and more information, so don't worry about that.

### There's a user called "Account with XUID (insert numbers here)" on the list. Who's that?

Well, that happens when the bot fails to convert what can essentially be called Xbox's IDs into its respective gamertag. Let me explain.

You may have heard of a Discord ID - it's a bunch of numbers that represents a thing on Discord, like a user, a channel, or a role (we'll be focusing on users). These numbers are useful because trying to use names means we can have conflicts - there's *definitely* more than one user named "Hawk" out there, after all. Instead of referring to a user by name, Discord tools (and Discord itself) refers to users by their ID, with their usernames basically being a thing only people see.

A similar concept is present in Xbox Live, which is used a lot with Realms (and Bedrock Edition in general). "Gamertags" can be thought up as usernames here, and "XUID"s are like Discord IDs.

The methods the bot uses to keep track of people gets the *XUIDs* of people. This isn't useful for most people, though, and so the bot has to find out what a person's gamertag is based off their XUID. While this resolving works *most* of the time, there are times where it fails, which is when this question comes into play.

To reliably get the gamertag of the XUID shown, you can use `/gamertag-from-xuid`, which uses several (possibly slow) methods to make sure you actually get the gamertag.

## Technical

### Can I self-host this?

...yes, but I can only wish you luck. This thing is *far* from simple to get everything working, requiring you to know the ins-and-outs of most of the libraries I use. It can be a mess, and gathering the databases and servers needed even more so. There's also not much room for simplification here. If you do want to continue, it's best if you have a decent understanding at Python, PostgreSQL, Redis, and Sentry.io before trying this.

[This](https://github.com/OpenXbox/xbox-webapi-python) is a good place to start researching on how it all works. Everything the bot uses can be gotten for free in some way, shape, or form.

Little support will be given for self-hosters (not trying to sound cruel, but it takes away at my time. That being said, if you know what you're doing, I can help you with troubleshooting). I *do* plan on making a guide on how to host it eventually though.

### What programming language does this use?

Python. It's slow (though there a lot of tricks to make it faster), but I'm *very* familiar with it. It's my favorite commonly-used language, so that helps.

Note that Python is *not* like Javascript, the most popular language for making small bots. There are some fundamental differences between them.

### Why is this bot so complex?

Funny enough, neither of the two methods the bot can use are really *that* complex. The Realms method is annoying for sure, since it's a bulk-only endpoint that only tells us who's online in a Realm, but the logic to make it work as a playerlist isn't anything really hard to understand - just keep a copy of the last minute's online list and compare it.

What *is* hard, however, is turning the XUIDs from these methods into gamertags *at scale*. This is because:
- The Xbox API *sucks.* It is *horribly* documented (literally anything about clubs is more or less hidden away, as obscure as it can be), and it throws a *lot* of errors even if you're doing absolutely everything right. There's reasons why services like OpenXBL exists - it's legitimately so bad that *an API for an API* needs to exist.
- This is compounded by the fact that `xbox-webapi-python` is almost absurdly complex. It is a *pain* to set up, and its folder structure makes me want to scream. *To be fair*, without it, I would have no way of authenticating the Xbox API, but still.
- Going back to the gamertag issue, the bulk endpoint for getting people's profiles (which has their gamertags) *seems* like the perfect solution to everything, but it errors out if you request more than ~30 people at a time. This isn't enough for big realms, and so forces us to use a backup method using OpenXBL while we wait for the ratelimit caused by the request to go away (OpenXBL isn't ratelimited, from what I can tell). A lot of things had to be put together to make sure it uses both systems as effectively as possible when they are needed, and so the final result came to be.
- Did I mention that the Xbox API just *fails* sometimes? Like, the bot sometimes gets a `200` status when requesting a gamertag without getting *any* data, and sometimes the Xbox API throws a `500` to keep you on your toes.
- It should be noted that the bot actually *does* keep its own cache of XUID > gamertags just to hope it doesn't have to rely on the Xbox API except when needed. I purposely made it expire entries after 14 days so there isn't an outdated gamertag for too long, though.

It also helps that there's a growing demand for more complex statical data to come from the bot. This requires usage of a database to do so, which just adds onto everything.