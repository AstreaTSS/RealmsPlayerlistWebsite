---
date: 2023-08-02
authors:
  - astrea
categories:
  - Playerlist Premium

description: Due to the Ko-Fi method has been increasingly unreliable, new users will not be able to purchase Premium using Ko-Fi anymore.
comments: true
---

# Deprecating the Legacy Ko-Fi Method for Playerlist Premium

Due to the Ko-Fi method has been increasingly unreliable, new users will not be able to purchase Premium using Ko-Fi anymore.
Existing users will continue being able to use Ko-Fi for existing subscriptions.

<!-- more -->

## Details

A month ago, a new method of paying for [Playerlist Premium](premium.md) was added to the Premium page. This came from the frustrations of using Ko-Fi as the payment handler - Ko-Fi was clearly not meant to handle premium features for Discord bots, and so an awkward hack was used to make it work (involving requiring to join the support server and using a role as a proof of subscription). This wasn't a good long-term solution, not least because the hack was dependent on Ko-Fi managing roles properly, which it didn't. T

The new payment method is a custom solution that manages subscriptions properly using a custom premium dashboard. When I first released it, I was cautious - I had no idea how it would play out in a real world setting, and so I left the Ko-Fi method as a backup option in case the new method failed. A month later and some bugs fixed, and it seems to be reliable now - most current issues come from user error (and poor communication on my part).

Looking at the numbers, the new method is also *much* more popular than the Ko-Fi method ever was, which is a good sign. In fact, no users have used the Ko-Fi method after the new method was introduced. Because of this, and because the only remaining benefit of the Ko-Fi method is that it accepts PayPal accounts (which isn't a huge loss), there's no reason to keep the Ko-Fi method around.

## Existing Users

To re-iterate: **existing users will continue being able to use Ko-Fi for existing subscriptions.** This change only affects new users.

Support for Ko-Fi methods will be done on a "best effort" basis. If you have any issues with your Ko-Fi subscription, please contact me on the [support server](https://discord.gg/NSdetwGjpK) or [through email](mailto:discord@astrea.cc) and I'll try to make it work - most likely it'll work out, but if it doesn't, then I'll refund you and direct you to the new/current method.

Switching to the new method for my sake would be nice of you, but you don't have to do it at all. If you're happy with Ko-Fi, then you can keep using it. Switching methods requires disabling your old code and getting a new one anyhow.