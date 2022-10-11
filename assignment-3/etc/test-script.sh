# Assignemnt 3 // Adrianna Deeb
# script for setAsset alias
# including testing steps along the way

# create asset variable
export asset=goofy

# see if that worked
echo $asset

# create setAsset alias
alias setAsset="export asset=donald"

# see if that worked
setAsset
echo $asset

# enter correct directory
cd /c/Users/adria/code/anim-t380-2022-assignments/assignment-3/etc

# send the results to a txt file called .aliases
echo alias setAsset=\"export asset=mickey\" > .aliases

# see if that worked
source .aliases
setAsset
echo $asset

