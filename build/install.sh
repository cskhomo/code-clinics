#!/bin/bash

# Setup local storage for clinic
CLINIC="$HOME/.code-clinic"
mkdir -p $CLINIC/cache

if [ $? -eq 0 ]; then

    if ! grep -q "export CACHE=$CLINIC/cache" ~/.bashrc; then
        echo "export CACHE=$CLINIC/cache" >> ~/.bashrc
    fi

    echo -e "\033[32mSuccessfully setup local storage \033[0m"
    else
        echo -e "\033[31mFailed to setup local storage \033[0m"
    exit 1
fi


# Configure secrets directory
if [ -d "$CLINIC/secrets" ] || { [ -d secrets/ ] && mv -n secrets $CLINIC; }; then

    if ! grep -q "export CREDENTIALS=$CLINIC/secrets/credentials.json" ~/.bashrc; then
        echo "export CREDENTIALS=$CLINIC/secrets/credentials.json" >> ~/.bashrc
    fi

    if ! grep -q "export TOKEN=$CLINIC/secrets/token.json" ~/.bashrc; then
        echo "export TOKEN=$CLINIC/secrets/token.json" >> ~/.bashrc
    fi

    if ! grep -q "export IDENTITY=$CLINIC/secrets/identity.json" ~/.bashrc; then
        echo "export IDENTITY=$CLINIC/secrets/identity.json" >> ~/.bashrc
    fi

    echo -e "\033[32mSuccessfully stored user secrets \033[0m"
    else
    echo -e "\033[31mNo secrets directory found \033[0m"
fi


# Install clinic package
if ! pip show clinic > /dev/null 2>/dev/null; then
    cp setup.py ../
    pip install --user --editable ../
    rm ../setup.py
else
    echo -e "\033[32mClinic package is already installed \033[0m"
fi


# Configure PATH environment variable
if ! grep -q "export PATH=\$PATH:~/.local/bin" ~/.bashrc; then
    echo "export PATH=\$PATH:~/.local/bin" >> ~/.bashrc
fi


# Configure aliases for student and volunteer
if ! grep -q "alias student='clinic student'" ~/.bashrc; then
    echo "alias student='clinic student'" >> ~/.bashrc
fi

if ! grep -q "alias volunteer='clinic volunteer'" ~/.bashrc; then
    echo "alias volunteer='clinic volunteer'" >> ~/.bashrc
fi


# Finalize setup
echo -e "\033[32mCommand-line tool 'clinic' ready for use\033[0m"
echo -e "\033[32mPlease wait...\033[0m"
sleep 5