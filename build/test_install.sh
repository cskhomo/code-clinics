CLINIC="$HOME/.code-clinic"

[ -d "$CLINIC" ] && echo -e "\033[32mFound .code-clinic/ \033[0m" || echo -e "\033[31m.code-clinic/ does not exist \033[0m"
[ -d "$CLINIC/cache" ] && echo -e "\033[32mFound cache/ \033[0m" || echo -e "\033[31mcache/ does not exist \033[0m"
[ -d "$CLINIC/secrets" ] && echo -e "\033[32mFound secrets/ \033[0m" || echo -e "\033[31msecrets/ does not exist \033[0m"

type clinic &> /dev/null && echo -e "\033[32mclinic installed\033[0m" || echo -e "\033[31mclinic not installed\033[0m"
grep -q "alias student=" ~/.bashrc && echo -e "\033[32mstudent configured\033[0m" || echo -e "\033[31mstudent not configured\033[0m"
grep -q "alias volunteer=" ~/.bashrc && echo -e "\033[32mvolunteer configured\033[0m" || echo -e "\033[31mvolunteer not configured\033[0m"