pages = []
def get_it():
    #get files
    import glob
    all_html_files = glob.glob("content/*.html")
    #get names
    import os
    for html_file in all_html_files:
        file_name = os.path.basename(html_file)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
            "filename": html_file,
            "title": name_only,
            "output": "docs/" + file_name,
            "file_name": file_name
        })




#template
top_html = open('templates/top.html').read()
bottom_html = open('templates/bottom.html').read()

def template():
    base_html = top_html + "{{content}}" + bottom_html
    open('templates/base.html', 'w+').write(base_html)
    template = open("templates/base.html").read()
    return template



#page_links
page_links = []
def page_linkage():
    for page in pages:
        page_links.append('<li><a href="file:///home/kotosi/Downloads/homepage-master/homepage/' + page["output"] + '">' + page["title"] + '</a></li>')

#glue
def main():
#    for page in pages:
#        page_filename = page["filename"]
#        page_output = page["output"]
#        content = open(page_filename).read()
#        finished_page = template().replace("{{content}}", content)
#        shoot = open(page_output, "w+").write(finished_page)
        
    from jinja2 import Template
    for page in pages:
        page_filename = page["filename"]
        page_output = page["output"]
        page_html = open(page_filename).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        shoot = template.render(
                    title=page["title"],
                    content=page_html,
                    some_page_link=page_links,
        )
        score = open(page_output, "w+").write(shoot)
    return score



