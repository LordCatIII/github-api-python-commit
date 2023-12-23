from github import Github
import datetime
g=Github('token')

repo = g.get_repo("LordCatIII/lordcatiii.github.io")

contents = repo.get_contents("/blabberings/index.html")

spliced = contents.decoded_content.decode().split('<!--comment that helps with updating-->')

title = str(input('Input a title '))
body = str(input('Input a text body '))

cont = spliced[0] + '<!--comment that helps with updating-->\n\n' '''  <details>
  <summary>''' + title + ' ||| ' + str(datetime.datetime.now()) + '''</summary>
  <div.a>
  <p>''' + body + '''</p>
  </div>
  </details>''' + spliced[1]

print(cont)
repo.update_file(contents.path, "Updated index.html via a python script", cont, contents.sha, branch="main")
