import os
import logging
import smtplib
import time

import schedule
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
recipients = ["yehor.dudnik@gmail.com"]


def configure_logging():
    """
    Configure logging settings.

    This function sets up logging for the application. It configures the logging level, log file name, file mode, and format.

    :return: None
    """

    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a+",
                        format="%(asctime)s %(levelname)s %(message)s")


def configure_smtplib():
    """
    Configure SMTP server settings.

    This function configures the SMTP server, SMTP port, and login credentials for sending emails.

    :return: List containing SMTP server, SMTP port, username, and password.
    """

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = os.getenv("MY_EMAIL_USERNAME")
    password = os.getenv("MY_EMAIL_PASSWORD")
    return [smtp_server, smtp_port, username, password]


def compose_message(sender: str, recipient: str):
    """
    Compose an email message.

    This function creates an email message with a specified sender, recipient, subject, and message body.
    It also attaches a PDF file to the email.

    :param sender: The email address of the sender.
    :param recipient: The email address of the recipient.
    :return: The email message.
    """

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = "Report"
    message = "My report"
    msg.attach(MIMEText(message, 'plain'))
    with open("report.pdf", 'rb') as file:
        pdf_attachment = MIMEApplication(file.read(), _subtype='pdf')
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename='report.pdf')
    msg.attach(pdf_attachment)
    return msg


def send_emails():
    """
    Send emails to recipients.

    This function sends emails to the specified recipients using SMTP settings and email composition.

    :return: None
    """

    configurations = configure_smtplib()
    for recipient in recipients:
        message = compose_message(sender=configurations[2], recipient=recipient)
        try:
            server = smtplib.SMTP(configurations[0], configurations[1])
            server.starttls()
            server.login(configurations[2], configurations[3])
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            logging.error(f"Error connecting to the server: {e}")
        try:
            server.sendmail(message['From'], message['To'], message.as_string())
            print('The letter has been successfully sent')
            logging.info(f"The email has been successfully sent")
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
            logging.error(f"Error while sending the email {e}")
        server.quit()


def main():
    """
    Main function to schedule and send emails.

    This function configures logging, schedules the email sending task daily at midnight, and runs the scheduler loop.

    :return: None
    """

    configure_logging()

    schedule.every().day.at("00:00").do(send_emails)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    """
    Entry point of the script.
    """

    main()

