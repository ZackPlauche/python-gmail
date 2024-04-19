from gmail import GmailClient


def test_gmail():
    gmail = GmailClient.from_env()
    gmail.send_email(
        gmail.email,
        'Test email',
        'This is a test email',
    )
