"""
Ability to Send Emails.

Sending Email using google SMTP.
"""

from flask import render_template
from flask_mail import Message
from app import mail

sender = "Eduardo.Eddy.Verde94@gmail.com"


def configEmailTemp(userinformation):
    """Creating The HTML Body Template and send email."""
    sendEmail(
        sender,
        [userinformation['email']],
        "WooHooo Got Your Email",
        render_template("emailTemp.html", user=userinformation),
    )


def sendEmail(sender, recipient, subject, html_body):
    """Sending Email."""
    msg = Message(subject, sender=sender, recipients=recipient)
    msg.html = html_body
    mail.send(msg)
