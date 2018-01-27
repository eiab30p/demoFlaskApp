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
        userinformation.email,
        "WooHooo Got Your Email",
        render_template("emailTemp.html", user=userinformation),
    )


def sendEmail(sender, recipient, subject, html_body, attachment):
    """Sending Email."""
    msg = Message(subject, sender=sender, recipient=recipient)
    msg.html = html_body
    mail.send(msg)
