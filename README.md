# Git Conflict Lab

Practice collaboration between two developers using Git.

## Local setup

This workspace has a starter repository (`git-conflict-lab`), a shared bare remote (`git-conflict-lab-remote.git`), and two working clones (`developer-one` and `developer-two`). The clones use the shared local remote as `origin`, so exercises run without network access. Each clone has a separate practice Git identity; your global Git configuration is unchanged.

## Exercise 1: Sync without a conflict

1. In Developer One, edit the first line of `story.txt`, then commit and push:

   ```powershell
   git add story.txt
   git commit -m "Update opening line"
   git push origin main
   ```

2. In Developer Two, pull the change:

   ```powershell
   git pull --ff-only origin main
   ```

3. Edit a different line in Developer Two, commit and push, then pull in Developer One.

## Exercise 2: Resolve a same-line conflict

Start with both clones up to date.

1. In Developer One, replace the first line of `story.txt`, commit, and push:

   ```powershell
   git add story.txt
   git commit -m "Write developer one's opening"
   git push origin main
   ```

2. Before pulling, replace that same first line differently in Developer Two and commit:

   ```powershell
   git add story.txt
   git commit -m "Write developer two's opening"
   ```

3. Try `git push origin main` from Developer Two. It should be rejected because the remote has a commit it does not have.

4. Merge the remote changes. Git should report a conflict in `story.txt`:

   ```powershell
   git pull --no-rebase origin main
   ```

5. Edit `story.txt`, choose or combine both versions, remove `<<<<<<<`, `=======`, and `>>>>>>>`, then finish the merge:

   ```powershell
   git add story.txt
   git commit -m "Resolve opening line conflict"
   git push origin main
   ```

6. Update Developer One with `git pull --ff-only origin main`.

## Exercise 3: Compare rebase

Repeat Exercise 2 from a fresh state, but use `git pull --rebase origin main`. If Git stops for a conflict, resolve the file and run:

```powershell
git add story.txt
git rebase --continue
git push origin main
```

Restart by recloning both developer folders from the unchanged starter repository.
