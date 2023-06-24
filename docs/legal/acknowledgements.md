---
description: Acknowledgements for various people/tools/companies that helped make the Realms Playerlist Bot possible.
---

# Acknowledgements

*Note: this is an informal section, and probably needs polishing.*

## Minecraft
- Minecraft and Minecraft Realms is owned by Mojang.
  - Shoutouts to CornerHard for being a great developer for Realms!
- Mojang itself and Xbox Live (including its API) is owned by Microsoft.

## Branding
- Icon made by [beni2am](https://www.beni2am.space) - thanks!
- Other assets made by me, [AstreaTSS](https://astrea.cc/).
  - The banner uses the [Bare Bones resource pack](https://www.curseforge.com/minecraft/texture-packs/bb) and [Complementary Reimagined shaders](https://www.complementary.dev/reimagined/). Yes, it was taken on Java edition, yes, that is ironic.[^1]

## Code

I won't list every dependency here, because GitHub does a good job of that. Check them out [through this link!](https://github.com/AstreaTSS/RealmsPlayerlistBot/network/dependencies) Instead, here are the major ones:
- [interactions.py](https://github.com/interactions-py/interactions.py) is made by a slew of people, including myself, but the current lead is [LordOfPolls](https://github.com/LordOfPolls). That being said, thanks to all of the (other) contributors for making it one of the best Python Discord libraries I ever used - I really love it.
- [xbox-webapi-python](https://github.com/OpenXbox/xbox-webapi-python) is made by [Team OpenXbox](https://github.com/OpenXbox), and while I do have my issues with how it's designed, I cannot thank them enough for doing the hard work of parsing the Xbox API for me.[^2]
- [Tortoise ORM](https://github.com/tortoise/tortoise-orm) is just a wonderful ORM to use. Seriously, it feels natural to make and use database related objects thanks to it.
- [orjson](https://github.com/ijl/orjson) by [ijl](https://github.com/ijl) is... just a fun thing to use. Fast, always correct, and pretty much unrivaled - what more could you want?
  - Actually, [msgspec](https://github.com/jcrist/msgspec) by [jcrist (Jim Crist-Harif)](https://github.com/jcrist) *does* rival it and is also a great library.[^3]

## Other
- Literally anyone who made [this page about the Realms API](https://wiki.vg/Bedrock_Realms) is my savior. What's otherwise undocumented was made really easy to understand and use thanks to that page.
- [Fallen Anarchy](https://discord.gg/VBnZ6gk6zt), managed by the Fallen Network, provides a space to test out this bot without paying a decent amount for a Realm - thanks!

[^1]: Bedrock Edition doesn't have great shader support, and I do not have a GPU capable of raytracing.
[^2]: Though this library is not being used in the bot itself (anymore) - it was just inspiration.
[^3]: Both libraries are used in the bot itself. orjson for general JSON support and msgspec when there's a known format in mind. As you can imagine, this is down to their speeds in those respective scenerios.