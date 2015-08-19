# github-api-profile

## Objectives

After completing this assignment, you should be able to:

* Demonstrate the use of a 3rd party API
* Recreate a CSS page 

## Details

### Deliverables

* Django repository with code recreating the Github repository page

### Requirements

* No pip or pyflakes errors
* Must implement all features described below 
* Must have tests

## Easy Mode

Recreate the HTML and CSS for the Github tab page (https://github.com/matthiasak?tab=repositories) as your design. Use a Django backend to process the results and pass them to the front end.:

- Your profile: `https://api.github.com/users/<username>`
- Your repos: `https://api.github.com/users/<username>/repos`

After loading data from the Github API, use as least the following in your page:

- name
- blog
- location
- email
- an `<img>` with its source as the avatar_url
- html_url
- for each repo owned by your user, list that repo in a `<ul>` with the description and the last_updated info.

