# Ansible Ubuntu 19.04

## Tested with:

```
ansible >= 2.7.8
```

----------------------------

## 1 - Ansible installation

### 1.1 - Update and upgrade

```
sudo su
apt update && apt upgrade -y
```

### 1.2 - Install [software-properties-common] package

```
apt install software-properties-common
```

### 1.3 - Install ansible

```
apt-add-repository ppa:ansible/ansible
apt update
apt install ansible
ansible --version
```

----------------------------

## 2 - Python 2 and Git Installation

```
sudo apt install python2 python2.7 git
```

----------------------------

## 3 - Enable passwordless sudo for ansible

### 3.1 - Visudo

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

### 3.2 - Add user to sudo group

As root:

```
sudo usermod -a -G sudo <user>
```

----------------------------

### 4 - Download this project

Download this project and put it on **/etc/ansible** dir

```
sudo rm -rf /etc/ansible/
sudo git clone https://github.com/ant-rod-silva/ansible_ubuntu_19_04
sudo mv ansible_ubuntu_1904 /etc/ansible
sudo chown -R $USER:$USER /etc/ansible
```

----------------------------

## 5 - Check if Ansible can access the hosts using Ping

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
sudo mkdir /etc/keys
```

3) As user, generate ssh key

```
ssh-keygen
```

4) Copy private key

```
sudo cp /home/user/.ssh/id_rsa /etc/keys
```

5) Copy public key

```
cat /home/user/.ssh/id_rsa.pub > /tmp/id_rsa.pub
```

6) Log as root

```
sudo su
```

7) Create **/root/.ssh** directory if not exists

```
mkdir /root/.ssh
```

8) Paste the public key inside command 

```
cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys
rm /tmp/id_rsa.pub
```

9) Logout root

```
exit
```

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

----------------------------

## 6 - How to execute playbooks

```
ansible-playbook /etc/ansible/playbooks/01_ubuntu1904_initial.yaml
ansible-playbook /etc/ansible/playbooks/02_ubuntu1904_dev_apps.yaml
ansible-playbook /etc/ansible/playbooks/03_ubuntu1904_zsh.yaml
ansible-playbook /etc/ansible/playbooks/04_ubuntu1904_databases.yaml
ansible-playbook /etc/ansible/playbooks/05_ubuntu1904_lamp_server.yaml
ansible-playbook /etc/ansible/playbooks/06_ubuntu1904_virtualenv.yaml
ansible-playbook /etc/ansible/playbooks/07_ubuntu1904_maintenancetools.yaml
```

To skip update and python2 check steps:

```
ansible-playbook /etc/ansible/playbooks/03_ubuntu1904_zsh.yaml --skip-tags apt_update,python2_check
```

