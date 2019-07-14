# Momepage

Momepage is a homepage for Momentum students that provides information on class schedules, guest speakers, field trips, and assignments. Momepage also serves as a project to provide experience with contributing to open-source and collaboration using git.

## Getting Started

To set up a development environment for contributing to Momepage, first [fork this repository on GitHub](https://help.github.com/en/articles/fork-a-repo). This will create a copy of this repository and put it on your own GitHub profile.

You will then need to clone your forked repository to put it in your local development environment:

```bash
git clone https://github.com/<your-user-name>/momepage.git
```

Next, you will need to ```cd ``` into the momepage directory that was just created and install the dependencies listed in the Pipfile with ```pipenv``` (this will also create a virtual environment for you):

```bash
pipenv install
```

You will then need to activate the virtual environment that was just created:

```bash
pipenv shell
```

Next, run the migrations to create your database structure:

```bash
python3 manage.py migrate
```

Finally, run the server to access Momepage in the browser:

```bash
python3 manage.py runserver
```

After following these steps, you will be able to access Momepage in the browser and your development environment will be all set.


## Contributing
To contribute to Momepage, just make a [pull request](https://help.github.com/en/articles/about-pull-requests)!

Here's the basic steps to contributing:

After setting up the development environment, create a new branch for your contribution:

```bash
git checkout -b my-new-feature
```

In the new branch, write the code for whatever you want to add. When the feature is finished, and all changes have been committed, push the branch up to your forked repo and create a pull request:

First, add this repo (the original momepage repo that you forked) as an upstream repository to your forked repo. This will create a connection between the original repo and your forked repo:

```bash
git remote add upstream https://github.com/djknox/momepage.git
```

Now push your new branch:

```bash
git push origin my-new-feature
```

After pushing your branch, go to your repo on GitHub and [create a new pull request](https://help.github.com/en/articles/creating-a-pull-request).

When the pull request is accepted, your new code will be merged into the master branch of Momepage and you will have officially contributed to an open-source project!

If the feature is completely finished, and the pull request has been accepted, you can get back on your local master branch and pull down the new changes:

```bash
git checkout master
git pull origin master
```

You may also want to delete your completed feature branch:

```bash
git branch -d my-new-feature
```