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
        attrs['userPrincipalName'] = str(row['userprincipalname'])
        attrs['sAMAccountName'] = str(row['samaccountname'])
        attrs['cn'] = str(row['cn'])
        attrs['givenName'] = str(row['givenname'])
        attrs['sn'] = str(row['sn'])
        attrs['displayName'] = str(row['displayname'])
        attrs['department'] = str(row['department'])
        attrs['description'] = str(row['description'])
        attrs['title'] = str(row['title'])
        attrs['thumbnailPhoto'] = str(row['thumbnailphoto'])
        attrs['mail'] = str(row['mail'])
        attrs['mailNickname'] = str(row['mailnickname'])
        attrs['extensionAttribute2'] = str(row['extensionattribute2'])
        attrs['extensionAttribute3'] = str(row['extensionattribute3'])
        attrs['extensionAttribute4'] = str(row['extensionattribute4'])
        attrs['extensionAttribute5'] = str(row['extensionattribute5'])
        attrs['extensionAttribute6'] = str(row['extensionattribute6'])
        attrs['extensionAttribute7'] = str(row['extensionattribute7'])
        attrs['extensionAttribute10'] = str(row['extensionattribute10'])
        attrs['streetAddress'] = str(row['streetaddress'])
        attrs['l'] = str(row['l'])
        attrs['st'] = str(row['st'])
        attrs['postalCode'] = str(row['postalcode'])
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

