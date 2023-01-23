# TankYou
Small hobby app to track cbg/cng mileage


Used following command to generate frontend container:
```
    docker run --rm -v "${PWD}:/$(basename `pwd`)" -w "/$(basename `pwd`)" -it node:18.13-alpine sh -c "yarn global add @vue/cli && vue create ."
```