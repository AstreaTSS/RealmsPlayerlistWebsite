---
date: 2023-08-05
authors:
  - astrea
categories:
  - Features

description: A new way of linking the bot to your Realm has been added, removing the need to use a Realm code if you do not wish to.
comments: true
---

# A New Method of Linking Realms (Beta)

A new way of linking the bot to your Realm has been added as a beta, removing the need to use a Realm code if you do not wish to.
Instead of using a Realm code, `/config alternate-link` uses standard Microsoft linking to allow Realm owners to authenticate the bot
into adding itself into a Realm. Depending on your usecase, this may be more convenient to you.

<!-- more -->

## How to Use

Instead of using `/config link-realm` and giving a Realm code, you can use `/config alternate-link` to use the new method.
The new method will automatically start asking/showing prompts in an ephemeral message, so you do not need to worry about
other users seeing your authentication data or authenticating for you.

The prompts will first warn you about how the method works and the potential downsides of using it, and then (after accepting to continue)
ask you to authenticate with Microsoft through a code. Once you have authenticated, the bot will ask which Realm you wish to link -
select the Realm you wish to link, and the bot will automatically link itself to the Realm.

## Downsides

While this method is more convenient for some, it does have some downsides.
- This requires the Realm owner to do the command, as the bot will not be able to link itself to a Realm without the owner's permission. The normal method does not have this requirement.
- Using this method, as mentioned before, requires you to briefly authenticate with Microsoft. This is done through a code in line with Microsoft standards, and the bot will never see your password. Furthermore, the bot will not store the authentication data for longer than the setup process, and the entire process is available to view in the [server config file](https://github.com/AstreaTSS/RealmsPlayerlistBot/blob/main/exts/guild_config.py) and the [device code handling file](https://github.com/AstreaTSS/RealmsPlayerlistBot/blob/main/common/device_code.py). However, if you do not trust the bot with this data at all, you should not use this method.

Of course, `/config link-realm` will always remain and be the recommended method - as the name of the command suggests, this is just an alternative method.