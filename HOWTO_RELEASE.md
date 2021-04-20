**How to issue a glacier simulator release**

1. Go to your local main repository (not the fork) and ensure your master branch is synced:
```
git checkout master
git pull
```
2. Edit `version.py` to reflect the new version number (`v1.3`, `v1.4`, etc.)
3. On the master branch, commit the release in git:
```
git commit -a -m 'Release v1.X'
```
4. Tag the release:
```
git tag -a v1.X -m 'v1.X'
```
5. Push your changes to master:
```
git push origin master
git push origin --tags
```

6. Edit `version.py` to revert to the dev version (i.e. `v1.X+1.dev`: `v1.4.dev`, `v1.5.dev`, etc.)
7. Edit `README.md` to change the link of the first badge which should point to the latest stable tag (`v1.3.`, `v1.4`, etc.)
8. Commit your changes and push to master again:
```
git commit -a -m 'Revert to dev version'
git push origin master
```
9. Edit the Bokeh server configuration file to publish the new version on OGGM-Edu: https://github.com/OGGM/Bokeh-Docker/blob/master/bokeh.oggm.org/docker-compose.yml

10. Change MyBinder link and docker comment to new version number in OGGM-Edu doccumentation: https://github.com/OGGM/oggm-edu/blob/master/docs/simulator.rst
