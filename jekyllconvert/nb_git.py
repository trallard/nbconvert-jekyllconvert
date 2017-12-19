import pygit2
import os

import fnmatch
import glob
from pathlib import Path

class nb_repo(object):
    """ Class containing methods used to
    identify the notebooks committed to the
    repository and add the SHA to the Jinja template"""

    def __init__(self, here):
        try:
            repo_path = pygit2.discover_repository(here)
            repo = pygit2.Repository(repo_path)
            self.repo = repo
            self.here = here
        except:
            raise IOError ('This does not seem to be a repository')


    def check_log(self):
        """ Check the number of commits be"""
        all_commits = [commit for commit in self.repo.head.log()]
        if len(all_commits) <= 1:
            print('Only one commit: converting all notebooks')
            notebooks = find_notebooks()
            return notebooks
        else:
            print(("There are notebooks already in version control",
                   "finding the notebooks passed in the last commit"))
            notebooks = last_commit()
            return noteooks

    def find_notebooks(self):
        """ Find all the notebooks in the repo, but excludes those
        in the _site folder, this will be default if no specific
        notebook was passed for conversion
        """
        basePath = Path(os.getcwd())
        notebooksAll = [nb for nb in glob.glob('**/*.ipynb')]
        exception = os.path.join(basePath, '/_site/*/*')
        notebooks = [nb for nb in notebooksAll if not fnmatch.fnmatch(nb, exception)]

        if not(notebooks) == True:
            print('There were no notebooks found')
        else:
            return notebooks

    def last_commit(self):
        last = repo.revparse_single('HEAD')
        sha1 = last.hex[0:7]
        notebooks = [nb.name for nb in last.tree if '.py' in nb.name]
        nb_coll = {'sha1': sha1,
                   'notebooks': notebooks}
        return nb_coll

