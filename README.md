
## Environment Setup

Run the following inside /web_app_assignment in a terminal:

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```


## App Setup

1. Run the following inside /web_app_assignment in a terminal to setup the database for users and products:

    ```bash
    python3 populate_db.py 
    ```

2. Modify the SECRET_KEY in app/__ init __.py to a randomly generated 16-character secret

## Run App (Server)

Run the following inside /web_app_assignment in a separate terminal to start the server:

```bash
  python3 main.py
```

## Run App (Client)

Run the following inside /web_app_assignment/client in a separate terminal to start the client:

```bash
  python3 client.py
```

## User Credentials (for Client use)

Refer to the following for the predefined users of the client:

```bash
  User: admin
  Password: admin123

  User: privileged
  Password: priv123
```