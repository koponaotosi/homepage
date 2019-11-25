from utils import *
import sys
print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)

if command == "build":
    print("Build was specified")
    #get files and names
    get_it()
    #form template
    template()
    #update links
    page_linkage()
    #make pages
    main()
elif command == "new":
    print("New page was specified")
    open('content/new_content_page.html', "w+").write("<h1>New Content!</h1><p>New content...</p>")
else:
    print("Please specify ’build’ or ’new’")

