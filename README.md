# rapidpro-datagen


RapidPro sample data generator.

## Prerequisites

 - pipenv (better with pipsi)
 - npm
 
 
### NOTE: 
    
> Due some conflicts in the RapidPRO requirements, that prevent the creation of a 
> replicabile and predicibile environment, it is not possible to install rapidpro 
> using pipenv.
> We still use pipenv to be ready if/when RapidPRO requirements conflicts will be solved. 


## Install

Set `DATABASE_URL` environment variable to reflect your postgres database
    
    $ export DATABASE_URL=postgres://postgres:@127.0.0.1:5432/rapidpro

Clone the repo and setup the virtualenv

    $ git clone https://github.com/unicef/rapidpro-datagen.git datagen
    $ cd datagen
    $ make develop
    $ pipenv shell
    
## QUICKSTART

    # generate db
    
     
## HELP
    $ generate --help
    Usage: RapidPro Data Generator [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.
    
    Commands:
      db      generate data
      status  display database numbers
      zap     empty database
      
### db
    $ generate db --help
    Database: perf://postgres:@127.0.0.1:5432/rapidpro
    Usage: RapidPro Data Generator db [OPTIONS]
    
      generate data
    
    Options:
      -v, --verbosity INTEGER
      --zap                    Erase all data first
      --atomic                 Use single transaction. Do not use for large dataset  (>~500.000
      --create / --append      Create new organizations or append new data to existing
      -p, --processes INTEGER  number of processes to use
      --seed INTEGER           initial pk value for numbers
      --base-email EMAIL       Base GMail addres to use for email generation
      --admin-email EMAIL      Alll Organizanizations admin's email
      --superuser-email EMAIL  System superuser email
      --users INTEGER          Number od Users to create
      --organizations INTEGER  Number od Organizations to create
      --channels INTEGER       Minimum number of Channels to create
      --contacts INTEGER       Minimum number of Contacts to create
      --archives INTEGER       Minimum number of Archive to create
      --flows INTEGER          Minimum number of Flow to create
      --broadcasts INTEGER     Minimum number of Broadcasts to create
      --archives INTEGER       Minimum number of Archives to create
      --help                   Show this message and exit.
      
       
## Note

Following users will be always available to interact with RapidPRO
    
- One system superuser `superuser` (password `123`) 
- One "all organizations" admin `admin` (password `123`)

- Multiprocessing does not work on some platform, due postgres `libpq` issues. 
Use `--processes=1` if any problem 
