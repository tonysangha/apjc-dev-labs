# Setup Wrangler

This guide will instruct you through setting up a Cloudflare account to deploying your first Worker. This guide assumes that you already have a Cloudflare account. If you do not have a Cloudflare account, [sign up](https://dash.cloudflare.com/sign-up/workers) before continuing.

## Install Wrangler (Workers CLI)

Installing `wrangler`, the Workers command-line interface (CLI), allows you to, [`dev`](/workers/wrangler/commands/#dev), and [`deploy`](/workers/wrangler/commands/#deploy) your Workers projects.

To install [`wrangler`](https://github.com/cloudflare/workers-sdk/releases), ensure you have [`npm` installed](https://docs.npmjs.com/getting-started), preferably using a Node version manager like [Volta](https://volta.sh/) or [nvm](https://github.com/nvm-sh/nvm). Using a version manager helps avoid permission issues and allows you to easily change Node.js versions.

Then run:

```sh
npm install -g wrangler
```

or install with `yarn`:

```sh
yarn global add wrangler
```

## Authenticate Wrangler

To authenticate Wrangler, run `wrangler login`:

```sh
wrangler login
```

You will be directed to a web page asking you to log in to the Cloudflare Dashboard. After you have logged in, you will be asked if Wrangler can make changes to your Cloudflare account. Scroll down and select **Allow** to continue.

```{admonition} Wrangler Playground
:class: note
The quickest way to experiment with Cloudflare Workers is in the [Playground](https://cloudflareworkers.com/#36ebe026bf3510a2e5acace89c09829f:about:blank). The Playground does not require any setup. It is a simple, instant way to preview and test a Workers script directly in the browser.
```

## Create-Cloudflare-CLI (C3)

C3 (create-cloudflare-cli) is a cli tool to setup and deploy applications to Cloudflare. One of the benefits of this tool, is it leverages officially developed templates for Workers, and framework-specific setup guides to ensure each new application that you setup follows Cloudflare, and any third-party best practices for deployment on the Cloudflare network. 

You'll use this tool in this lab to setup any new Worker projects going forward. 