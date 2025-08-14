from graphviz import Digraph

# Create the ER diagram
dot = Digraph(comment="Blogging Website ER Diagram", format="png")
dot.attr(rankdir="LR", fontsize="10")

# Entities
dot.node("users", "auth.users\n(Supabase)", shape="box", style="filled", fillcolor="#FFDDC1")
dot.node("profiles", "profiles\n(id PK, username, bio, avatar_url)", shape="box", style="filled", fillcolor="#FFABAB")
dot.node("categories", "categories\n(id PK, name)", shape="box", style="filled", fillcolor="#FFC3A0")
dot.node("posts", "posts\n(id PK, title, content, cover_image_url)", shape="box", style="filled", fillcolor="#FF677D")
dot.node("comments", "comments\n(id PK, content)", shape="box", style="filled", fillcolor="#D4A5A5")
dot.node("bookmarks", "bookmarks\n(id PK, user_id, post_id)", shape="box", style="filled", fillcolor="#392F5A", fontcolor="white")
dot.node("likes", "likes\n(id PK, user_id, post_id)", shape="box", style="filled", fillcolor="#31A2AC", fontcolor="white")
dot.node("post_views", "post_views\n(id PK, post_id, user_id, viewed_at)", shape="box", style="filled", fillcolor="#61C0BF")

# Relationships
dot.edge("users", "profiles", label="1 - 1")
dot.edge("users", "posts", label="1 - many (author_id)")
dot.edge("users", "comments", label="1 - many (author_id)")
dot.edge("users", "bookmarks", label="1 - many")
dot.edge("users", "likes", label="1 - many")
dot.edge("users", "post_views", label="1 - many")

dot.edge("categories", "posts", label="1 - many")

dot.edge("posts", "comments", label="1 - many")
dot.edge("posts", "bookmarks", label="1 - many")
dot.edge("posts", "likes", label="1 - many")
dot.edge("posts", "post_views", label="1 - many")

# Render to file
file_path = 'blogging_er_diagram'
dot.render(file_path, cleanup=True)

file_path + ".png"
