#!/usr/bin/env python3

__author__ = 'Joseph Reid'

import datetime
import string
import glob
import os
import copy
from jinja2 import Template
import markdown


def main():
    """
    main() - Main Loop for Static Site Generator.
    """
    BLOG_BASE = 'templates/blog_base.html'
    SITE_BASE = 'templates/base.html'

    gen_blog_posts(BLOG_BASE,SITE_BASE)
    gen_index_page()
    gen_projects_page()
    gen_site_pages(SITE_BASE)

def gen_site_pages(site_base):
    site_template_html = get_page_template(site_base)
    site_template = Template(site_template_html)

    site_pages = get_page_names(root="content",ext=".html")

    for page in site_pages:
        options = {'title':'Joseph\s Blog',
                   'index':'',
                   'projects':'',
                   'contact':'',
                   'content':'',
                   'year':datetime.datetime.now().year,
                   'project_pages':''}
        options['content'] = get_content(page)
        options[os.path.splitext(page)[0]] = 'active'
        #todo move render call to seperate file
        output_file = site_template.render(**options)
        open(os.path.join("docs",page),'w').write(output_file)

def get_page_names(root,ext):
    """
    get_page_names(root)

    Returns list of html files in directory root.
    """
    path_to_posts = os.path.join(root,'*'+ ext)
    pages = glob.glob(path_to_posts)
    return [os.path.basename(page) for page in pages]

def get_page_template(template):
    """
    get_page(template)

    Returns string with template file specified by input var.
    """
    return open(template).read()

def get_content(page):
    """
    get_page(template)

    Returns string with page content specified by input var.
    """
    return get_page(os.path.join("content",page))

def gen_blog_posts(blog_posts,index_formatting,blog_base,site_base):
    """
    gen_blog_posts() - Generates html blog posts from markdown files in blog/
    """
    blog_base_template = get_page_template(blog_base)
    site_base_template = get_page_template(site_base)
    blog_pages = get_page_names(root="blog",ext='.md')

    # for page in blog_pages:
    #
    #
    #
    #
    #     options = {'title':'Joseph\s Blog',
    #                'index':'',
    #                'projects':'',
    #                'contact':'',
    #                'content':'',
    #                'year':datetime.datetime.now().year,
    #                'project_pages':''}
    #     options['content'] = get_content(page)
    #     options[os.path.splitext(page)[0]] = 'active'
    #     #todo move render call to seperate file
    #     output_file = site_template.render(**options)
    #     open(os.path.join("docs",page),'w').write(output_file)


#     blog_posts = gen_blog_post_list()
#     other_pages = gen_other_pages()
#
#     INDEX_PAGE = 'docs/index.html'
#     INDEX_FORMATTING = {'title':'Joseph\'s Blog',
#                               'index':'active',
#                               'projects':'',
#                               'contact':'',
#                                }
#     BLOG_BASE ='templates/blog_base.html'
#     SITE_BASE ='templates/base.html'
#     BLOG_PREVIEW_BASE='templates/index_blog_preview_base.html'
#     INDEX_BASE = 'templates/index_base.html'
#
#     gen_blog_posts(blog_posts,INDEX_FORMATTING,BLOG_BASE,SITE_BASE)
#     gen_index_page(blog_posts,INDEX_PAGE,INDEX_FORMATTING,SITE_BASE,BLOG_PREVIEW_BASE,INDEX_BASE)
#     gen_content_pages(SITE_BASE,other_pages)
#
# def gen_blog_post_list():
#     blog_dict = {'content_file':'',
#                     'ouput_file':'',
#                     'formatting':{'blog_title':'',
#                                   'publication_date':'',
#                                   'img_link':'',
#                                   'image_subtext':'',
#                                   'blog_text':'',
#                                   'output_link':'',
#                                    }}
#     blog_pages = glob.glob("blog/*.html")
#     output = []    #todo better formatting for page details
#
#     print(blog_pages)
#     for page in blog_pages:
#         page_base = os.path.basename(page)
#         blog_dict['content_file'] = os.path.join("blog",page_base)
#         blog_dict['ouput_file'] = os.path.join("docs",page_base)
#         blog_dict['formatting']["blog_title"] = page_base.split('.')[0]
#         output.append(copy.deepcopy(blog_dict))
#     print(output)
#     return output


# def gen_other_pages():
#     return [{'filename':'content/projects.html',
#                    'output':'docs/projects.html',
#                    'formatting':{'title':'Joseph\'s Projects',
#                                  'index':'',
#                                  'projects':'active',
#                                  'contact':'',
#                                   }},
#                   {'filename':'content/contact.html',
#                   'output':'docs/contact.html',
#                   'formatting':{'title':'Contact Me',
#                                 'index':'',
#                                 'projects':'',
#                                 'contact':'active',
#                              }}]
#
#     INDEX_PAGE = 'docs/index.html'
#     INDEX_FORMATTING = {'title':'Joseph\'s Blog',
#                               'index':'active',
#                               'projects':'',
#                               'contact':'',
#                                }
#
#     BLOG_BASE ='templates/blog_base.html'
#     SITE_BASE ='templates/base.html'
#     BLOG_PREVIEW_BASE='templates/index_blog_preview_base.html'
#     INDEX_BASE = 'templates/index_base.html'
#
#     gen_blog_posts(BLOG_POSTS,INDEX_FORMATTING,BLOG_BASE,SITE_BASE)
#     gen_index_page(BLOG_POSTS,INDEX_PAGE,INDEX_FORMATTING,SITE_BASE,BLOG_PREVIEW_BASE,INDEX_BASE)
#     gen_content_pages(SITE_BASE,OTHER_PAGES)
#     # addCopyRight()
#

# def gen_index_page(blog_posts,index_page,index_formatting,site_base,blog_preview_base,index_base):
#     """
#     gen_index_page(blog_posts,index_formatting,blog_base,site_base)
#
#     Generates blog post preview elements on site landing page.
#     """
#
#     index_blog_preview_template = get_page(blog_preview_base)
#     blog_post_previews = ''
#     for post in blog_posts:
#         formatting = post['formatting']
#         blog_content = get_page(post['content_file'])
#         first_par = ''.join(blog_content.split('</p>')[:2]) + '</p>'
#         formatting['blog_text']=first_par #need to truncate blog text better
#         blog_post_previews += index_blog_preview_template.format(**formatting)
#     site_template = get_page(site_base)
#     index_template = get_page(index_base)
#     index_formatting['content'] = index_template.format(blog_posts=blog_post_previews)
#     open(index_page,'w').write(site_template.format(**index_formatting))
#
# def gen_content_pages(site_base,other_pages):
#     """
#     genContntPages() - Generates other pages.
#     """
#     template = get_page(site_base)
#     for page in other_pages:
#         formatting = page['formatting']
#         formatting['content'] = open(page['filename']).read()
#         open(page['output'],'w').write(template.format(**formatting))




# def addCopyRight(index_page,blog_posts,other_pages):
#     year = datetime.datetime.now().year
#     blogpages = [page['ouput_file'] for page in blog_posts]
#
#     other_pages =
#
#     pages = index_page +


if __name__ == '__main__':
    main()
