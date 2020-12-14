echo " "
echo "------------------------------------"
echo "Login Test"
echo "------------------------------------"
echo "Running Test with Chrome in headless mode"
echo "------------------------------------"
python tests/TS001LoginSuccessful.py -hl True
echo " "

echo "------------------------------------"
echo "Filter Test"
echo "------------------------------------"
echo "Running automation with Firefox and not in headless mode"
echo "------------------------------------"
python tests/dashboard/TS002FilterByTicketAndCity.py --browser FIREFOX -hl False
echo " "

echo "------------------------------------"
echo "Thanks"
echo "------------------------------------"
