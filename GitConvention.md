1. Create a new branch

- `git checkout -b dev/feature-name`
- `git checkout -b fix/bug-name`

2. Add new features or fix bugs

- `git add .`

3. Commit changes

- `git commit -m "Add: feature-name"`
- `git commit -m "Fix: bug-name"`
- `git commit -m "Update: feature-name"`

4. Push to the remote repository

Push the new branch to the remote repository
You are not allowed to push to the master branch or the develop branch directly

- `git push origin dev/feature-name`
- `git push origin fix/bug-name`

5. Pull the latest changes from the remote repository

- `git pull origin develop`
- `git pull origin master`
- `git pull origin dev/feature-name`
- `git pull origin fix/bug-name`

6. Merge latest changes from develop branch to current branch

- `git merge origin/develop`

7. Create a pull request

- Make a pull request from the new branch to the develop branch
- Mustn't make a pull request from the new branch to the master branch
- Mustn't merge the pull request without approval

8. Review and merge
9. Delete the branch

Remove the branch on the local repository

- `git branch -d dev/feature-name`
- `git branch -d fix/bug-name`

And then delete the branch on the remote repository

- `git push origin --delete dev/feature-name`
- `git push origin --delete fix/bug-name`
