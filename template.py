from github import Github

g=Github('token') #replace token with your API token

repo = g.get_repo("username/repo-name") #e.g. 'LordCatIII/github-api-python-commit'

contents = repo.get_contents("/directory/file") #e.g. 'template.py' or '/files/index.html'

spliced = contents.decoded_content.decode().split('split') #replace split with what you want your document to split at
#remember to add this to the document you want to split, and where you want to split it

input1 = str(input('Input 1 '))

input2 = str(input('Input 2 '))

#spliced[0] is section 1

cont = spliced[0] + input1 + ' ||| ' + input2 + spliced[1]

print(cont)

repo.update_file(contents.path, "Updated file via a python script", cont, contents.sha, branch="main")
#change main to your default branch name
