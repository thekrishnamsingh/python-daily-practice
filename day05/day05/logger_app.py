def log_message(message):
    try:
        with open("app.log", "a") as log_file:
            log_file.write(message + "\n")
    except Exception as e:
        print("Logging failed:", e)


log_message("Application started")
log_message("User logged in")
log_message("Application closed")
