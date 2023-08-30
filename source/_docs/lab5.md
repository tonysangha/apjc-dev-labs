# Lab 5 - Building with D1 - Northwinds

This lab will showcase how to leverage Cloudflare D1 (SQL Database), using the Dataset from [northwind-SQLite3](https://github.com/jpwhite3/northwind-SQLite3). It will leverage:

- Cloudflare Workers for compute
- D1 for database
- Typescript 
- Tailwind CSS
- React for DOM interaction
- Remix for the React framework

## Background on D1

[D1](https://developers.cloudflare.com/d1/) is Cloudflare's native serverless database, which was launched in late 2022. It's based on the same fundamentals as KV, Durable Objects which is to be deployed to **Region:Earth**, scale-to-zero, and in addition be SQL-based. D1 is be accessible using [Pages](https://developers.cloudflare.com/pages/) or [Workers](https://developers.cloudflare.com/workers/), depending on your use case.  


## Deploying Northwinds on D1

For this lab, we will clone an existing Git. 

1. Git clone the following repo into your code folder, and we'll call in Lab 5. 

```bash
git clone git@github.com:cloudflare/d1-northwind.git lab5
```

```bash
tree -L 1
.
├── LICENSE
├── README.md
├── db
├── frontend
├── node_modules
├── package-lock.json
├── package.json
├── tsconfig.json
└── worker

5 directories, 5 files
```

- `db` - contains the schema and data that we will load into D1
- `frontend` - contains the Remix Pages project which will be used for the front-end
- `worker` - contains the backend Worker that will interact with the D1 database. The Worker is written in TypeScript and will leverage the binding defined in the `wrangler.toml` file.


2. Install required packages using `npm install` once you change into the Lab 5 directory
3. Create a new D1 database in your Cloudflare account:

```bash
wrangler d1 create northwind

Successfully created DB 'northwind' in region APAC
Created your database using D1's new storage backend. The new storage backend is not yet recommended for production workloads, but backs up your data via point-in-time restore.

[[d1_databases]]
binding = "DB" # i.e. available in your Worker on env.DB
database_name = "northwind"
database_id = "7361f116-09cb-4178-a76c-1a9c21d80c27"
```

```{admonition} Data location
:class: Info
By default, D1 will automatically create your database in a location close to where you issued the request to create a database. In most cases this allows D1 to choose the optimal location for your database on your behalf. To provide location hints to where your D1 instance should be created, use the `--location` flag when creating your DB. Hints available are as follows:

- `wnam` - Western North America
- `enam` - Eastern North America
- `weur` - Western Europe
- `eeur` - Eastern Europe
- `apac` - Asia-Pacific
```

4. Change the `database_id` field in your `wrangler.toml` located in the `worker` subdirectory, and update the route to a custom domain as per the example below:

```bash
compatibility_date = "2022-04-05"
main = "index.ts"
name = "northwind-worker"
routes = [
	{ pattern = "api.<YOUR_ZONE>.com", custom_domain = true }
]

[[d1_databases]]
binding = "DB"
database_name = "northwind"
database_id = "<DATABASE_ID>"

```

5. Next, let's create the D1 schema, and import the data using the following commands:

```bash
wrangler d1 execute northwind --file=./db/schema.sql
wrangler d1 execute northwind --file=./db/data-big.sql --batch-size=50000

🌀 Mapping SQL input into an array of statements
🌀 Parsing 639024 statements
🌀 We are sending 13 batch(es) to D1 (limited to 50000 statements per batch. Use --batch-size to override.)
✔ ⚠️  Too much SQL to send at once, this execution will be sent as 13 batches.
ℹ️  Each batch is sent individually and may leave your DB in an unexpected state if a later batch fails.
⚠️  Make sure you have a recent backup. Ok to proceed? … yes
🌀 Let's go
```

**Note:** This operation may take several minutes to complete.

```{admonition} Importing data into D1
:class: Info
The two scripts to create the schema and load the data are located in the `db` folder and are called:
- `schema.sql`
- `data-big.sql`
```

6. Using `wrangler` explore the available options and execute a SQL query from the command line as shown below:

```bash
wrangler d1

🗄  Interact with a D1 database

Commands:
  wrangler d1 list                List D1 databases
  wrangler d1 info <name>         Get information about a D1 database, including the current database size and state.
  wrangler d1 create <name>       Create D1 database
  wrangler d1 delete <name>       Delete D1 database
  wrangler d1 backup              Interact with D1 Backups
  wrangler d1 execute <database>  Executed command or SQL file
  wrangler d1 time-travel         Use Time Travel to restore, fork or copy a database at a specific point-in-time.
  wrangler d1 migrations          Interact with D1 Migrations
  ```

```bash
wrangler d1  execute northwind --command 'SELECT Title, FirstName, LastName, BirthDate from Employee'

🌀 Mapping SQL input into an array of statements
🌀 Parsing 1 statements
🌀 Executing on northwind (82cf203a-645e-4198-a1f4-f308d70ecf8b):
🚣 Executed 1 commands in 0.22076299996115267ms
┌──────────────────────────┬───────────┬───────────┬────────────┐
│ Title                    │ FirstName │ LastName  │ BirthDate  │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Representative     │ Nancy     │ Davolio   │ 1980-12-08 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Vice President, Sales    │ Andrew    │ Fuller    │ 1984-02-19 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Representative     │ Janet     │ Leverling │ 1995-08-30 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Representative     │ Margaret  │ Peacock   │ 1969-09-19 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Manager            │ Steven    │ Buchanan  │ 1987-03-04 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Representative     │ Michael   │ Suyama    │ 1995-07-02 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Representative     │ Robert    │ King      │ 1992-05-29 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Inside Sales Coordinator │ Laura     │ Callahan  │ 1990-01-09 │
├──────────────────────────┼───────────┼───────────┼────────────┤
│ Sales Representative     │ Anne      │ Dodsworth │ 1998-01-27 │
└──────────────────────────┴───────────┴───────────┴────────────┘
```

7. Next, we need to replace the `api.northwind.d1sql.com` dns record with the one you created in step 4 in the front-end pages app code. 

- Change into the directory: `./frontend/app/routes` and execute the following command:

```bash
find . -type f -name '*.tsx' -exec sed -i '' 's/api.northwind.d1sql.com/api.<YOUR_ZONE>.com/g' {} \;
```

8. Next, let's deploy the API Worker that will interact with the D1 database

```bash
cd ../../../worker
wrangler deploy
```
9. Deploy the Pages Front-End to Cloudflare

```bash
cd ../frontend

npm run build

wrangler pages deploy ./public

No project selected. Would you like to create one or use an existing project?
❯ Create a new project
  Use an existing project
✔ Enter the name of your new project: … northwind
✔ Enter the production branch name: … production
✨ Successfully created the 'northwind' project.
▲ [WARNING] Warning: Your working directory is a git repo and has uncommitted changes

  To silence this warning, pass in --commit-dirty=true


✨ Compiled Worker successfully
🌎  Uploading... (27/27)

✨ Success! Uploaded 27 files (2.04 sec)

✨ Uploading _headers
✨ Uploading Functions bundle
✨ Uploading _routes.json
✨ Deployment complete! Take a peek over at https://a5e2b850.northwind-gfp.pages.dev
```

Fantastic, go checkout your new app on the `*.pages.dev` URL, and explore the code to understand the mechanics of how it all fits together. 

```{admonition} Pages DNS Entry
:class: Info
It may take up to 60 seconds for the DNS entry to resolve, before you're able to access the front-end of the application. You can add a custom-domain into your Pages project via the Cloudflare Dashboard as well. 
```

## More Information

For more information on D1, check out the following links:

- [Introductory Blog Post](https://blog.cloudflare.com/d1-open-alpha/)
- [D1 Enhancements](https://blog.cloudflare.com/d1-turning-it-up-to-11/)
- [D1 Documentation](https://developers.cloudflare.com/d1/)
- [D1 Discord Channel](https://discord.com/channels/595317990191398933/992060581832032316)
- [Access D1 over HTTP GitHub Repo](https://github.com/elithrar/http-api-d1-example)