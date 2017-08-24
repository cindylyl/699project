# 699project

useful git commands & steps to manage our project
```bash
# clone project for the first time
git clone https://github.com/zhang1oc/699project.git

cd 699project/

# edit files

git add .
git commit -m "write your comments here"
git push


# for later editing
# remember to type following commands before changing files to get lastest version of project each time
git pull
# edit files
git add .
git commit -m "write your comments here"
git push

```

---
export data

```bash
python manage.py dumpdata [app_name] > xxx.json
```

import data

```bash
python manage.py loaddata xxx.json
```