---
description: Information about how to self-host the Realms Playerlist Bot.
---

# Self-Hosting

!!! warning "Note about Self-Hosting"
    Self-hosting is not recommended for most users, being a complicated process that requires a decent bit of technical knowledge. Only do this if you have a personal interest in self-hosting, or if you want to contribute to the bot's development.
    For most people, the public instance of the bot is more than enough - see the [Server Setup Guide](server_setup.md) for more information.

As the bot is [open source](https://github.com/AstreaTSS/RealmsPlayerlistBot), that means anyone has the means to self-host the bot. This is a fairly complicated process, as the warning above states, but it is possible.

??? question "Why Self-Host, Then?"
    There are a few reasons why you might want to self-host the bot:
    - You want to contribute to the bot's development.
    - You want to modify the bot for your own purposes.
    - You care about privacy and want to host the bot yourself.
    - ...you can, of course, get Premium for free if you self-host the bot. I won't stop you, but [considering donating to my Ko-Fi](https://ko-fi.com/astreatss) at least.

There are two methods of self-hosting the bot: using Docker, or using a manual installation. Docker is the recommended method, as it is easier to set up and maintain, but a manual installation is also possible.

## Docker

!!! note 
    General knowledge of how Git, Docker, and docker-compose works is highly recommended before attempting to self-host the bot through Docker.

    While this list looks long, most of this is a process you only have to do once. After that, updating the bot is much easier.

### Setup 

1. Install [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).
2. Create a Discord application through [Discord's developer portal](https://discord.com/developers/applications) if you do not already have one. You will need its bot token later, so make a bot account too.
3. Clone the bot repo - `git clone https://github.com/AstreaTSS/RealmsPlayerlistBot.git`.
  - You will have to [install Git](https://git-scm.com/downloads) if you do not already have it installed. You can also download the repo as a ZIP file through GitHub, though this will make updating the bot much harder.
4. Create a copy of the existing `config_example.toml` file and rename it to `config.toml`.
5. Go into the `config.toml` file and follow the instructions there in the file to fill in as many fields as you can. To note:
   - `DOCKER_MODE` should be set to `true`. You can leave the values of `DB_URL` and `REDIS_URL` as-is - they are only used if you are using a manual installation.
   - You may want to skip the steps about `XBOX_CLIENT_ID` and `XBOX_CLIENT_SECRET` for later if you don't have a Python installation on your PC (if you don't know, you probably don't have Python installed) or don't want to install a package on your host PC.
   - For the emojis:
     - `"RAW EMOJI STRING"` means the emoji's raw string, like `<:emoji:123456789012345678>`. You can get this by typing `\` and then the emoji in Discord.
     - `"EMOJI ID"` means the emoji's ID, like `123456789012345678`. You can get this by doing the same thing as above, but copying the numbers in the middle.
     - The only requirements for emojis is that they must be custom emojis and they must be usable by the bot; it is recommended you upload the emojis at the developer portal and use them from there.
6. Initialize Docker. Run `docker compose build` to build the bot's Docker image.
7. Make a `.env` file in the root directory with one thing in it: `POSTGRES_PASSWORD="PASSWORD"`. This is used by Docker to set up the database. Of course, replace `PASSWORD` with a password of your choice.
8. If you skipped setting up the Xbox Live authentication steps, this is the time to do so. You can use `docker compose run bot CMD` (replacing `CMD` with the a command) to run any commands seen in [the guide linked in `config.toml`](https://github.com/Astrea-Stellarium-Labs/elytra-ms#make-an-application) to set it up.
  - Remember to rename the generated file to `tokens.json` and set `XBOX_CLIENT_ID` and `XBOX_CLIENT_SECRET` in `config.toml`.
9. Run `docker compose up -d` to start the bot. You can use `docker compose logs -f` to view the logs of the bot.
  - To sync slash commands, run `@BOT_MENTION debug sync` in Discord (replace `BOT_MENTION` with the bot's mention, like `@Realms Playerlist Bot`).

### Updating
1. Pull the latest changes from the repo - `git pull`.
2. Run `docker compose build` to build the bot's Docker image.
3. Run `docker compose up -d` to restart the bot.
  - To sync new slash commands, run `@BOT_MENTION debug sync` in Discord (replace `BOT_MENTION` with the bot's mention, like `@Realms Playerlist Bot`).

!!! note
    Migrations, by default, are run automatically when the bot starts up in Docker mode. If you don't want this to happen for whatever reason (you usually do!), you can set a debug flag in `config.toml` (add this to the end of your file):
    ```toml
    [DEBUG]
    RUN_MIGRATIONS_AUTOMATICALLY = false
    ```

## Manual Installation

!!! warning
    This is complicated and requires knowledge about Python, Postgres, and Redis. The Docker method is almost always preferred if you're self-hosting.

### Setup
1. Install the latest version of Python. The bot is almost always using the latest features of Python - you can verify the exact version the bot is using by checking the [Dockerfile on the bot's repo](https://github.com/AstreaTSS/RealmsPlayerlistBot/blob/main/Dockerfile) and seeing the Python version used.
2. Get your hands on:
  - A Postgres database. Free options include Supabase or CockroachDB, or you can host it yourself. Remember the database connection URL for later.
  - A Redis database. Free options include Redis Labs, or you can host it yourself. Remember the connection URL for later.
3. Create a Discord application through [Discord's developer portal](https://discord.com/developers/applications) if you do not already have one. You will need its bot token later, so make a bot account too.
4. Clone the bot repo - `git clone https://github.com/AstreaTSS/RealmsPlayerlistBot.git`.
  - You will have to [install Git](https://git-scm.com/downloads) if you do not already have it installed. You can also download the repo as a ZIP file through GitHub, though this will make updating the bot much harder.
4. Install the required Python packages. You can do this by running `pip install -r requirements.txt` in the bot's directory.
  - You should set up a virtual environment for the bot. A popular one is `venv`, done simply through `python -m venv env`. You can then activate it through `source env/bin/activate` on Linux or `env\Scripts\activate.bat` on Windows.
5. Create a copy of the existing `config_example.toml` file and rename it to `config.toml`.
6. Go into the `config.toml` file and follow the instructions there in the file to fill in as many fields as you can. To note:
  - `DOCKER_MODE` should be set to `false`. You MUST set `DB_URL` and `REDIS_URL` to the URLs you got earlier.
  - For the emojis:
     - `"RAW EMOJI STRING"` means the emoji's raw string, like `<:emoji:123456789012345678>`. You can get this by typing `\` and then the emoji in Discord.
     - `"EMOJI ID"` means the emoji's ID, like `123456789012345678`. You can get this by doing the same thing as above, but copying the numbers in the middle.
     - The only requirements for emojis is that they must be custom emojis and they must be usable by the bot; it is recommended you upload the emojis at the developer portal and use them from there.
7. Run `python -m prisma generate` to generate the database models.
8. Run `python -m prisma migrate deploy` to initialize the database. You'll need to set the `DB_URL` variable manually in your terminal for this command, likely via `export`.
  - Depending on your needs, you may want to replace `deploy` with `dev` to perform a destructive migration. For more information, check out [the docs about Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate).
9. Run `python main.py` to start the bot. You may want to use a process manager like `pm2` to keep the bot running in the background.
  - To sync slash commands, run `@BOT_MENTION debug sync` in Discord (replace `BOT_MENTION` with the bot's mention, like `@Realms Playerlist Bot`).

### Updating
1. Pull the latest changes from the repo - `git pull`.
2. Install the latest packages through `pip install -r requirements.txt`.
3. If the `prisma` package was updated, or `schema.prisma` was modified with new/removed fields, you should run `python -m prisma generate` to generate the database models.
4. If any new entries were added to `migrations/`, run `python -m prisma migrate deploy` to update the database. You'll need to set the `DB_URL` variable manually in your terminal for this command, likely via `export`.
  - Depending on your needs, you may want to replace `deploy` with `dev` to perform a destructive migration. For more information, check out [the docs about Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate).
5. Run `python main.py` to restart the bot. You may want to use a process manager like `pm2` to keep the bot running in the background.
  - To sync new slash commands, run `@BOT_MENTION debug sync` in Discord (replace `BOT_MENTION` with the bot's mention, like `@Realms Playerlist Bot`).

## Notes
- When first running the bot, you'll need to sync the slash commands to start using the bot. You can do this by running `@BOT_MENTION debug sync` in Discord (replace `BOT_MENTION` with the bot's mention, like `@Realms Playerlist Bot`).
  - If you wish to use the developer slash commands, you'll also need to sync to your dev server through `@BOT_MENTION debug sync DEV_SERVER_ID` (`DEV_SERVER_ID` with the ID of the server you want to sync to).
- There are a *lot* of developer commands. You can check them out by looking through the [`owner_cmds.py` file](https://github.com/AstreaTSS/RealmsPlayerlistBot/blob/main/exts/owner_cmds.py).
- While self-hosting the bot, you are subject under the terms of the GNU Affero General Public License license. You can read more about the license [on this page](https://choosealicense.com/licenses/agpl-3.0/) or [on the GNU website](https://www.gnu.org/licenses/agpl-3.0.html).
- While you can [join my support server](https://discord.gg/NSdetwGjpK) for help, I cannot guarantee I will be able to help you with self-hosting the bot due to how different each setup can be. I will also not help you with setting up Docker, Postgres, Redis, or any other software you need to self-host the bot. I will only help with the bot itself.
