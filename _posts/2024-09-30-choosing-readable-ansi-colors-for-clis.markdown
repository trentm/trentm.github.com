---
layout: post
title: Choosing readable ANSI colors for CLIs
published: true
date: 2024-09-30T16:21:06.366134
categories: [programming]
---

Earlier today Julia Evans [asked for "some examples of programs which don't do well with a light background"](https://social.jvns.ca/@b0rk/113227585852563559). My (mostly ancient) experience here is attempting to have reasonable colour usage out of my [`bunyan`](https://github.com/trentm/node-bunyan#readme) and [`ecslog`](https://github.com/trentm/go-ecslog#readme) tools for pretty-printing log files. I use iTerm2 on macOS with the default "Light Background" color preset. I have occasionally noted programs that generate output with colors that don't work for me. Julia's post was a good kick for me post some of the screenshots I've collected. (And to post to a blog that I haven't touched in 8 years.)

When I say "colour" (or "color" for some of y'all), I really mean [ANSI Select Graphic Rendition (SGR) parameters](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters), which includes more than just colours -- bold, italics, blink (!), "bright" or high-intensity colors, etc. I've have typically limited my usage to a few colours, and some usage of bold.

## tl;dr limited colour advice

A set of guidelines for ANSI style/colour usage. These are limited to my experience, which is restricted and old.

- **Avoid blue**, because it is not visible on cmd.exe on Windows. (It has been over a decade since I used Windows regularly, so this might be out of date.)
- **Avoid bright yellow and bold yellow**. The contrast with a white background, e.g. on the "Light Background" default preset for iTerm2 and Terminal.app on macOS, is too low, making the text unreadable. Note that plain "yellow" -- not bolded or bright -- is fine.
- **Avoid grey**. It is the same colour as the *background* on the Solarized Dark theme from <https://github.com/altercation/solarized>. (See [node-bunyan#160](https://github.com/trentm/node-bunyan/issues/160) and [solarized#220](https://github.com/altercation/solarized/issues/220).


## Examples of poor colours on a light background

Here are some examples, with screenshots, of programs that use colours/styles in the terminal that are problematic for readability. Some of these might be outdated. I hadn't noted program version or the date when collecting these. Also, bad me for never having opened issues on these projects regarding the colour issue.

Webpack using bright yellow.

![webpack program using bright yellow](/img/ansi-color-webpack.png)

`npm install` using bright yellow for the count of moderate vulnerabilities.

![npm using bright yellow for a moderate vulnerability](/img/ansi-color-npm.png)

`nvm ls` using bright yellow for some aliases.

!['nvm ls' using bright yellow](/img/ansi-color-nvm.png)

Maven test output using bright yellow.

![maven test output using bright yellow](/img/ansi-color-maven.png)

`az login` using bright yellow.
`az` is the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)

!['az' using bright yellow](/img/ansi-color-az.png)


## Links

- <https://no-color.org/> is an interesting effort to attempt to standardize the `NO_COLOR=1` environment variable for programs to disable their ANSI colouring.
- My Go-lang code for doing ANSI colouring: <https://github.com/trentm/go-ecslog/blob/main/internal/ansipainter/ansipainter.go#L3-L7>
- My (old) Node.js code for doing ANSI colouring: <https://github.com/trentm/node-bunyan/blob/master/bin/bunyan#L655-L691>
