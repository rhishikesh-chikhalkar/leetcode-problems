
@echo off

set REPO_NAME=leetcode-problems

rem Run the batch file from the cmd directory
call "%github-local-directory%\%REPO_NAME%\cmd\run.cmd" %1
