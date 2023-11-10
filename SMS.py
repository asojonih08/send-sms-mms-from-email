import smtplib
carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(subject, body):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = '**phone_number**{}'.format(carriers['tmobile'])
	email = '**email**'
	smtp_password = "smtp password"

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(email, smtp_password)

	message = 'Subject: {}\n\n{}'.format(subject, body)
	# Send text message through SMS gateway of destination number
	server.sendmail( email, to_number, message)