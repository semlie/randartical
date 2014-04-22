import pymysql
class makeArtical(object):
    
    def __init__(self, dbName='mysql'):
        self.db =dbName
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db=self.db ,charset='utf8')
    
    def select(self, q):
        cur = self.conn.cursor()
        cur.execute(q)
        return cur.fetchall()

    def getDataFromFile(self,fil ):
        s =[]
        with open( fil, 'r+') as f:
            s=f.read().split('\n')
        print [x for x in s]
   
#r = makeArtical ('smulik')
#s=r.getDataFromFile('c:\\xp\\genr.txt')
#a=r.select("Select `result` FROM  `firstlevelquery_trufotsabta` ")
#v=[x for x in a]
#with open('c:\\xp\\ll.txt','w+')as f:
#    for x in a:
#        f.write(x[0].encode('utf-8'))
#
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
class addToWordpress(object):
    
    def __init__(self, arg):
        self.url=arg['url']
        self.user=arg['user']
        self.pas=arg['pas']
        print arg['url'],arg['user'],arg['pas']
        self.host=Client(self.url, self.user, self.pas)
        
    def addPost(self,pst ):
        post = WordPressPost()
        post.title = pst['title']
        post.content = pst['content']
        post.terms_names = {'post_tag': pst['tags'], 'category': pst['category']}
        print post
        post_status = 'publish'
        self.host.call(NewPost(post))
        print 'done'

#test it
def main():
    url={'url':'http://127.0.0.1/wp/xmlrpc.php',
         'user':'admin',
         'pas':'123456'}
    wp = addToWordpress(url)
    post={'title':"my Title",
          'content':'my content',
          'tags':["rr","tt"],
            'category':["classic","super"]}
    wp.addPost(post)

if __name__ == '__main__':
    main()
