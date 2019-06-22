# ansible_ubuntu_1904

## 1 - Initial steps

### 1.1 - Update and upgrade

```
sudo apt-get update
sudo apt-get upgrade
```

### 1.2 - Enable passwordless sudo for ansible

In order to fully control a remote machine we need to be able to execute command on the remote machines as user root. 
There are a number of ways to accomplish this.

On the remote server run:

```
sudo visudo
```

We need to edit the line

```
%sudo   ALL=(ALL:ALL) ALL
```

and look like this:

```
%sudo  ALL=(ALL:ALL) NOPASSWD:ALL
```

We can save the file and exit.

### 1.3 - Add user to sudo group

As root:

```
sudo usermod -a -G sudo <user>
```

### 1.4 - Install ansible

```
sudo apt-get install -y ansible
```

### 1.5 - Download this project

Download this project and put it on **/etc/ansible** dir


## 1.6 - Check if Ansible can access the hosts using Ping

Let's verify that Ansible can access the machine. 
Just as with network you'd use the ping command, Ansible also provides a command called "ping" that checks if the remote machine is accessible to Ansible. 
Instead of sending ICMP packets, the ping of Ansible will try to log in to the remote machine using standard SSH.

Run the following commands:

edit /etc/ansible/ansible.cfg. Uncomment **private_key_file**. Set as:

```
private_key_file = /etc/keys/id_rsa
```

2) Create /etc/keys dir

```
mkdir /etc/keys
```

3) As user, generate ssh key

```
ssh-keygen
```

4) Copy private key

```
cp /home/user/.ssh/id_rsa /etc/keys
```

5) Copy public key

```
cat /home/user/.ssh/id_rsa.pub
```

6) Log as root

7) Create **/root/.ssh** directory if not exists

8) Paste the public key inside command 

```
echo "ssh-rsa key..." >> /root/.ssh/authorized_keys
```

9) Logout root

10) Test

```
ansible local -u root -m ping
```

```
127.0.0.1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

Let's see the details of the command:

* The -t inventory.cfg tells ansible the location of the inventory file.
* local selects the host(s) upon which we'd like to act.
* -u root tells Ansible to use user root on the remote server.
* -m ping tells Ansible to execute the "ping" module.

## 2 - How to execute playbooks

```
ansible-playbook /etc/ansible/playbooks/01_ubuntu_1904_initial.yaml
```
