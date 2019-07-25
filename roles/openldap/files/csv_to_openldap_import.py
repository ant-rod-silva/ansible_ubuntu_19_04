```
import csv
import ldap
import ldap.modlist as modlist
 
try:
    conn = ldap.initialize('ldap://localhost:389')
    conn.simple_bind_s('cn=admin,dc=example,dc=com', 'abcd1234')
 
except ldap.LDAPError, e:
    print e
 
with open('/etc/ansible/roles/openldap/files/openldap_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    uid = 48059
    for row in readCSV:
 
        dn = "uid={},{}".format(str(row[3]), "ou=People,dc=example,dc=com")
        print "Adding: {}".format(dn)
 
        attrs = {}
        #attrs['objectclass'] = ['top','posixAccount','inetOrgPerson']
        attrs['objectclass'] = ['ServidorPublicoObjectClass']
        attrs['dn'] = str(dn)
        attrs['givenName'] = str(row[1])
        attrs['sn'] = str(row[2])
        attrs['cn'] = str(row[3])
        attrs['displayName'] = str(row[4])
        attrs['description'] = str(row[5])
        attrs['mail'] = str(row[6])
        attrs['userPassword'] = str(row[7])
        
        #attrs['uid'] = str(row[4])
        #attrs['uidNumber'] = str(uid)
        #attrs['gidNumber'] = '0'
        #attrs['homeDirectory'] = str(row[4])
        
        ldif = modlist.addModlist(attrs)
 
        # print "ldif" + str(ldif)
        conn.add_s(dn,ldif)
 
        #uid = uid + 1
 
conn.unbind_s()
print "All Done"
```
