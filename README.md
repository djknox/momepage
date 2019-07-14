# Momepage

Momepage is a homepage for Momentum students that provides information on class schedules, guest speakers, field trips, and assignments. Momepage also serves as a project to provide experience with contributing to open-source and collaboration using git.

## Getting Started

To set up a development environment for contributing to Momepage, first clone this repository:

```bash
git clone https://github.com/djknox/momepage.git
```

Next, you will need to ```cd ``` into the momepage directory and install the dependencies listed in the Pipfile with ```pipenv``` (this will also create a virtual environment for you):

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

After following these steps, you will be able to access Momepage in the browser and have your development environment ready to go!


## Contributing
To make a contribution to Momepage, just make a [pull request](https://help.github.com/en/articles/about-pull-requests)!

Here's the basic steps to contributing:

After setting up the development environment, create a new branch for your contribution:

```bash
git checkout -b my-new-feature
```

In the new branch, write the code for whatever you want to add. When the feature is finished, and all changes have been committed, push the branch up to this repo:

```bash
git push --set-upstream origin my-new-feature
```

After pushing your branch, come back to this repo on GitHub and create a new pull request.

When the pull request is accepted, your new code will be merged into the master branch of Momepage and you will have officially contributed to an open-source project!