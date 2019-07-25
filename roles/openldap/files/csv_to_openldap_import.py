import csv
import ldap
import ldap.modlist as modlist
 
try:
    conn = ldap.initialize('ldap://localhost:389')
    conn.simple_bind_s('cn=admin,dc=example,dc=com', 'abcd1234')
 
except ldap.LDAPError, e:
    print e
 
with open('/etc/ansible/roles/openldap/files/openldap_data.csv') as csvfile:
    input_file = csv.DictReader(csvfile, delimiter=',')
    for row in input_file:
        dn = "uid={},{}".format(row["cn"], "ou=People,dc=example,dc=com")
        print("Adding: {}".format(dn))
 
        attrs = {}
        #attrs['objectclass'] = ['top','posixAccount','inetOrgPerson']
        attrs['objectclass'] = ['ServidorPublicoObjectClass']
        attrs['sAMAccountName'] = str(row['sAMAccountName'])
        attrs['givenName'] = str(row['givenName'])
        attrs['sn'] = str(row['sn'])
        attrs['cn'] = str(row['cn'])
        attrs['displayName'] = str(row['displayName'])
        attrs['description'] = str(row['description'])
        attrs['title'] = str(row['title'])
        attrs['mail'] = str(row['mail'])
        attrs['userPassword'] = str(row['userPassword'])
        
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

