class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.author.username}: {self.content}"


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = set()

    def addComment(self, comment):
        self.comments.append(comment)

    def addLike(self, user):
        if user not in self.likes:
            self.likes.add(user)

    def __str__(self):
        return f"Post by {self.author.username}: {self.content} ({len(self.likes)} likes)"


class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def addFriend(self, user):
        self.friends.add(user)
        user.friends.add(self)

    def createPost(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def commentOnPost(self, post, content):
        comment = Comment(content, self)
        post.addComment(comment)
        return comment

    def likePost(self, post):
        post.addLike(self)

    def __str__(self):
        return f"User: {self.username}"

user1 = User("User1")
user2 = User("User2")
user1.addFriend(user2)


post1 = user1.createPost("Guys I think I failed my exams...")
comment1 = user2.commentOnPost(post1, "It's okay, we all fam.")
user2.likePost(post1)
for p in user1.posts:
    print(p)
    for c in p.comments:
        print(f"  Comment: {c}")