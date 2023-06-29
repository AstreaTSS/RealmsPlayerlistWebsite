---
description: The privacy policy for the Realms Playerlist Bot.
---

# Privacy Policy

*Last updated: 2023-06-29 (YYYY-MM-DD).*

This document contains the privacy policy and agreement you accept when adding the below mentioned Bot to a server, or use them as a member of a Server. This document does not supersede any of the terms laid out by Discord.

## Terminology

-   **Discord** – The chat platform hosted and operated by Discord INC.
-   **User** – Any Discord account that uses a Service in any way.
-   **Server** – A server on Discord, also known as a "Guild."
-   **Server Member** – Anyone who is a member of Server to which one of the bots has been added.
-   **Server Manager** – A Server Member that has the ability to add Bots to a Server and/or configure a Bot for a Server.
-   **Bot** – An automated user on Discord denominated by the "BOT" tag.
-   **Xbox Service** - the specific service hosted by Microsoft for their gaming content.
-   **Minecraft** - An open-world sandbox game - more specifically, this refers to what is commonly referred to as the "Bedrock Edition."
-   **Player** - An account using Xbox Services, including those made to play Minecraft online.
-   **Realm** - Minecraft Realms, a service hosted by Minecraft to allow multiple Players to play together.
-   **Associated Service** – A service hosted outside Discord to offer additional functionality to a Bot.

### Bots and Services

This privacy policy applies to the following Bots.

-   **Realms Playerlist Bot**#4414 (725483868777611275)

## What Data We Collect

We collect data with different scenarios, each scenario covered by this Policy will be explained below.

#### Collected by Command

The following data may be collected and temporarily stored when intentionally provided by a User via usage of a function of the Bot, hence this data is not collected automatically. Should a User provide data in this manner, they forego any rights pertaining to the content of the data provided.

-   Server specific configuration settings.
-   Data and content for the task called.

#### Automatically Collected

This data may be collected automatically by some Services. This data is used to facilitate critical functionality of Services, and are vital to its operation.

-   Any data needed for standard operation of the Bot. This typically includes channel data and roles.
-   Data relating to users via the Xbox Service, including any Minecraft-related data (e.g. information on when a Player was on a Realm).

## Why We Collect Data

We collect data to facilitate functions of Services, and to provide us with analytical data about the Bot's usage and behavioral patterns. For example, data from the Xbox Services is used in order to track several's Players' activity on a Realm to later present them in a human-readable way.

## Who We Share Data With

We do not share data with any 3rd party for any reason whatsoever, unless required by law.

## How Your Data is Stored

All data is stored on protected infrastructure. While storage methods may vary between Services, most data will be stored within enterprise-standard databases such as [PostgreSQL](https://www.postgresql.org/) (persistent) or [Redis](https://redis.io/) (cache). Please keep in mind that even with the highest standard of protection, no data can ever be 100% secure. While we strive to keep data secure and private at all times, absolute security cannot be guaranteed.

## How Long Your Data is Retained

Data collected via command, meaning collected via explicit understanding that the data is going to be saved (cache), is retained for as long as the instance of the Bot runs or until it is cleared to make room. Other data retained is as follows:

#### Server Configuration

The Bot stores information relating to a Server's configuration. This information is automatically deleted if it leaves a Server, but is otherwise indefinitely kept.

#### Gamertags

The Bot uses Redis/a cache in order to store a link between "XUID", the way Xbox Services denotes its Users, and a "Gamertag", a human-friendly way of referring to said User. Entries are automatically deleted after 14 days.

#### Realm Player Session Activity

The Bot uses Xbox Services in order to track Players on Realms, and stores it per each session - a period of time where a Player was on a Realm. This data is deleted after 31 days after the Player left the Realm for that session, or when the last Server tracking the Realm removes the bot.

## Your Rights to Your Data

Pursuant to various jurisdictions, you have the right to request a machine-readable copy of your data for portability's sake and the right to have your data deleted from the Service.

Should you wish to enforce one of these rights, please send an email to [discord@astrea.cc](mailto:discord@astrea.cc) - we will strive to respond to your request within 30 days.

## Children's Privacy

Our Services do not address anyone under the age of 13. We do not knowingly collect personally identifiable information from anyone under the age of 13. If you are a parent or guardian and you are aware that your child has provided us with personal data, please contact us. If we become aware that we have collected personal data from anyone under the age of 13 without verification of parental consent, we will take steps to remove that information from our servers.

## Feedback

Feedback concerning any of the outlined Services is appreciated. However, you agree that upon submission of feedback, you forego any rights to the content, title, or intent of the provided feedback. Additionally, the feedback you provide may be used in any way.

## Agreement

By utilizing any of the before mentioned Services, you are consenting to the policies outlined in this document. Additionally, you, the Server Manager, agree to inform other Server Members in your Server about the contents of this document.

If you, the Server Manager, do not agree to the terms laid out in this document, you may remove the Bots from the server and stop using Associated Services.

If you, the Server Member, do not agree to the terms laid out in this document, you may leave Servers that contain any of the before mentioned Bots.
