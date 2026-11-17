#!/bin/bash
# Task 2 - Linux commands practice (safe: everything happens inside a temp sandbox directory)
# Run:  bash linux_practice.sh
set -u
SANDBOX=$(mktemp -d /tmp/linux_practice.XXXXXX)
cd "$SANDBOX" || exit 1

section() { echo; echo "=== $1 ==="; }

section "pwd - print working directory"; pwd
section "mkdir - make directories";       mkdir -p project/docs project/src; ls
section "cd - change directory";          cd project && pwd
section "touch - create empty files";     touch notes.txt src/main.py docs/readme.md; ls -R
section "redirection (> and >>)"
echo "line one" > notes.txt
echo "line two" >> notes.txt
echo "line three" >> notes.txt
seq 1 30 > numbers.txt
echo "wrote notes.txt and numbers.txt"
section "cat - show file";                cat notes.txt
section "file - detect file type";        file notes.txt src/main.py .
section "more / less (non-interactive demo)"
echo "(more/less are pagers; here we pipe through head to show the idea)"
head -n 15 numbers.txt | timeout 5 more | head -3
section "head";                           head -n 5 numbers.txt
section "cp - copy";                      cp notes.txt notes_backup.txt; ls
section "mv - move/rename";               mv notes_backup.txt docs/; mv docs/notes_backup.txt docs/backup_renamed.txt; ls docs
section "alias";                          shopt -s expand_aliases; alias ll='ls -l'; alias ll; ll notes.txt
section "chmod - permissions"
echo 'echo "Hello from script.sh"' > script.sh
ls -l script.sh; chmod +x script.sh; ls -l script.sh
section "bash / sh - run a script";       bash script.sh; sh script.sh
section "ps and kill"
sleep 300 &
PID=$!
ps -p "$PID" -o pid,comm
kill "$PID"; wait "$PID" 2>/dev/null
echo "process $PID killed"
ps -p "$PID" >/dev/null 2>&1 && echo "still running" || echo "confirmed: process is gone"
section "man (manual page, first lines)"
(timeout 10 man ls 2>/dev/null | head -5) || true
command -v man >/dev/null || echo "man not installed here; try: man ls"
section "dpkg - list installed packages (first 5)"
(dpkg -l 2>/dev/null | head -8) || echo "dpkg not available (non-Debian system)"
section "rm and rmdir"
rm docs/backup_renamed.txt; rm docs/readme.md
rmdir docs && echo "docs removed (rmdir works only on empty directories)"
rm -r src && echo "src removed (rm -r removes a non-empty directory)"
ls
section "Commands NOT executed in this script (need root / affect the system)"
cat <<'TXT'
sudo apt update && sudo apt upgrade   # package update and upgrade (sudo = run as administrator)
sudo dpkg -i package.deb              # install a .deb package
sudo shutdown -h now                  # power off
sudo shutdown -r now  /  sudo reboot  # restart
nano file.txt                         # terminal text editor (Ctrl+O save, Ctrl+X exit)
printenv / export NAME=value          # environment variables
TXT
cd / && rm -rf "$SANDBOX"
echo; echo "Done. Sandbox removed."
