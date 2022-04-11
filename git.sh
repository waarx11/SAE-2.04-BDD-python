if [ $# -eq 0 ]
then
    echo "Est ce que t regarder la vidéo de Marc"
    exit 1
fi

git add .

git status

git commit -m "$1"

if git push
then
    echo "Le push à bien fonctionner"
    exit 0
else
    echo "Problème lors du push"
    exit 1
fi