# RESTful Routing - Blog Capstone Part 3
A blog to HTTP routes to create, edit, and delete blog posts.

## Requirements
- [X] Be able to GET blog post items
- [X] Be able to POST a new blog post
- [X] Be able to edit existing blog posts
- [X] Be able to DELETE blog posts

## Remarks
For this project, I had a little bit of an easier time figuring things out. However, I realized that I put constraints on myself for no reason.
For example, as a part of requirement 3 I was supposed to 

>Change the make-post.html so that if the user came from "Create New Post" the `<h1>` should read "New Post", but if the user came to edit a particular blog post, it should read "Edit Post".

And because I saw the method passed post_id, I thought I had to do it using post_id and tried to do it like that. Like checking if post_id != None. I wasn't able to figure out why even when post_id was not something being passed at all that it was still showing 'Edit Post' instead of 'New Post'. When I looked at a part of the solution is when I realized I was adding restraints for no reason. They passed a boolean isEdit = True and checked that...