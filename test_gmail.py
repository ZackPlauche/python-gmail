import gmail


def test_gmail():
    client = gmail.Client.from_env()
    client.send_email(
        client.email,
        'Test email',
        'This is a test email',
    )
