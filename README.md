ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFrjZoDDzBNp3uhZJMxneau99ksJyS3tu1Zrzk673Jfb miye@Mykhailo
# CLI - generator of positive vibe
## Use it when you feel bad

![I ll cry at night (post-rock, indie-rock playlist)](https://github.com/user-attachments/assets/c8084121-7018-4e78-8184-48274172150a)
I took image from this [cool youtube playlist](https://www.youtube.com/watch?v=36C2zYyJ8E0)

# How to install (Linux only)

1. install python and pip:

   Debian/Ubuntu:
   ```shell
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 pip
   sudo apt install python3.10-venv
   ```
   Archlinux:
   ```shell
   sudo pacman -Syu
   sudo pacman -S python
   sudo pacman -S python-pip
   ```
2. clone this reposiroty and build CLI with bash script:
   ```shell
   git clone https://github.com/Vellih0r/I_ll_cry
   cd I_will_cry
   ```
3. Set correct language at tmp.py
   ```shell
   nano ./tmp.py
   ```
4. Start installation script
   ```shell
   ./init.sh
   ````
5. If you delete folder with repository CLI will crash :(((

      ### important files: `config.py`, `helpeng.txt`(depends on lang you choosed)==

   You can delete all, except these 2 files.
