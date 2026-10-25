# Git Conflict Lab

A small repository for practicing Git collaboration with two local developer clones.

## Folders

- `git-conflict-lab`: the starter working repository
- `git-conflict-lab-remote.git`: the shared local bare remote for exercises
- `developer-one`: working clone for Developer One
- `developer-two`: working clone for Developer Two

The developer clones use the shared local remote as `origin`, so the exercises work without network access. Their practice identities are configured locally and do not change your global Git settings. The starter repository publishes to the public GitHub repository `npower3/git-conflict-lab`; after publishing, each developer clone can use a `github` remote to share work online.

## Exercise 1: Sync without a conflict

1. In `developer-one`, change the first line of `story.txt`, commit, and push:

   ```powershell
   git add story.txt
   git commit -m "Update opening line"
   git push origin main
   ```

2. In `developer-two`, get the change:

   ```powershell
   git pull --ff-only origin main
   ```

3. Edit a different line in `story.txt`, then commit and push. Pull again in `developer-one`.

## Exercise 2: Create and resolve a Python conflict

Start with both clones up to date.

1. In `developer-one`, change the return line in `format_result` in `calculator.py` to:

   ```python
   return f"Total: ${result:.2f}"
   ```

   Commit and push:

   ```powershell
   git add calculator.py
   git commit -m "Format total as currency"
   git push origin main
   ```

2. Before pulling, change that same return line in `developer-two` to a different format:

   ```python
   return f"Answer: {result:.2f}"
   ```

   Commit the change:

   ```powershell
   git add calculator.py
   git commit -m "Label formatted answer"
   ```

3. Try pushing from `developer-two`. The push is rejected because the remote has a commit it does not have:

   ```powershell
   git push origin main
   ```

4. Merge the remote changes. Git should report a conflict in `calculator.py`:

   ```powershell
   git pull --no-rebase origin main
   ```

5. Open `calculator.py`, combine the two labels as you like, and remove all conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`). Update the expected string in `test_calculator.py` to match your chosen format. Run the tests, then complete the merge:

   ```powershell
   python -m unittest
   git add calculator.py test_calculator.py
   git commit -m "Resolve calculator format conflict"
   git push origin main
   ```

6. In `developer-one`, update its clone:

   ```powershell
   git pull --ff-only origin main
   ```

## Exercise 3: Compare merge and rebase

Repeat Exercise 2 from a fresh state if you want to compare workflows. For the pull step, use `git pull --rebase origin main` instead of `git pull --no-rebase origin main`. If Git stops for a conflict, resolve the files, stage them, and continue with:

```powershell
git add calculator.py test_calculator.py
git rebase --continue
git push origin main
```

To restart the lab after an exercise, reclone both developer folders from the unchanged starter repository or recreate the local remote and clones.
