@echo off
echo ======================================================================
echo             Running EduSaathi Automated Unit Tests
echo        Dept. of AI^&DS, CBIT Hyderabad ^| AICTE-IBM SkillsBuild
echo ======================================================================
echo.
python -m unittest discover -s tests -v
pause
