#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import string
import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

one   = color.RED + "(1)" + color.END
two   = color.RED + "(2)" + color.END
three = color.RED + "(3)" + color.END
four  = color.RED + "(4)" + color.END
five  = color.RED + "(5)" + color.END
six   = color.RED + "(6)" + color.END
seven = color.RED + "(7)" + color.END
eight = color.RED + "(8)" + color.END
nine  = color.RED + "(9)" + color.END
ten   = color.RED + "(10)" + color.END
eleven= color.RED + "(11)" + color.END
twelve= color.RED + "(12)" + color.END
thirth= color.RED + "(13)" + color.END
fourth= color.RED + "(14)" + color.END
fifth = color.RED + "(15)" + color.END
sixth = color.RED + "(16)" + color.END
svnth = color.RED + "(17)" + color.END
ninety= color.RED + "(99)" + color.END


####################### Findmyhash ############################
def findmyhash():
	services_title = """	** Hash ALgorithms  **"""
	findmyhash_processes = """
	%s  MD4	- RFC 1320		  %s  MD5	 - RFC 1321
	%s  SHA1	- RFC 3174 (FIPS 180-3)	  %s  SHA224    - RFC 3874 (FIPS 180-3)
	%s  SHA256	- FIPS 180-3		  %s  SHA384    - FIPS 180-3
	%s  SHA512	- FIPS 180-3		  %s  RMD160    - RFC 2857
	%s  GOST	- RFC 5831		  %s WHIRLPOOL - ISO/IEC 10118-3:2004
	%s LM		- Microsoft Windows hash  %s NTLM      - Microsoft Windows hash
	%s MYSQL	- MySQL 3, 4, 5 hash	  %s CISCO7    - Cisco IOS type 7 encrypted passwords
	%s LDAP_MD5	- MD5 Base64 encoded	  %s LDAP_SHA1 - SHA1 Base64 encoded
	%s JUNIPER	- Juniper Networks
	
	%s Ana Menüye Dön
	"""%(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirth,fourth,fifth,sixth,svnth,ninety)
	print findmyhash_processes
	
	findmyhash_process = input(color.YELLOW + "Yukarıdaki findmyhash yöntemlerinden birisini seçiniz : " + color.END)
	if findmyhash_process ==1 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash MD4 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash MD4 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==2 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash MD5 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash MD5 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==3 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash SHA1 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash SHA1 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==4 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash SHA224 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash SHA224 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==5 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash SHA256 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash SHA256 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==6 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash SHA384 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash SHA384 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==7 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash SHA512 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash SHA512 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==8 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash RMD160 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash RMD160 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==9 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash GOST -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash GOST -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==10 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash WHIRLPOOL -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash WHIRLPOOL -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==11 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash LM -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash LM -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==12 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash NTLM -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash NTLM -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==13 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash MYSQL -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash MYSQL -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==14 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash CISCO7 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash CISCO7 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==15 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash LDAP_MD5 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash LDAP_MD5 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==16 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash LDAP_SHA1 -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash LDAP_SHA1 -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process ==17 :
		hash = raw_input(color.BLUE + "Hash giriniz  :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, findmyhash ile %s'ne karşı başlatıldı.\n" %(hash) + color.END
		findmyhash = "python /usr/bin/findmyhash JUNIPER -h %s"%hash
		print color.RED + """	******************************************************************
	*  python /usr/bin/findmyhash JUNIPER -h %s
	******************************************************************
	"""%(hash) + color.END
		os.system(findmyhash)

	elif findmyhash_process == 99 :
		os.system("python brutfort.py")
	else : 
		print color.RED + "\nYanlış seçim yaptınız. Lütfen kontrol edip tekrar deneyiniz." + color.END
		time.sleep(3)
		os.system("python brutfort.py")
####################### Findmyhash ############################



####################### Medusa ############################
def medusa():
	mods_title = """	** Mods  **"""
	medusa_processes = """
		%s  Kullanıcı adı ve parola
		%s  Kullanıcı adı ve parola dosyası
		%s  Kullanıcı adı dosyası ve parola
		%s  Kullanıcı adı dosyası ve parola dosyası
		%s  Combo dosyası

		%s Ana Menüye Dön
	"""%(one,two,three,four,five,ninety)
	print medusa_processes
	medusa_process = input(color.YELLOW + "Yukarıdaki medusa yöntemlerinden birisini seçiniz : " + color.END)
	if medusa_process ==1 :
		user_name = raw_input(color.BLUE + "Kullanıcı adını giriniz : " + color.END)
		password  = raw_input(color.BLUE + "Parolayı giriniz        : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     : " + color.END)
		print ""		
		print color.RED + mods_title + color.END
		mods      ="""	cvs, ftp, http, imap, mssql, mysql, ncp, nntp, pcanywhere, pop3, postgres, rexec, rlogin, 
	rsh, smbnt, smtp, smtp-vrfy, snmp, ssh, svn, telnet, vmauthd, vnc, web-form, wrapper       
		"""
		print mods
		mod	  = raw_input(color.BLUE + "Mod giriniz             : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Medusa ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		medusa= "medusa -u %s -p %s -h %s -M %s" %(user_name,password,ip_address,mod)
		print color.RED + """	******************************************************************
	*  medusa -u %s -p %s -h %s -M %s
	******************************************************************
	"""%(user_name,password,ip_address,mod) + color.END 
		os.system(medusa) 
	elif medusa_process ==2 :        
		user_name = raw_input(color.BLUE + "Kullanıcı adını giriniz					   : " + color.END)
		password  = raw_input(color.BLUE + "Parola dosya uzantısını giriniz (Ör:/root/Desktop/pass.txt): " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz					   : " + color.END)
		print ""
		print color.RED + mods_title + color.END
		mods      = """	cvs, ftp, http, imap, mssql, mysql, ncp, nntp, pcanywhere, pop3, postgres, rexec, rlogin, 
	rsh, smbnt, smtp, smtp-vrfy, snmp, ssh, svn, telnet, vmauthd, vnc, web-form, wrapper       
		"""
		print mods
		mod	  = raw_input(color.BLUE + "Mod giriniz						   : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Medusa ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		medusa= "medusa -u %s -P %s -h %s -M %s" %(user_name,password,ip_address,mod)
		print color.RED + """	******************************************************************
	*  medusa -u %s -P %s -h %s -M %s
	******************************************************************
	"""%(user_name,password,ip_address,mod) + color.END
		os.system(medusa)
	elif medusa_process ==3 :
		user_name = raw_input(color.BLUE + "Kullanıcı adı dosya uzantısını giriniz(Ör:/root/Desktop/user.txt): " + color.END)
		password  = raw_input(color.BLUE + "Parolayı giriniz						 : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     					 : " + color.END)
		print ""
		print color.RED + mods_title + color.END
		mods      = """	cvs, ftp, http, imap, mssql, mysql, ncp, nntp, pcanywhere, pop3, postgres, rexec, rlogin, 
	rsh, smbnt, smtp, smtp-vrfy, snmp, ssh, svn, telnet, vmauthd, vnc, web-form, wrapper       
		"""
		print mods
		mod	  = raw_input(color.BLUE + "Mod giriniz							 : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Medusa ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		medusa= "medusa -U %s -p %s -h %s -M %s" %(user_name,password,ip_address,mod)
		print color.RED + """	******************************************************************
	*  medusa -U %s -p %s -h %s -M %s
	******************************************************************
	"""%(user_name,password,ip_address,mod) + color.END
		os.system(medusa)
	elif medusa_process ==4 :
		user_name = raw_input(color.BLUE + "Kullanıcı adı dosya uzantısını giriniz(Ör:/root/Desktop/user.txt): " + color.END)
		password  = raw_input(color.BLUE + "Parola dosya uzantısını giriniz(Ör:/root/Desktop/pass.txt)	 : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     					 : " + color.END)
		print ""
		print color.RED + mods_title + color.END
		mods      = """	cvs, ftp, http, imap, mssql, mysql, ncp, nntp, pcanywhere, pop3, postgres, rexec, rlogin, 
	rsh, smbnt, smtp, smtp-vrfy, snmp, ssh, svn, telnet, vmauthd, vnc, web-form, wrapper       
		"""
		print mods
		mod	  = raw_input(color.BLUE + "Mod giriniz							 : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Medusa ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		medusa= "medusa -U %s -P %s -h %s -M %s" %(user_name,password,ip_address,mod)
		print color.RED + """	******************************************************************************************************
	*  medusa -U %s -P %s -h %s -M %s
	******************************************************************************************************
	""" %(user_name,password,ip_address,mod) + color.END
		os.system(medusa)
	elif medusa_process ==5 :
		combo     = raw_input(color.BLUE + "Combo dosya uzantısını giriniz(Ör:/root/Desktop/combo.txt): " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz				 	  : " + color.END)
		print ""
		print color.RED + mods_title + color.END
		mods      = """	cvs, ftp, http, imap, mssql, mysql, ncp, nntp, pcanywhere, pop3, postgres, rexec, rlogin, 
	rsh, smbnt, smtp, smtp-vrfy, snmp, ssh, svn, telnet, vmauthd, vnc, web-form, wrapper       
		"""
		print mods
		mod	  = raw_input(color.BLUE + "Mod giriniz					 	  : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Medusa ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		medusa= "medusa -C %s -h %s -M %s" %(combo,ip_address,mod)
		print color.RED + """	******************************************************************
	*  medusa -C %s -h %s -M %s
	******************************************************************
	""" %(combo,ip_address,mod) + color.END
		os.system(medusa)

	elif medusa_process == 99:
		os.system("python brutfort.py")


	else : 
		print color.RED + "\nYanlış seçim yaptınız. Lütfen kontrol edip tekrar deneyiniz." + color.END
		time.sleep(3)
		os.system("python brutfort.py")

####################### Medusa ############################	

####################### Hydra ############################
def hydra():
	services_title = """	** Services  **"""
	hydra_processes = """
		%s  Kullanıcı adı ve parola
		%s  Kullanıcı adı ve parola dosyası
		%s  Kullanıcı adı dosyası ve parola
		%s  Kullanıcı adı dosyası ve parola dosyası
		%s  Combo dosyası

		%s Ana Menüye Dön
	"""%(one,two,three,four,five,ninety)
	print hydra_processes
	hydra_process = input(color.YELLOW + "Yukarıdaki hydra yöntemlerinden birisini seçiniz : " + color.END)
	if hydra_process ==1 :
		user_name = raw_input(color.BLUE + "Kullanıcı adını giriniz : " + color.END)
		password  = raw_input(color.BLUE + "Parolayı giriniz        : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     : " + color.END)
		print ""		
		print color.RED + services_title + color.END
		services      ="""	asterisk, cisco, cisco-enable, cvs, firebird, ftp, ftps, http[s]-{head|get}, http[s]-{get|post}-form, http-proxy,
	http-proxy-urlenum, icq, imap[s], irc, ldap2[s], ldap3[-{cram|digest}md5][s], mssql, mysql, nntp, oracle-listener, 
	oracle-sid, pcanywhere, pcnfs, pop3[s], postgres, rdp, redis, rexec, rlogin, rsh, s7-300, sip, smb, smtp[s], 
	smtp-enum, snmp, socks5, ssh, sshkey, teamspeak, telnet[s], vmauthd, vnc, xmpp
	"""
		print services
		mod	  = raw_input(color.BLUE + "Servis giriniz          : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Hydra ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		hydra= "hydra -l %s -p %s %s://%s" %(user_name,password,mod,ip_address)
		print color.RED + """	******************************************************************
	*  hydra -l %s -p %s %s://%s
	******************************************************************
	"""%(user_name,password,mod,ip_address) + color.END 
		os.system(hydra) 
	elif hydra_process ==2 :        
		user_name = raw_input(color.BLUE + "Kullanıcı adını giriniz					   : " + color.END)
		password  = raw_input(color.BLUE + "Parola dosya uzantısını giriniz (Ör:/root/Desktop/pass.txt): " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz					   : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	asterisk, cisco, cisco-enable, cvs, firebird, ftp, ftps, http[s]-{head|get}, http[s]-{get|post}-form, http-proxy,
	http-proxy-urlenum, icq, imap[s], irc, ldap2[s], ldap3[-{cram|digest}md5][s], mssql, mysql, nntp, oracle-listener, 
	oracle-sid, pcanywhere, pcnfs, pop3[s], postgres, rdp, redis, rexec, rlogin, rsh, s7-300, sip, smb, smtp[s], 
	smtp-enum, snmp, socks5, ssh, sshkey, teamspeak, telnet[s], vmauthd, vnc, xmpp
	"""
		print services
		mod	  = raw_input(color.BLUE + "Servis giriniz						   : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Hydra ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		hydra= "hydra -l %s -P %s %s://%s" %(user_name,password,mod,ip_address)
		print color.RED + """	******************************************************************
	*  hydra -l %s -P %s %s://%s
	******************************************************************
	"""%(user_name,password,mod,ip_address) + color.END
		os.system(hydra)
	elif hydra_process ==3 :
		user_name = raw_input(color.BLUE + "Kullanıcı adı dosya uzantısını giriniz(Ör:/root/Desktop/user.txt): " + color.END)
		password  = raw_input(color.BLUE + "Parolayı giriniz						 : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     					 : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	asterisk, cisco, cisco-enable, cvs, firebird, ftp, ftps, http[s]-{head|get}, http[s]-{get|post}-form, http-proxy,
	http-proxy-urlenum, icq, imap[s], irc, ldap2[s], ldap3[-{cram|digest}md5][s], mssql, mysql, nntp, oracle-listener, 
	oracle-sid, pcanywhere, pcnfs, pop3[s], postgres, rdp, redis, rexec, rlogin, rsh, s7-300, sip, smb, smtp[s], 
	smtp-enum, snmp, socks5, ssh, sshkey, teamspeak, telnet[s], vmauthd, vnc, xmpp
	"""
		print services
		mod	  = raw_input(color.BLUE + "Servis giriniz							 : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Hydra ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		hydra= "hydra -L %s -p %s %s://%s" %(user_name,password,mod,ip_address)
		print color.RED + """	******************************************************************
	*  hydra -L %s -p %s %s://%s
	******************************************************************
	"""%(user_name,password,mod,ip_address) + color.END
		os.system(hydra)
	elif hydra_process ==4 :
		user_name = raw_input(color.BLUE + "Kullanıcı adı dosya uzantısını giriniz(Ör:/root/Desktop/user.txt): " + color.END)
		password  = raw_input(color.BLUE + "Parola dosya uzantısını giriniz(Ör:/root/Desktop/pass.txt)	 : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     					 : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	asterisk, cisco, cisco-enable, cvs, firebird, ftp, ftps, http[s]-{head|get}, http[s]-{get|post}-form, http-proxy,
	http-proxy-urlenum, icq, imap[s], irc, ldap2[s], ldap3[-{cram|digest}md5][s], mssql, mysql, nntp, oracle-listener, 
	oracle-sid, pcanywhere, pcnfs, pop3[s], postgres, rdp, redis, rexec, rlogin, rsh, s7-300, sip, smb, smtp[s], 
	smtp-enum, snmp, socks5, ssh, sshkey, teamspeak, telnet[s], vmauthd, vnc, xmpp
	"""
		print services
		mod	  = raw_input(color.BLUE + "Servis giriniz							 : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Hydra ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		hydra= "hydra -L %s -P %s %s://%s" %(user_name,password,mod,ip_address)
		print color.RED + """	******************************************************************************************************
	*  hydra -L %s -P %s %s://%s
	******************************************************************************************************
	""" %(user_name,password,mod,ip_address) + color.END
		os.system(hydra)
	elif hydra_process ==5 :
		combo     = raw_input(color.BLUE + "Combo dosya uzantısını giriniz(Ör:/root/Desktop/combo.txt): " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz				 	  : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	asterisk, cisco, cisco-enable, cvs, firebird, ftp, ftps, http[s]-{head|get}, http[s]-{get|post}-form, http-proxy,
	http-proxy-urlenum, icq, imap[s], irc, ldap2[s], ldap3[-{cram|digest}md5][s], mssql, mysql, nntp, oracle-listener, 
	oracle-sid, pcanywhere, pcnfs, pop3[s], postgres, rdp, redis, rexec, rlogin, rsh, s7-300, sip, smb, smtp[s], 
	smtp-enum, snmp, socks5, ssh, sshkey, teamspeak, telnet[s], vmauthd, vnc, xmpp
	"""
		print services
		mod	  = raw_input(color.BLUE + "Servis giriniz					 	  : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, Hydra ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,mod) + color.END
		hydra= "hydra -C %s %s://%s" %(combo,mod,ip_address)
		print color.RED + """	******************************************************************
	*  hydra -C %s %s://%s
	******************************************************************
	""" %(combo,mod,ip_address) + color.END
		os.system(hydra)

	elif hydra_process == 99:
		os.system("python brutfort.py")


	else : 
		print color.RED + "\nYanlış seçim yaptınız. Lütfen kontrol edip tekrar deneyiniz." + color.END
		time.sleep(3)
		os.system("python brutfort.py")

####################### Hydra ############################

####################### Ncrack ############################
def ncrack():
	services_title = """	** Modules  **"""
	ncrack_processes = """
		%s  Kullanıcı adı ve parola
		%s  Kullanıcı adı ve parola dosyası
		%s  Kullanıcı adı dosyası ve parola
		%s  Kullanıcı adı dosyası ve parola dosyası

		%s Ana Menüye Dön
	"""%(one,two,three,four,ninety)
	print ncrack_processes
	ncrack_process = input(color.YELLOW + "Yukarıdaki ncrack yöntemlerinden birisini seçiniz : " + color.END)
	if ncrack_process ==1 :
		user_name = raw_input(color.BLUE + "Kullanıcı adını giriniz : " + color.END)
		password  = raw_input(color.BLUE + "Parolayı giriniz        : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     : " + color.END)
		print ""		
		print color.RED + services_title + color.END
		services      ="""	FTP(21), SSH(22), TELNET(23), HTTP(S)(80-443), 
	POP3(S)(110-995), SMB(445), RDP(3389), VNC(5900)
	"""
		print services
		port	  = input(color.BLUE + "Port numarasını giriniz	: " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, ncrack ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,port) + color.END
		ncrack= "ncrack --user %s --pass %s -p %d %s" %(user_name,password,port,ip_address)
		print color.RED + """	******************************************************************
	*  ncrack --user %s --pass %s -p %d %s
	******************************************************************
	"""%(user_name,password,port,ip_address) + color.END 
		os.system(ncrack) 
	elif ncrack_process ==2 :        
		user_name = raw_input(color.BLUE + "Kullanıcı adını giriniz					   : " + color.END)
		password  = raw_input(color.BLUE + "Parola dosya uzantısını giriniz (Ör:/root/Desktop/pass.txt): " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz					   : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	FTP(21), SSH(22), TELNET(23), HTTP(S)(80-443), 
	POP3(S)(110-995), SMB(445), RDP(3389), VNC(5900)
	"""
		print services
		port	  = input(color.BLUE + "Port numarasını giriniz					   : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, ncrack ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,port) + color.END
		ncrack= "ncrack --user %s -P %s -p %d %s" %(user_name,password,port,ip_address)
		print color.RED + """	******************************************************************
	*  ncrack --user %s -P %s -p %d %s
	******************************************************************
	"""%(user_name,password,port,ip_address) + color.END
		os.system(ncrack)
	elif ncrack_process ==3 :
		user_name = raw_input(color.BLUE + "Kullanıcı adı dosya uzantısını giriniz(Ör:/root/Desktop/user.txt): " + color.END)
		password  = raw_input(color.BLUE + "Parolayı giriniz						 : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     					 : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	FTP(21), SSH(22), TELNET(23), HTTP(S)(80-443), 
	POP3(S)(110-995), SMB(445), RDP(3389), VNC(5900)
	"""
		print services
		port	  = input(color.BLUE + "Port numarasını giriniz						 : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, ncrack ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,port) + color.END
		ncrack= "ncrack -U %s --pass %s -p %d %s" %(user_name,password,port,ip_address)
		print color.RED + """	******************************************************************
	*  ncrack -U %s --pass %s -p %d %s
	******************************************************************
	"""%(user_name,password,port,ip_address) + color.END
		os.system(ncrack)
	elif ncrack_process ==4 :
		user_name = raw_input(color.BLUE + "Kullanıcı adı dosya uzantısını giriniz(Ör:/root/Desktop/user.txt): " + color.END)
		password  = raw_input(color.BLUE + "Parola dosya uzantısını giriniz(Ör:/root/Desktop/pass.txt)	 : " + color.END)
		ip_address= raw_input(color.BLUE + "IP adresini giriniz     					 : " + color.END)
		print ""
		print color.RED + services_title + color.END
		services      ="""	FTP(21), SSH(22), TELNET(23), HTTP(S)(80-443), 
	POP3(S)(110-995), SMB(445), RDP(3389), VNC(5900)
	"""
		print services
		port	  = input(color.BLUE + "Port numarasını giriniz						 : " + color.END)
		print ""
		print color.YELLOW + "\tBrute Force, ncrack ile %s IP adresine %s modunda başlatıldı.\n" %(ip_address,port) + color.END
		ncrack= "ncrack -U %s -P %s -p %d %s" %(user_name,password,port,ip_address)
		print color.RED + """	******************************************************************************************************
	*  ncrack -U %s -P %s -p %d %s
	******************************************************************************************************
	""" %(user_name,password,port,ip_address) + color.END
		os.system(ncrack)

	elif ncrack_process == 99:
		os.system("python brutfort.py")


	else : 
		print color.RED + "\nYanlış seçim yaptınız. Lütfen kontrol edip tekrar deneyiniz." + color.END
		time.sleep(3)
		os.system("python brutfort.py")


####################### Ncrack ############################


####################### HashID ############################
def hashid():
	print color.BLUE + "\nHash Identifier, elde edilen hashli parolaları kırmak için, bu hashlerin tipini belirleyebilmemizi sağlar.\n" + color.END
	os.system("hash-identifier") 
	
####################### HashID ############################


####################### John ############################
def john():
	format_type_title="""	
	** HASH Tipleri ** """
	format_types = """	afs, bf, bfegg, bsdi, crc32, crypt,
	des, django, dmd5, dominosec, dragonfly3-32, dragonfly3-64,
	dragonfly4-32, dragonfly4-64, drupal7, dummy, dynamic_n,
	epi, episerver, gost, hdaa, hmac-md5, hmac-sha1,
	hmac-sha224, hmac-sha256, hmac-sha384, hmac-sha512,
	hmailserver, ipb2, keepass, keychain, krb4, krb5, lm, lotus5,
	md4-gen, md5, md5ns, mediawiki, mscash, mscash2, mschapv2,
	mskrb5, mssql, mssql05, mysql, mysql-sha1, nethalflm, netlm,
	netlmv2, netntlm, netntlmv2, nsldap, nt, nt2, odf, office,
	oracle, oracle11, osc, pdf, phpass, phps, pix-md5, pkzip, po,
	pwsafe, racf, rar, raw-md4, raw-md5, raw-md5u, raw-sha,
	raw-sha1, raw-sha1-linkedin, raw-sha1-ng, raw-sha224,
	raw-sha256, raw-sha384, raw-sha512, salted-sha1, sapb,
	sapg, sha1-gen, sha256crypt, sha512crypt, sip, ssh,
	sybasease, trip, vnc, wbb3, wpapsk, xsha, xsha512, zip
	"""
	
	print color.RED + format_type_title + color.END
	print format_types
	format_type = raw_input(color.BLUE + "Format tipini giriniz           : " + color.END)
	hash_file   = raw_input(color.BLUE + "Hash dosya uzantısınızı giriniz : " + color.END)
	john= "john --format=%s %s"%(format_type,hash_file)

	print color.RED + """
	******************************************************************
	*  john --format=%s %s
	******************************************************************
	"""%(format_type,hash_file) + color.END
	os.system(john) 
####################### John ############################


####################### Truecrack ############################
def truecrack():
	print color.YELLOW + "\nTruecrack, Truecrypt ile şifrelenmiş dosyalara kaba kuvvet saldırısı yapabilmemizi sağlar.\n" + color.END	
	
	truecrypt_file = raw_input(color.BLUE + "Truecrypt ile şifrelenmiş dosyanın uzantısını giriniz(Ör:/root/Desktop/truecrypt_file)	: " + color.END)
	wordlist       = raw_input(color.BLUE + "Saldırı için wordlistin uzantısını giriniz(Ör:/root/Desktop/wordlist_file)		: " + color.END)
	keys_title     = """\n	** Keys **"""	
	print color.RED + keys_title + color.END
	keys 	       = """	%s ripemd160	%s sha512	%s whirlpool
	"""%(one,two,three)
	print keys
	key = input(color.BLUE + "Anahtar türetme işlemi için yukarıdaki maddelerden birisini seçiniz			: " + color.END)
	
	if key==1:
		truecrack= "truecrack -t %s -k ripemd160 -w %s"%(truecrypt_file,wordlist)
		print color.RED + """
	******************************************************************
	*  truecrack -t %s -k ripemd160 -w %s
	******************************************************************
	"""%(truecrypt_file,wordlist) + color.END
	elif key==2:
		truecrack= "truecrack -t %s -k sha512 -w %s"%(truecrypt_file,wordlist)
		print color.RED + """
	******************************************************************
	*  truecrack -t %s -k sha512 -w %s
	******************************************************************
	"""%(truecrypt_file,wordlist) + color.END
	elif key==3:
		truecrack= "truecrack -t %s -k whirlpool -w %s"%(truecrypt_file,wordlist)
		print color.RED + """
	******************************************************************
	*  truecrack -t %s -k whirlpool -w %s
	******************************************************************
	"""%(truecrypt_file,wordlist) + color.END
	else : 
		print color.RED + "Yanlış seçim yaptınız. Lütfen kontrol edip tekrar deneyiniz." + color.END
	os.system(truecrack) 

####################### Truecrack ############################


####################### Pyrit ############################
def pyrit():
	subject = color.YELLOW + "\nPyrit, WPA/WPA2-PSK Şifrelerini kırmak için geliştirilmiş bir yazılımdır. En önemli özelliği CPU’ya ek olarak NVIDIA ve ATI ekran kartlarının grafik işlemcilerini kullanarak parola kırma işlemi yapmasıdır. Özellikle yeni nesil gelişmiş ekran kartlarıyla oldukça iyi performans verebilir ve daha hızlı bir şekilde hash’leri kırmamızı sağlayabilir.\n" + color.END
	pyrit_processes = """
		%s  Kullanılabilecek CPU Ve GPU‘ların listelenmesi
		%s  CPU ve GPU’ların performans testi
		%s  Yakalanan Handshake Analizi
		%s  Şifre kırma saldırısı

		%s Ana Menüye Dön
	"""%(one,two,three,four,ninety)
	print pyrit_processes
	pyrit_process = input(color.YELLOW + "Yukarıdaki pyrit yöntemlerinden birisini seçiniz : " + color.END)
	if pyrit_process ==1 :
		print color.YELLOW + "\n\tKullanılabilecek CPU Ve GPU‘ların listelenmesi başlatıldı.\n" + color.END	
		pyrit= "pyrit list_cores"
		print color.RED + """	******************************************************************
	*  pyrit list_cores
	******************************************************************
	""" + color.END 
		os.system(pyrit) 
	
	elif pyrit_process ==2 :    
		print color.YELLOW + "\n\tCPU ve GPU’ların performans testi başlatıldı.\n" + color.END    
		pyrit= "pyrit benchmark"
		print color.RED + """	******************************************************************
	*  pyrit benchmark
	******************************************************************
	""" + color.END
		os.system(pyrit)
	elif pyrit_process ==3 :        
		handshake = raw_input(color.BLUE + "Yakalanan Handshake dosya uzantısını giriniz(Ör:/root/Desktop/wpahashfile.cap) :  " + color.END)
		print color.YELLOW + "\n\tPyrit ile %s dosyasına analiz başlatıldı.\n" %(handshake) + color.END
		pyrit= "pyrit -r %s analyze" %(handshake)
		print color.RED + """	******************************************************************
	*  pyrit -r %s analyze
	******************************************************************
	"""%(handshake) + color.END
		os.system(pyrit)
	elif pyrit_process ==4 :        
		handshake = raw_input(color.BLUE + "Yakalanan Handshake dosya uzantısını giriniz(Ör:/root/Desktop/wpahashfile.cap):  " + color.END)
		wordlist  = raw_input(color.BLUE + "Wordlist uzantısını giriniz(Ör:/root/Desktop/wordlist.txt)		      :  " + color.END)		
		bssid     = raw_input(color.BLUE + "BSSID giriniz								      :  " + color.END)
		print color.YELLOW + "\n\tBrute Force, Pyrit ile %s dosyasına ve %s BSSID'ye karşı başlatıldı.\n" %(handshake,bssid) + color.END
		pyrit= " pyrit -r  %s -i %s -b %s  attack_passthrough" %(handshake,wordlist,bssid)
		print color.RED + """	******************************************************************
	*   pyrit -r  %s -i %s -b %s  attack_passthrough
	******************************************************************
	"""%(handshake,wordlist,bssid) + color.END
		os.system(pyrit)

	elif pyrit_process == 99:
		os.system("python brutfort.py")


	else :
		print color.RED + "\nYanlış seçim yaptınız. Lütfen, kontrol edip tekrar deneyiniz." + color.END
		time.sleep(3)
		os.system("python brutfort.py")

####################### Pyrit ############################

####################### Crunch ############################
def crunch():
	crunch_processes = """
		%s  Sadece harf ile sözlük oluşturma		     : (Ör:a-z)
		%s  Belirtilen karakterler ile sözlük oluşturma     : (Ör:Ab123.!@, vb.)
		%s  Karakter takımlarını kullanarak sözlük oluşturma: (Ör:hex-lower,symbols14...)
		%s  Özel sözlük oluşturma			     : (Ör:'@', ',', '%%', '^')

		%s Ana Menüye Dön
	"""%(one,two,three,four,ninety)
	print crunch_processes
	crunch_process = input(color.YELLOW + "Yukarıdaki crunch yöntemlerinden birisini seçiniz : " + color.END)
	if crunch_process ==1 :
		print color.YELLOW + "\nBu yöntem ile a-z arasındaki tüm harf kombinasyonları gerçekleştirilir.\n" + color.END
		pass_num1 = input(color.BLUE + "En düşük parola uzunluğunu giriniz  : " + color.END)
		pass_num2 = input(color.BLUE + "En yüksek parola uzunluğunu giriniz : " + color.END)
		output    = raw_input(color.BLUE + "Oluşturulacak dosyanın kaydedileceği dosya uzantısını giriniz(Ör:/root/Desktop/wordlistoutput.txt) : " + color.END)
		crunch= "crunch %s %s -o %s" %(pass_num1,pass_num2,output)
		print color.RED + """\n	******************************************************************
	*  crunch %s %s -o %s
	******************************************************************
	"""%(pass_num1,pass_num2,output) + color.END 
		os.system(crunch)
 
	elif crunch_process ==2 :
		print color.YELLOW + "\nBu yöntem ile belirtilecek karakterler çerçevesindeki kombinasyonlar gerçekleştirilir.\n" + color.END
		pass_num1 = input(color.BLUE + "En düşük parola uzunluğunu giriniz  : " + color.END)
		pass_num2 = input(color.BLUE + "En yüksek parola uzunluğunu giriniz : " + color.END)
		characters= raw_input(color.BLUE + "Oluşturulmak istenen karakterler    : " + color.END)
		output    = raw_input(color.BLUE + "Oluşturulacak dosyanın kaydedileceği dosya uzantısını giriniz(Ör:/root/Desktop/wordlistoutput.txt) : " + color.END)
		crunch= "crunch %s %s %s -o %s" %(pass_num1,pass_num2,characters,output)
		print color.RED + """\n	******************************************************************
	*  crunch %s %s %s -o %s
	******************************************************************
	"""%(pass_num1,pass_num2,characters,output) + color.END 
		os.system(crunch) 

	elif crunch_process ==3 :
		print color.YELLOW + "\nBu yöntem ile hazır karakter takımları kullanılarak sözlük oluşturulur.\n" + color.END
		pass_num1 = input(color.BLUE + "En düşük parola uzunluğunu giriniz  : " + color.END)
		pass_num2 = input(color.BLUE + "En yüksek parola uzunluğunu giriniz : " + color.END)			
		character_sets="""	hex-lower, hex-upper, numeric, numeric-space, symbols14,symbols14-space, 
	symbols-all, symbols-all-space, ualpha,ualpha-space, ualpha-numeric, 
	ualpha-numeric-space, ualpha-numeric-symbol14, ualpha-numeric-symbol14-space,
	ualpha-numeric-all, ualpha-numeric-all-space, lalpha, lalpha-space, lalpha-numeric,           
	lalpha-numeric-space, lalpha-numeric-symbol14, lalpha-numeric-symbol14-space,
	lalpha-numeric-all, lalpha-numeric-all-space, mixalpha, mixalpha-space,
	mixalpha-numeric,mixalpha-numeric-space, mixalpha-numeric-symbol14, 
	mixalpha-numeric-symbol14-space, mixalpha-numeric-all, mixalpha-numeric-all-space, 
	ualpha-sv, ualpha-space-sv, ualpha-numeric-sv, ualpha-numeric-space-sv,          
	ualpha-numeric-symbol14-sv, ualpha-numeric-symbol14-space-sv, ualpha-numeric-all-sv,            
	ualpha-numeric-all-space-sv, lalpha-sv, lalpha-space-sv, lalpha-numeric-sv,     
	lalpha-numeric-space-sv, lalpha-numeric-symbol14-sv,lalpha-numeric-symbol14-space-sv, 
	lalpha-numeric-all-sv, lalpha-numeric-all-space-sv, mixalpha-sv, mixalpha-space-sv,             
	mixalpha-numeric-sv, mixalpha-numeric-space-sv, mixalpha-numeric-symbol14-sv  ,
	mixalpha-numeric-symbol14-space-sv, mixalpha-numeric-all-sv, mixalpha-numeric-all-space-sv,
	"""
		print color.RED + "\n\t** Character Sets **" + color.END
		print character_sets
		print color.YELLOW + "\n\tKarakter takımları hakkında ayrıntılı bilgi edinmek için aşağıdaki komut kullanılabilir." + color.END
		print color.RED + "\tcat /usr/share/crunch/charset.lst\n" + color.END
		character_set= raw_input(color.BLUE + "Karakter takımını giriniz           : " + color.END)
		output    = raw_input(color.BLUE + "Oluşturulacak dosyanın kaydedileceği dosya uzantısını giriniz(Ör:/root/Desktop/wordlistoutput.txt) : " + color.END)
		crunch= "crunch %s %s -f /usr/share/crunch/charset.lst %s -o %s" %(pass_num1,pass_num2,character_set,output)
		print color.RED + """\n	******************************************************************
	*  crunch %s %s -f /usr/share/crunch/charset.lst %s -o %s
	******************************************************************
	"""%(pass_num1,pass_num2,character_set,output) + color.END 
		os.system(crunch) 


	elif crunch_process ==4 :
		print color.YELLOW + "\nBu yöntem ile kendi belirleyeceğiniz formatlarda özel bir sözlük oluşturulur.\n" + color.END
		pass_num = input(color.BLUE + "Parola uzunluğunu giriniz  : " + color.END)
		specifics_char=["@",",","%","^"]		
		specifics=["Küçük harfli karakterleri yazdırmak için","Büyük harfli karakterleri yazdırmak için","Rakam kullanmak için","Özel karakterleri yazdırmak için"]
		i=0
		print ""	
		while i<5:
			print "\t",color.RED + specifics_char[i] + color.END, " : ", specifics[i]
			i+=1
			if i==4:
				break
		print ""
		i=0
		special_pass=[]
		while i<pass_num:
			special_pass.append(raw_input(color.BLUE + "%d. karakteri giriniz       : "%(i+1) + color.END))
			i+=1
		output    = raw_input(color.BLUE + "\nOluşturulacak dosyanın kaydedileceği dosya uzantısını giriniz(Ör:/root/Desktop/wordlistoutput.txt) : " + color.END)
		crunch= "crunch %s %s -t %s -o %s" %(pass_num,pass_num,string.join(special_pass,""),output)
		print color.RED + """\n	******************************************************************
	*  crunch %s %s -t %s -o %s
	******************************************************************
	"""%(pass_num,pass_num,string.join(special_pass,""),output) + color.END 
		os.system(crunch) 

	elif crunch_process == 99:
		os.system("python brutfort.py")


	else :
		print color.RED + "\nYanlış seçim yaptınız. Lütfen, kontrol edip tekrar deneyiniz." + color.END
		time.sleep(3)
		os.system("python brutfort.py")

####################### crunch ############################	


####################### PTHWinexe ############################
def pthwinexe():
	print color.YELLOW + "\nPass-the-hash(pth-winexe), önceden ele geçirilmiş olan ve açık parola yerine parolanın özetini kullanarak sistemlere bağlanılmasını sağlar.\n" + color.END	
	
	user_name = raw_input(color.BLUE + "Ele geçirilen kullanıcı adını giriniz(Ör:Administrator...) : " + color.END)
	pass_hash = raw_input(color.BLUE + "Ele geçirilen parola hash'ini giriniz                      : " + color.END)
	ip_address= raw_input(color.BLUE + "IP adresini giriniz                                        : " + color.END)
	command   = raw_input(color.BLUE + "Sistemde kullanılmak üzere olan komutu giriniz(Ör:cmd.exe) : " + color.END)

	pthwinexe= "pth-winexe -U %s%%%s //%s %s"%(user_name,pass_hash,ip_address,command)
	print color.RED + """
	*****************************************************************************************************
	*  pth-winexe -U %s%%%s //%s %s
	*****************************************************************************************************
	"""%(user_name,pass_hash,ip_address,command) + color.END
	os.system(pthwinexe) 

####################### PTHWinexe ############################

subject = """
###########################################################
#	 ____             _   _____         _____ 	  #
#	| __ ) _ __ _   _| |_|  ___|__  _ _|_   _|	  #
#	|  _ \| '__| | | | __| |_ / _ \| '__|| |          #
#	| |_) | |  | |_| | |_|  _| (_) | |   | |          #
#	|____/|_|   \__,_|\__|_|  \___/|_|   |_|          #
#							  #
###########################################################
"""

print color.BLUE + subject + color.END

title = """###########################################################
#           BRUTE FORCE TOOLKIT v1.0 (BrutForT)  	  #
#---------------------------------------------------------#
#	       	      TOLGA AKKAPULU			  #
#              http://www.tolgaakkapulu.com		  #
#---------------------------------------------------------#
#   https://tr.linkedin.com/in/tolga-akkapulu-518054105   #
#              https://github.com/tolgaakkapulu		  #
###########################################################
"""

print color.RED + title + color.END

processes = """	
	%s  HASH IDENTIFIER	%s  MEDUSA
	%s  FINDMYHASH		%s  HYDRA	
	%s  JOHN		%s  NCRACK	
	%s  TRUECRACK		%s  PYRIT
	%s  PTH-WINEXE		%s CRUNCH
	
	%s BrutForT'dan Çık
"""%(one,six,two,seven,three,eight,four,nine,five,ten,ninety)

print processes

process = input(color.YELLOW + "Yukarıdaki araçlardan birisini seçiniz : " + color.END)


if process == 1:
	hashid()	
elif process == 2:
	findmyhash()
elif process == 3:
	john()
elif process == 4:
	truecrack()
elif process == 5:
	pthwinexe()
elif process == 6:
	medusa()
elif process == 7:
	hydra()
elif process == 8:
	ncrack()
elif process == 9:
	pyrit()
elif process == 10:
	crunch()
elif process ==99:
	exit()
else : 
	print color.RED + "Yanlış seçim yaptınız. Lütfen kontrol edip tekrar deneyiniz." + color.END
	time.sleep(3)
	os.system("python brutfort.py")
	
