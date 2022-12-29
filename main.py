#!/usr/bin/python

"""
Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
"""



# Required modules
import threading
import requests
import random
import json
import os

# Do not modify this part (Used for temporary memory)
loopback = 0
logtype = 0


# Terminal Purger
def clean_af():
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")


# Main Runner
def main():
	# Open required files
	with open("target.json", "r") as ft:
		targets = json.load(ft)
	with open("sources/proxylist.json", "r") as fp:
		proxies = json.load(fp)
	with open("sources/useragent.json", "r") as fu:
		useragents = json.load(fu)
	with open("sources/raw_userdata.json", "r") as fr:
		raw_userdatas = json.load(fr)
	with open(".logs", "a") as fl:
		logfile = fl

	# Count all inputted targets on "target.json"
	def count_attributes():
		global loopback
		loopback = loopback + len(targets["attributes"])

	# Prompt the user before launching an attack!
	def prompt():
		global logtype
		interface_1 = input(f'\n\n"{loopback}" targeted sites are found in "target.json". Please check your inputted data to minimize errors.\n ~ Continue? [Y/N] ')
		if not interface_1 in ["Y", "y"]:
			exit("Thank you for choosing PSpammer!")
		interface_2 = input('What type of posts spam log you want to use?\n [01] In-Terminal-Logging Only (Best for long attacks - Recommended)\n [02] On-File-Logging (Best for quick diagnostic attack - Not Recommended)\n [03] Both (Use this if you like option 1 and 2 at the same time)\n [04] None (Only Shows Status Codes And Text - Recommended)\n ~ Answer: ')
		if interface_2 == 1:
			logtype = logtype + 1
		elif interface_2 == 2:
			logtype = logtype + 2
		elif interface_2 == 3:
			logtype = logtype + 3
		else:
			logtype = logtype + 4

	def loghandler(status, text, id, proxy, payload1, payload2):
		if logtype == 1:
			print(f'Status Code: {status} | Target: {id} | Text: {text} | Proxy: {proxy} | Header: {payload1} | Form | {payload2}')
		elif logtype == 2:
			print(f'Status Code: {status} | Target: {id} | Text: {text}')
			logfile.write(status + text)
		elif logtype == 3:
			print(f'Status Code: {status} | Target: {id} | Text: {text} | Proxy: {proxy} | Header: {payload1} | Form | {payload2}')
			logfile.write(status + text)
		else:
			print(f'Status Code: {status} | Target: {id} | Text: {text}')
			print(status)

	# Parsing up some necessary data that doesn't require to be randomized and store it in memory to improve performance
	userdata = raw_userdatas["attributes"][0]
	par_firstname = userdata["common_firstnames"]
	par_lastname = userdata["common_lastnames"]
	par_modname = userdata["common_modnames"]
	par_webname = userdata["common_webnames"]
	par_email = userdata["common_email_names"]
	par_password = userdata["common_passwords"]
	par_domain = userdata["common_domains"]
	par_scrambler = userdata["scramblers"]
	par_symbol = userdata["symbols"]

	par_useragent = useragents["headers"]

	par_proxy = proxies["headers"]

	def attack():
		for loop in range(0, int(loopback)):
			# Loops for every target that the user has encoded in "target.json" and read its form names
			id = targets["attributes"][loop]["id"]
			post_link = targets["attributes"][loop]["post_link"]
			header = targets["attributes"][loop]["headers"]

			form = targets["attributes"][loop]["forms"]
			input_username = form["username_form_name"]
			input_password = form["password_form_name"]
			input_ip = form["ip_form_name"]

			custom = targets["attributes"][loop]["custom"]
			certificate = custom["certificate"]
			timeout = custom["timeout"]
			threading_value = custom["threading_value"]

			# Generate useless data to validate as valid when posted
			gen_firstname = random.choice(par_firstname)
			gen_lastname = random.choice(par_lastname)
			gen_modname = random.choice(par_modname)
			gen_webname = random.choice(par_webname)
			gen_email = random.choice(par_email)
			gen_password = random.choice(par_password)
			gen_domain = random.choice(par_domain)
			gen_scrambler = random.choice(par_scrambler)
			gen_symbol = random.choice(par_symbol)

			gen_proxy = random.choice(par_proxy)

			# Generating multiple variants to make it more random and legit
			variant_1_username = random.choice([gen_firstname + gen_symbol + gen_lastname, gen_lastname + gen_symbol + gen_firstname]) + "@" + gen_email + "." + gen_domain
			variant_2_username = random.choice([gen_firstname + gen_symbol + gen_scrambler, gen_lastname + gen_symbol + gen_scrambler, gen_scrambler + gen_symbol + gen_firstname, gen_scrambler + gen_symbol + gen_lastname]) + "@" + gen_email + "." + gen_domain
			variant_3_username = gen_modname + "@" + gen_webname + "." + gen_domain

			variant_1_password = random.choice([gen_firstname + gen_symbol + gen_lastname, gen_lastname + gen_symbol + gen_firstname, gen_firstname + gen_symbol + gen_scrambler, gen_lastname + gen_symbol + gen_scrambler, gen_scrambler + gen_symbol + gen_firstname, gen_scrambler + gen_symbol + gen_lastname]) + " " + gen_password
			variant_2_password = random.choice([gen_password + gen_symbol + gen_scrambler, gen_scrambler + gen_symbol + gen_password])
			variant_3_password = random.choice([gen_password + gen_symbol + gen_scrambler + gen_symbol + gen_password + gen_firstname, gen_password + gen_symbol + gen_scrambler + gen_symbol + gen_password + gen_lastname])

			# Randomly choose different variants
			chosen_variant_username = random.choice([variant_1_username, variant_2_username, variant_3_username])
			chosen_variant_password = random.choice([variant_1_password, variant_2_password, variant_3_password])

			# Formats
			proxy = {'http':gen_proxy, 'https':gen_proxy}
			if certificate == 0:
				cert_conv = False
			else:
				cert_conv = True

			# Just incase "User-Agent" word where found in header
			if header in ["user-agent", "User-Agent"]:
				main_header = header
			else:
				gen_useragent = random.choice(par_useragent)
				main_header = header | {"User-Agent":gen_useragent}

			# Making "IP Form" optional and process its data according to its source
			if input_ip == "":
				main_form = {input_username:chosen_variant_username, input_password:chosen_variant_password}
			else:
				main_form = {input_username:chosen_variant_username, input_password:chosen_variant_password, input_ip:gen_proxy}

			def Sender():
				while True:
					try:
						Spammer = requests.get(url=post_link, timeout=timeout, data=main_form, headers=main_header, proxies=proxy, cert=cert_conv)
						print("[Console] Status: Request Sent")
						loghandler(status=Spammer.status_code, text="Request Posted", id=id, proxy=gen_proxy, payload1=main_header, payload2=main_form)
					except requests.ReadTimeout:
						loghandler(status="Unknown", text="Request Blocked", id=id, proxy=gen_proxy, payload1=main_header, payload2=main_form)
						continue
					except (requests.ConnectTimeout, requests.ConnectionError):
						loghandler(status="Unknown", text="Sent Failed -> Possible Cause: No Internet/Request Block", id=id, proxy=gen_proxy, payload1=main_header, payload2=main_form)
						continue
					except requests.RequestException:
						print("[Error] Invalid Url!!! Stopping Process...")
						exit("\n\n Code:Invurl")

			def Threader():
				threads = []
				for i in range(threading_value):
					t = threading.Thread(target=Sender)
					t.daemon = True
					threads.append(t)
				for i in range(threading_value):
					threads[i].start()
				for i in range(threading_value):
					threads[i].join()

			Threader()
	count_attributes()
	prompt()
	attack()


# Initiator
if __name__ == "__main__":
	try:
		clean_af()
		print("Phishing link Spammer (PSpammer) version 3 (Beta) || DO NOT DISTRIBUTE WITHOUT PERMISSION")
		"If you are planning to add a flask here to be available 24/7 on replit, Please add bellow this line for it to work."

		main()
	except KeyboardInterrupt:
		exit("\n\nThank you for choosing PSpammer!")
