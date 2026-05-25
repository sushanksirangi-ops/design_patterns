from logger import Logger
from notification_factory import NotificationFactory
from user_builder import UserBuilder

def main():

    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Application Started")

    print("\nSame Logger Instance:",
          logger1 is logger2)


    email = NotificationFactory.create_notification("email")
    sms = NotificationFactory.create_notification("sms")
    push = NotificationFactory.create_notification("push")

    email.send("Welcome Email")
    sms.send("OTP Message")
    push.send("App Notification")


    user = (
        UserBuilder("Sushank", "sushank@gmail.com")
        .set_age(22)
        .set_phone("9876543210")
        .set_address("Hyderabad")
        .build()
    )
    user.display()
    logger1.log("\nApplication Finished")

if __name__ == "__main__":
    main()