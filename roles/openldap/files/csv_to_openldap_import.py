```
import csv
import ldap
import ldap.modlist as modlist
 
try:
    conn = ldap.initialize('ldap://localhost:389')
    conn.simple_bind_s('cn=admin,dc=waqar,dc=local', 'admin_password')
 
except ldap.LDAPError, e:
    print e
 
with open('data_file.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    uid = 48059
    for row in readCSV:
        print "Adding " + str( row[0] + " " + row[1] + " " + row[2] + " " + row[3]+ " " + row[4]+ " " + row[5]+ " " + row[6]+ " " + row[7]+ " " + row[8])
 
        dn = "uid="+str(row[4]) + ",ou=" + str(row[1]) + ",ou=" + str(row[0]) + ",ou=students,dc=waqar,dc=local"
 
        attrs = {}
        attrs['objectclass'] = ['top','posixAccount','inetOrgPerson']
        attrs['sn'] = str(row[6])
        attrs['displayName'] = str(row[6])
        attrs['givenName'] = str(row[6])
        attrs['uid'] = str(row[4])
        attrs['uidNumber'] = str(uid)
        attrs['gidNumber'] = '0'
        attrs['homeDirectory'] = str(row[4])
        attrs['mail'] = str(row[8])
        attrs['cn'] = str(row[6])
        attrs['userPassword'] = str(row[5])
        attrs['description'] = str(row[6]) + " Son of " + str(row[7]) + " Student of " + str(row[1]) + " of " + str(row[2])
 
        ldif = modlist.addModlist(attrs)
 
        # print "ldif" + str(ldif)
        conn.add_s(dn,ldif)
 
        uid = uid + 1
 
conn.unbind_s()
print "All Done"
```
