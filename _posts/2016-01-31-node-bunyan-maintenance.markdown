---
layout: post
title: node-bunyan maintenance
published: true
date: 2016-01-31T01:47:05.435Z
categories: [bunyan, nodejs, programming]
---

This is a mea culpa on [node-bunyan](https://github.com/trentm/node-bunyan)
maintenance.

I'm thankful for all the positive feedback I get for this project. However, I
can understand that it must be frustrating for users when there are large time
gaps in maintenance of it &mdash; as has been the case at the time of writing and in
the past &mdash; and especially with PRs that languish.

Bunyan started out as a small project to scratch an itch at work, significant
chunks developed on my own time &mdash; and it is working quite well for mine
and my work's use cases. It got moderately popular. I added features (typically
initiated by feature requests or pulls with a good start) that I don't
personally use. Node has seen a flurry of releases. Bunyan includes a
platform-specific binary dep. The test suite requires root access to fully run
(because of dtrace integration). These add up to there being a lot of
maintenance traffic for issues that don't affect me directly. But it has one
effect: guilt.

There are features I'd love to add to Bunyan, and have wanted to add for
quite a while. However, I never feel right diving into those with all the
outstanding bugs that block usage for some use cases. Those issues take a lot
of energy (clarifying, reproducing, fixing, testing, documenting) and after a
while the built up wall of them makes it hard to *start*.

Time for a plan and perhaps, eventually, some help.<br/>
**The plan: <https://github.com/trentm/node-bunyan/issues/335>**

Please read [Bunyan's contributing
guide](https://github.com/trentm/node-bunyan/blob/master/CONTRIBUTING.md)
if you are interested, and be aware that I'm still attempting to make a
pass through all the issues.

My hope is to get through issue #335 over the next few weeks, including a
triage of all issues and PR and having a clearer formula for triage and a short
term roadmap. Then ideally I can share some of the maintenance work with others.
Thank you to many for great PRs, patience, polite issue conversations, and
offers of maintenance help.
