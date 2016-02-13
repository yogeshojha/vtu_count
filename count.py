import mechanize

start = 1
end = 100
list_usn = [format(a, "03d") for a in range(start,end)]
fcd, fc, fail, sc, na = 0, 0, 0, 0, 0

for i in list_usn:
	br = mechanize.Browser()
	br.open("http://results.vtu.ac.in")
	br.select_form(name = "new")


	base_usn = "1ep14cv"

	usn = base_usn + str(i)
	br["rid"] = usn
	response = br.submit()
	a = response.get_data()

	if "FIRST CLASS WITH DISTINCTION" in a:
		fcd = fcd + 1

	elif "FIRST CLASS" in a:
		fc = fc + 1

	elif "SECOND CLASS" in a:
		sc = sc + 1

	elif "FAIL" in a:
		fail = fail + 1
	
	else:
		na = na + 1

print "\n\nResults:" 
print "First Class Distinction =",fcd
print "First Class =",fc
print "Second Class=",sc
print "Fail =",fail
print "N.A =",na,"\n"
