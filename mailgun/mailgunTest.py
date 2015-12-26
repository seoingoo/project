import requests
# Sending e-mail
def send_email() :
	return requests.post(
		"https://api.mailgun.net/v3/sandboxd13de7857b744ce1872cea0b767eeb12.mailgun.org/messages",
		auth=("api", "key-3d3d6b97bec40a2d401864e20179a949"),
		data={"from": "mailgun test <mailgun@test>",
		"to": ["gadin.kang@gmail.com"],
		"subject": "[test mailgun] Mail Gun Test With Github Address",
		"text": "Seoingoo, Mail Gun Last  Test\n\n  https://github.com/seoingoo/project"})

if __name__ == "__main__" :
	send_email()


